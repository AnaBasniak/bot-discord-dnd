import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
import psycopg2


# =========================================================
# VARIÁVEIS DE AMBIENTE
# =========================================================

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")


# =========================================================
# INTENTS
# =========================================================

intents = discord.Intents.default()


# =========================================================
# BOT
# =========================================================

class MiniMestre(commands.Bot):

    def __init__(self):
        
        super().__init__(
            command_prefix="!",
            intents=intents
        )

    async def setup_hook(self):

    await self.load_extension(
        "mini_mestre.cogs.fichas"
    )

    await self.load_extension(
        "mini_mestre.cogs.consultar_ficha"
    )

    await self.load_extension(
        "mini_mestre.cogs.pv"
    )

    await self.load_extension(
        "mini_mestre.cogs.inventario"
    )

    comandos = await self.tree.sync()

    print(
        f"{len(comandos)} comando(s) "
        "sincronizado(s) com o Discord."
    )
    
# =========================================================
# EVENTOS
# =========================================================

@bot.event
async def on_ready():
    print(
        f"Mini Mestre conectado como {bot.user}"
    )


# =========================================================
# COMANDO DE TESTE
# =========================================================

@bot.tree.command(
    name="teste",
    description="Testa se o Mini Mestre está funcionando."
)
async def teste(interaction: discord.Interaction):

    await interaction.response.send_message(
        "Funcionando! O Mini Mestre está vivo!",
        ephemeral=True
    )


# =========================================================
# TESTE DO POSTGRESQL
# =========================================================

try:
    conexao = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    print(
        "Conexão com PostgreSQL realizada com sucesso!"
    )

    conexao.close()

except Exception as erro:

    print(
        "Erro ao conectar ao PostgreSQL:"
    )

    print(erro)


# =========================================================
# INICIAR BOT
# =========================================================

if not TOKEN:

    raise RuntimeError(
        "DISCORD_TOKEN não foi encontrado."
    )


bot.run(TOKEN)