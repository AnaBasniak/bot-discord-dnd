import discord
from discord import app_commands
from discord.ext import commands

from mini_mestre.services.ficha_service import (
    alterar_pv,
    buscar_personagem,
    listar_personagens_jogador,
    pode_acessar_personagem,
)


class SelecionarPersonagemPVView(
    discord.ui.View
):

    def __init__(
        self,
        user_id,
        personagens,
        valor
    ):
        super().__init__(
            timeout=300
        )

        self.user_id = user_id
        self.personagens = personagens
        self.valor = valor

        select = discord.ui.Select(
            placeholder="Escolha o personagem",
            min_values=1,
            max_values=1,
            options=[
                discord.SelectOption(
                    label=personagem["nome"],
                    description=(
                        f"{personagem['classe']} "
                        f"• PV "
                        f"{personagem['pv_atual']}/"
                        f"{personagem['pv_maximo']}"
                    ),
                    value=str(
                        personagem["id"]
                    )
                )
                for personagem
                in personagens[:25]
            ]
        )

        select.callback = self.escolher

        self.select = select

        self.add_item(
            select
        )

    async def interaction_check(
        self,
        interaction
    ):
        if interaction.user.id != self.user_id:

            await interaction.response.send_message(
                (
                    "❌ Esse menu pertence "
                    "a outro jogador."
                ),
                ephemeral=True
            )

            return False

        return True

    async def escolher(
        self,
        interaction
    ):
        personagem_id = int(
            self.select.values[0]
        )

        if not pode_acessar_personagem(
            interaction.user.id,
            personagem_id
        ):

            await interaction.response.send_message(
                (
                    "❌ Você não pode alterar "
                    "o PV dessa ficha."
                ),
                ephemeral=True
            )

            return

        await aplicar_alteracao(
            interaction,
            personagem_id,
            self.valor,
            editar=True
        )


async def aplicar_alteracao(
    interaction,
    personagem_id,
    valor,
    editar=False
):
    personagem = buscar_personagem(
        personagem_id
    )

    if personagem is None:

        if editar:
            await interaction.response.edit_message(
                content="❌ Ficha não encontrada.",
                view=None
            )

        else:
            await interaction.response.send_message(
                "❌ Ficha não encontrada.",
                ephemeral=True
            )

        return

    try:
        resultado = alterar_pv(
            personagem_id,
            valor
        )

    except Exception as erro:
        print(
            "Erro ao alterar PV:"
        )
        print(
            erro
        )

        if editar:
            await interaction.response.edit_message(
                content=(
                    "❌ Ocorreu um erro "
                    "ao alterar o PV."
                ),
                view=None
            )

        else:
            await interaction.response.send_message(
                (
                    "❌ Ocorreu um erro "
                    "ao alterar o PV."
                ),
                ephemeral=True
            )

        return

    if valor < 0:
        acao = "Dano"

    elif valor > 0:
        acao = "Cura"

    else:
        acao = "Sem alteração"

    embed = discord.Embed(
        title="❤️ Pontos de Vida",
        description=(
            f"**{personagem['nome']}**"
        )
    )

    embed.add_field(
        name="Ação",
        value=(
            f"{acao}: "
            f"{valor:+d}"
        ),
        inline=True
    )

    embed.add_field(
        name="Antes",
        value=str(
            resultado["antes"]
        ),
        inline=True
    )

    embed.add_field(
        name="Agora",
        value=(
            f"{resultado['depois']}/"
            f"{resultado['maximo']}"
        ),
        inline=True
    )

    if resultado["depois"] == 0:

        embed.add_field(
            name="⚠️ Estado",
            value=(
                "O personagem está com "
                "**0 PV**."
            ),
            inline=False
        )

    elif (
        resultado["depois"]
        ==
        resultado["maximo"]
    ):

        embed.add_field(
            name="✨ Estado",
            value=(
                "O personagem está com "
                "**PV máximo**."
            ),
            inline=False
        )

    if editar:

        await interaction.response.edit_message(
            content=None,
            embed=embed,
            view=None
        )

    else:

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )


class PV(
    commands.Cog
):

    def __init__(
        self,
        bot
    ):
        self.bot = bot

    @app_commands.command(
        name="pv",
        description=(
            "Aplica dano ou cura "
            "ao seu personagem."
        )
    )
    @app_commands.describe(
        valor=(
            "Use negativo para dano "
            "e positivo para cura. "
            "Ex.: -50 ou 10"
        )
    )
    async def pv(
        self,
        interaction: discord.Interaction,
        valor: int
    ):
        personagens = (
            listar_personagens_jogador(
                interaction.user.id
            )
        )

        if not personagens:

            await interaction.response.send_message(
                (
                    "❌ Você ainda não possui "
                    "nenhuma ficha."
                ),
                ephemeral=True
            )

            return

        if len(personagens) == 1:

            personagem = personagens[0]

            await aplicar_alteracao(
                interaction,
                personagem["id"],
                valor
            )

            return

        view = SelecionarPersonagemPVView(
            interaction.user.id,
            personagens,
            valor
        )

        await interaction.response.send_message(
            (
                f"❤️ Alteração de PV: "
                f"**{valor:+d}**\n\n"
                "Escolha o personagem:"
            ),
            view=view,
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(
        PV(bot)
    )