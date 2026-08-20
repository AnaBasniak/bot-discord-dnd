import discord
from discord import app_commands
from discord.ext import commands

from mini_mestre.services.ficha_service import (
    buscar_personagem,
    listar_bau,
    listar_personagens_jogador,
    recalcular_ca_personagem,
    transferir_bau_para_inventario,
    transferir_inventario_para_bau,
)


# =========================================================
# EMBED DO BAÚ
# =========================================================

def criar_embed_bau():
    itens = listar_bau()

    embed = discord.Embed(
        title="📦 Baú Comunitário"
    )

    if not itens:

        embed.description = (
            "O baú comunitário está vazio."
        )

        return embed

    linhas = []

    for item in itens:

        quantidade = item[
            "quantidade"
        ]

        if quantidade > 1:

            linhas.append(
                (
                    f"• **{item['nome']}** "
                    f"x{quantidade}"
                )
            )

        else:

            linhas.append(
                f"• **{item['nome']}**"
            )

    embed.description = "\n".join(
        linhas
    )[:4000]

    embed.set_footer(
        text=(
            "Itens compartilhados pelo grupo"
        )
    )

    return embed


# =========================================================
# SELECIONAR PERSONAGEM
# =========================================================

class SelecionarPersonagemBauView(
    discord.ui.View
):

    def __init__(
        self,
        user_id,
        personagens,
        acao,
        nome,
        quantidade
    ):
        super().__init__(
            timeout=300
        )

        self.user_id = user_id
        self.acao = acao
        self.nome = nome
        self.quantidade = quantidade

        self.select = discord.ui.Select(
            placeholder="Escolha o personagem",
            min_values=1,
            max_values=1,
            options=[
                discord.SelectOption(
                    label=personagem["nome"],
                    description=(
                        f"{personagem['classe']} "
                        f"• Nível {personagem['nivel']}"
                    ),
                    value=str(
                        personagem["id"]
                    )
                )
                for personagem
                in personagens[:25]
            ]
        )

        self.select.callback = (
            self.escolher
        )

        self.add_item(
            self.select
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

        await executar_transferencia(
            interaction,
            personagem_id,
            self.acao,
            self.nome,
            self.quantidade,
            editar=True
        )


# =========================================================
# TRANSFERÊNCIA
# =========================================================

async def executar_transferencia(
    interaction,
    personagem_id,
    acao,
    nome,
    quantidade,
    editar=False
):
    personagem = buscar_personagem(
        personagem_id
    )

    if personagem is None:

        mensagem = (
            "❌ Personagem não encontrado."
        )

        if editar:

            await interaction.response.edit_message(
                content=mensagem,
                view=None
            )

        else:

            await interaction.response.send_message(
                mensagem,
                ephemeral=True
            )

        return

    try:

        if acao == "guardar":

            resultado = (
                transferir_inventario_para_bau(
                    personagem_id,
                    nome,
                    quantidade
                )
            )

            # Caso tenha guardado uma armadura
            # ou escudo equipado, recalcula a CA.
            ca = recalcular_ca_personagem(
                personagem_id
            )

            mensagem = (
                f"📦 **{resultado['quantidade']}x "
                f"{resultado['nome']}** foi colocado "
                "no baú comunitário.\n\n"
                f"🛡️ CA atual de "
                f"**{personagem['nome']}**: **{ca}**"
            )

        elif acao == "retirar":

            resultado = (
                transferir_bau_para_inventario(
                    personagem_id,
                    nome,
                    quantidade
                )
            )

            mensagem = (
                f"🎒 **{resultado['quantidade']}x "
                f"{resultado['nome']}** foi retirado "
                "do baú e colocado no inventário de "
                f"**{personagem['nome']}**."
            )

        else:

            raise ValueError(
                "Ação inválida."
            )

    except Exception as erro:

        mensagem = (
            f"❌ {erro}"
        )

    if editar:

        await interaction.response.edit_message(
            content=mensagem,
            embed=None,
            view=None
        )

    else:

        await interaction.response.send_message(
            mensagem,
            ephemeral=True
        )


# =========================================================
# COG
# =========================================================

class Bau(
    commands.Cog
):

    def __init__(
        self,
        bot
    ):
        self.bot = bot

    # =====================================================
    # /bau
    # =====================================================

    @app_commands.command(
        name="bau",
        description=(
            "Mostra o baú comunitário do grupo."
        )
    )
    async def bau(
        self,
        interaction: discord.Interaction
    ):
        embed = criar_embed_bau()

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )

    # =====================================================
    # /bau_guardar
    # =====================================================

    @app_commands.command(
        name="bau_guardar",
        description=(
            "Move um item do personagem "
            "para o baú comunitário."
        )
    )
    @app_commands.describe(
        nome="Nome do item",
        quantidade="Quantidade a guardar"
    )
    async def bau_guardar(
        self,
        interaction: discord.Interaction,
        nome: str,
        quantidade: int = 1
    ):
        if quantidade <= 0:

            await interaction.response.send_message(
                (
                    "❌ A quantidade deve ser "
                    "maior que zero."
                ),
                ephemeral=True
            )

            return

        personagens = listar_personagens_jogador(
            interaction.user.id
        )

        if not personagens:

            await interaction.response.send_message(
                "❌ Você não possui nenhuma ficha.",
                ephemeral=True
            )

            return

        if len(personagens) == 1:

            await executar_transferencia(
                interaction,
                personagens[0]["id"],
                "guardar",
                nome,
                quantidade
            )

            return

        view = SelecionarPersonagemBauView(
            interaction.user.id,
            personagens,
            "guardar",
            nome,
            quantidade
        )

        await interaction.response.send_message(
            (
                "📦 Escolha de qual personagem "
                "o item será retirado:"
            ),
            view=view,
            ephemeral=True
        )

    # =====================================================
    # /bau_retirar
    # =====================================================

    @app_commands.command(
        name="bau_retirar",
        description=(
            "Retira um item do baú "
            "para um personagem."
        )
    )
    @app_commands.describe(
        nome="Nome do item",
        quantidade="Quantidade a retirar"
    )
    async def bau_retirar(
        self,
        interaction: discord.Interaction,
        nome: str,
        quantidade: int = 1
    ):
        if quantidade <= 0:

            await interaction.response.send_message(
                (
                    "❌ A quantidade deve ser "
                    "maior que zero."
                ),
                ephemeral=True
            )

            return

        personagens = listar_personagens_jogador(
            interaction.user.id
        )

        if not personagens:

            await interaction.response.send_message(
                "❌ Você não possui nenhuma ficha.",
                ephemeral=True
            )

            return

        if len(personagens) == 1:

            await executar_transferencia(
                interaction,
                personagens[0]["id"],
                "retirar",
                nome,
                quantidade
            )

            return

        view = SelecionarPersonagemBauView(
            interaction.user.id,
            personagens,
            "retirar",
            nome,
            quantidade
        )

        await interaction.response.send_message(
            (
                "🎒 Escolha qual personagem "
                "receberá o item:"
            ),
            view=view,
            ephemeral=True
        )


async def setup(bot):

    await bot.add_cog(
        Bau(bot)
    )