import discord
from discord.ext import commands
from discord import app_commands

class ServerInfo(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Exemplo de comando com prefixo (!)
    @commands.command(pass_context=True)
    async def oi(self, ctx):
        await ctx.send("Olá, Wumpus! Este é um Prefix Command...")

    # Exemplo de comando com slash (/)
    @app_commands.command()
    async def ola(self, interaction: discord.Interaction):
        await interaction.response.send_message("Olá, Wumpus! Este é um Slash Command...")

    # Exemplo de comando com ambos (! ou /)
    @commands.hybrid_command(name="ping")
    async def ping(self, ctx: commands.Context) -> None:
        await ctx.send(f"⏱️ | `{round(self.bot.latency*1000,2)}ms!`")

async def setup(bot: commands.Bot):
    await bot.add_cog(ServerInfo(bot))