import os

import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import psycopg2


# =========================================================
# VARIÁVEIS DE AMBIENTE
# =========================================================

load_dotenv()

TOKEN = os.getenv(
    "DISCORD_TOKEN"
)


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

        # Carrega os comandos de ficha
        await self.load_extension(
            "mini_mestre.cogs.fichas"
        )

        # Sincroniza slash commands com Discord
        comandos = await self.tree.sync()

        print(
            f"{len(comandos)} comando(s) "
            "sincronizado(s) com o Discord."
        )


bot = MiniMestre()


# =========================================================
# EVENTO DE CONEXÃO
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
async def teste(
    interaction: discord.Interaction
):

    await interaction.response.send_message(
        "Funcionando! O Mini Mestre está vivo!",
        ephemeral=True
    )


# =========================================================
# TESTAR POSTGRESQL
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
        "DISCORD_TOKEN não foi encontrado no arquivo .env."
    )


bot.run(
    TOKEN
)