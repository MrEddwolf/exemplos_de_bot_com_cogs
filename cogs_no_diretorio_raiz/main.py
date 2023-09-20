import discord
import os
import datetime
from discord.ext import commands
from dotenv import load_dotenv

# ID do servidor Discord
server_id = discord.Object(id= 717615951113093130)

# Obtendo a data e hora atual
date = datetime.datetime.today()
now = date.strftime('%d-%m-%Y %H:%M:%S')

# Classe MyClient derivada de commands.Bot
class MyClient(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True  # Isso é necessário para usar comandos de texto
        super().__init__(
            command_prefix="!",
            intents=intents,
        )

    async def setup_hook(self):

        # Itera sobre todos os arquivos e diretórios no diretório atual
        for filename in os.listdir('.'):
        
        # Verifica se o arquivo possui a extensão ".py" e não é o próprio "main.py"
            if filename.endswith('.py') and filename != 'main.py':
                
                # Remove a extensão ".py" do nome do arquivo.
                cog_name = filename[:-3]  

                # Carrega o cog como uma extensão utilizando o método "load_extension()"
                await bot.load_extension(cog_name)
            
        # Copia as configurações globais para o servidor especificado
        self.tree.copy_global_to(guild=server_id)

        # Sincroniza as configurações do bot para o servidor especificado
        await self.tree.sync(guild=server_id) 

# Instanciando o bot
bot = MyClient()

# Evento on_ready é disparado quando o bot estiver pronto
@bot.event
async def on_ready():
    print(f"\033[1;34m{now}\033[1;34m INFO  \033[1;33m   {bot.user.name} \033[m está online! ✔️")

# Sincroniza os dados para um servidor específico ou para todos os servidores.
@bot.command()
@commands.is_owner() 
async def sync(ctx,guild=None):
    if guild == None:
        await bot.tree.sync()
    else:
        await bot.tree.sync(guild=discord.Object(id=int(guild)))
    await ctx.send("Synced")

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Inicia o bot usando o token fornecido
bot.run(TOKEN)
