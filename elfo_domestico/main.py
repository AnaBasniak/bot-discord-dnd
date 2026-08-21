import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from mini_mestre.database import conectar


# =========================================================
# VARIÁVEIS DE AMBIENTE
# =========================================================

load_dotenv()

TOKEN = os.getenv(
    "ELFO_DISCORD_TOKEN"
)


# =========================================================
# INTENTS
# =========================================================

intents = discord.Intents.default()


# =========================================================
# BOT
# =========================================================

class ElfoDomestico(
    commands.Bot
):

    def __init__(
        self
    ):
        super().__init__(
            command_prefix="!",
            intents=intents
        )

    async def setup_hook(
        self
    ):

        # ================================================
        # COGS
        # ================================================

        await self.load_extension(
            "elfo_domestico.cogs.magias"
        )

        # ================================================
        # SINCRONIZAR COMANDOS
        # ================================================

        comandos = await self.tree.sync()

        print(
            f"{len(comandos)} comando(s) "
            "sincronizado(s) com o Discord."
        )


bot = ElfoDomestico()


# =========================================================
# EVENTO DE INICIALIZAÇÃO
# =========================================================

@bot.event
async def on_ready():

    print(
        "===================================="
    )

    print(
        f"Elfo Doméstico conectado como "
        f"{bot.user}"
    )

    print(
        "===================================="
    )


# =========================================================
# COMANDO DE TESTE
# =========================================================

@bot.tree.command(
    name="teste_elfo",
    description=(
        "Testa se o Elfo Doméstico "
        "está funcionando."
    )
)
async def teste_elfo(
    interaction: discord.Interaction
):

    await interaction.response.send_message(
        "🧝 Elfo Doméstico está funcionando!",
        ephemeral=True
    )


# =========================================================
# TESTAR BANCO
# =========================================================

def testar_banco():

    conexao = None
    cursor = None

    try:
        conexao = conectar()

        cursor = conexao.cursor()

        cursor.execute(
            """
            SELECT CURRENT_DATABASE();
            """
        )

        banco = cursor.fetchone()[0]

        print(
            "Conexão com PostgreSQL "
            "realizada com sucesso!"
        )

        print(
            f"Banco utilizado: {banco}"
        )

    except Exception as erro:

        print(
            "Erro ao conectar ao PostgreSQL:"
        )

        print(
            erro
        )

    finally:

        if cursor is not None:
            cursor.close()

        if conexao is not None:
            conexao.close()


# =========================================================
# INICIAR
# =========================================================

if __name__ == "__main__":

    if not TOKEN:

        raise RuntimeError(
            "ELFO_DISCORD_TOKEN não foi "
            "encontrado no arquivo .env."
        )

    testar_banco()

    bot.run(
        TOKEN
    )