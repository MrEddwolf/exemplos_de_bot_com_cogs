import discord
import os
import datetime
from discord.ext import commands
from dotenv import load_dotenv

server_id = discord.Object(id=id_do_servidor_aqui)


date = datetime.datetime.today()
now = date.strftime('%d-%m-%Y %H:%M:%S')

class MyClient(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True  # Isso é necessário para usar comandos de texto
        super().__init__(
            command_prefix="!",
            intents=intents,
        )

    async def setup_hook(self):

        # Carrega todos os arquivos .py que estão dentro da pasta cogs
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py') and not filename.startswith("__"):
                await bot.load_extension(f'cogs.{filename[:-3]}')

        self.tree.copy_global_to(guild=server_id)
        await self.tree.sync(guild=server_id) 

bot = MyClient()

@bot.event
async def on_ready():
    print(f"\033[1;34m{now}\033[1;34m INFO  \033[1;33m   {bot.user.name} \033[m está online! ✔️")

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
