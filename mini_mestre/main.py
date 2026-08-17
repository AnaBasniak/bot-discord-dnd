import os

import discord
from discord import app_commands
from dotenv import load_dotenv
import psycopg2

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()

bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)


@bot.event
async def on_ready():
    await tree.sync()
    print(f"Mini Mestre conectado como {bot.user}")


@tree.command(
    name="teste",
    description="Testa se o Mini Mestre está funcionando."
)
async def teste(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Funcionando! O Mini Mestre está vivo!"
    )

try:
    conexao = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    print("Conexão com PostgreSQL realizada com sucesso!")

    conexao.close()

except Exception as erro:
    print("Erro ao conectar ao PostgreSQL:")
    print(erro) 
    
bot.run(TOKEN)