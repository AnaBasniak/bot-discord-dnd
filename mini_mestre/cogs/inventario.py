import discord
from discord import app_commands
from discord.ext import commands

from mini_mestre.services.ficha_service import (
    adicionar_item_inventario,
    alterar_equipado,
    buscar_inventario_personagem,
    buscar_personagem,
    listar_personagens_jogador,
    recalcular_ca_personagem,
    remover_item_inventario,
)


# =========================================================
# SELETOR DE PERSONAGEM
# =========================================================

class SelecionarPersonagemInventario(
    discord.ui.View
):

    def __init__(
        self,
        user_id,
        personagens,
        acao,
        dados=None
    ):
        super().__init__(
            timeout=300
        )

        self.user_id = user_id
        self.acao = acao
        self.dados = dados or {}

        self.select = discord.ui.Select(
            placeholder="Escolha o personagem",
            options=[
                discord.SelectOption(
                    label=item["nome"],
                    description=(
                        f"{item['classe']} "
                        f"• Nível {item['nivel']}"
                    ),
                    value=str(
                        item["id"]
                    )
                )
                for item in personagens[:25]
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
                "❌ Esse menu pertence a outro jogador.",
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

        await executar_acao(
            interaction,
            personagem_id,
            self.acao,
            self.dados,
            editar=True
        )


# =========================================================
# MOSTRAR INVENTÁRIO
# =========================================================

def criar_embed_inventario(
    personagem,
    itens
):
    embed = discord.Embed(
        title=(
            f"🎒 Inventário de "
            f"{personagem['nome']}"
        )
    )

    if not itens:

        embed.description = (
            "O inventário está vazio."
        )

        return embed

    linhas = []

    for item in itens:

        texto = (
            f"• **{item['nome']}**"
        )

        if item["quantidade"] > 1:
            texto += (
                f" x{item['quantidade']}"
            )

        if item["equipado"]:
            texto += " ✅ Equipado"

        linhas.append(
            texto
        )

    embed.description = "\n".join(
        linhas
    )[:4000]

    return embed


# =========================================================
# EXECUTAR AÇÕES
# =========================================================

async def executar_acao(
    interaction,
    personagem_id,
    acao,
    dados,
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

        if acao == "ver":

            itens = buscar_inventario_personagem(
                personagem_id
            )

            embed = criar_embed_inventario(
                personagem,
                itens
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

            return

        if acao == "adicionar":

            adicionar_item_inventario(
                personagem_id,
                dados["nome"],
                dados["quantidade"]
            )

            mensagem = (
                f"✅ **{dados['quantidade']}x "
                f"{dados['nome']}** "
                "adicionado ao inventário."
            )

        elif acao == "remover":

            remover_item_inventario(
                personagem_id,
                dados["nome"],
                dados["quantidade"]
            )

            mensagem = (
                f"✅ Item removido: "
                f"**{dados['nome']}**."
            )

        elif acao == "equipar":

            alterar_equipado(
                personagem_id,
                dados["nome"],
                True
            )

            ca = recalcular_ca_personagem(
                personagem_id
            )

            mensagem = (
                f"✅ **{dados['nome']}** equipado.\n"
                f"🛡️ CA atual: **{ca}**"
            )

        elif acao == "desequipar":

            alterar_equipado(
                personagem_id,
                dados["nome"],
                False
            )

            ca = recalcular_ca_personagem(
                personagem_id
            )

            mensagem = (
                f"✅ **{dados['nome']}** desequipado.\n"
                f"🛡️ CA atual: **{ca}**"
            )

        else:

            raise ValueError(
                "Ação de inventário inválida."
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

class Inventario(
    commands.Cog
):

    def __init__(
        self,
        bot
    ):
        self.bot = bot

    async def escolher_ou_executar(
        self,
        interaction,
        acao,
        dados=None
    ):
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

            await executar_acao(
                interaction,
                personagens[0]["id"],
                acao,
                dados or {}
            )

            return

        view = SelecionarPersonagemInventario(
            interaction.user.id,
            personagens,
            acao,
            dados
        )

        await interaction.response.send_message(
            "Escolha o personagem:",
            view=view,
            ephemeral=True
        )

    # =====================================================
    # /inventario
    # =====================================================

    @app_commands.command(
        name="inventario",
        description="Mostra o inventário do personagem."
    )
    async def inventario(
        self,
        interaction: discord.Interaction
    ):
        await self.escolher_ou_executar(
            interaction,
            "ver"
        )

    # =====================================================
    # /item_adicionar
    # =====================================================

    @app_commands.command(
        name="item_adicionar",
        description="Adiciona um item ao inventário."
    )
    @app_commands.describe(
        nome="Nome do item",
        quantidade="Quantidade"
    )
    async def item_adicionar(
        self,
        interaction: discord.Interaction,
        nome: str,
        quantidade: int = 1
    ):
        await self.escolher_ou_executar(
            interaction,
            "adicionar",
            {
                "nome": nome,
                "quantidade": quantidade,
            }
        )

    # =====================================================
    # /item_remover
    # =====================================================

    @app_commands.command(
        name="item_remover",
        description="Remove um item do inventário."
    )
    @app_commands.describe(
        nome="Nome do item",
        quantidade="Quantidade"
    )
    async def item_remover(
        self,
        interaction: discord.Interaction,
        nome: str,
        quantidade: int = 1
    ):
        await self.escolher_ou_executar(
            interaction,
            "remover",
            {
                "nome": nome,
                "quantidade": quantidade,
            }
        )

    # =====================================================
    # /equipar
    # =====================================================

    @app_commands.command(
        name="equipar",
        description="Equipa um item do inventário."
    )
    @app_commands.describe(
        nome="Nome do item"
    )
    async def equipar(
        self,
        interaction: discord.Interaction,
        nome: str
    ):
        await self.escolher_ou_executar(
            interaction,
            "equipar",
            {
                "nome": nome,
            }
        )

    # =====================================================
    # /desequipar
    # =====================================================

    @app_commands.command(
        name="desequipar",
        description="Desequipa um item."
    )
    @app_commands.describe(
        nome="Nome do item"
    )
    async def desequipar(
        self,
        interaction: discord.Interaction,
        nome: str
    ):
        await self.escolher_ou_executar(
            interaction,
            "desequipar",
            {
                "nome": nome,
            }
        )


async def setup(bot):

    await bot.add_cog(
        Inventario(bot)
    )