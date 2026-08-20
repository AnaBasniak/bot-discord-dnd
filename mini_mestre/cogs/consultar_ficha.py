import discord
from discord import app_commands
from discord.ext import commands

from mini_mestre.services.ficha_service import (
    buscar_atributos_personagem,
    buscar_inventario_personagem,
    buscar_pericias_personagem,
    buscar_personagem,
    buscar_proficiencias_personagem,
    buscar_salvaguardas_personagem,
    calcular_modificador,
    listar_personagens_jogador,
    pode_acessar_personagem,
)


NOMES_ATRIBUTOS = {
    "forca": "Força",
    "destreza": "Destreza",
    "constituicao": "Constituição",
    "inteligencia": "Inteligência",
    "sabedoria": "Sabedoria",
    "carisma": "Carisma",
}


NOMES_PERICIAS = {
    "acrobacia": "Acrobacia",
    "arcanismo": "Arcanismo",
    "atletismo": "Atletismo",
    "atuacao": "Atuação",
    "enganacao": "Enganação",
    "furtividade": "Furtividade",
    "historia": "História",
    "intimidacao": "Intimidação",
    "intuicao": "Intuição",
    "investigacao": "Investigação",
    "lidar_animais": "Lidar com Animais",
    "medicina": "Medicina",
    "natureza": "Natureza",
    "percepcao": "Percepção",
    "persuasao": "Persuasão",
    "prestidigitacao": "Prestidigitação",
    "religiao": "Religião",
    "sobrevivencia": "Sobrevivência",
}


def criar_embed_ficha(personagem_id):
    personagem = buscar_personagem(
        personagem_id
    )

    if personagem is None:
        return None

    atributos = buscar_atributos_personagem(
        personagem_id
    )

    pericias = buscar_pericias_personagem(
        personagem_id
    )

    salvaguardas = buscar_salvaguardas_personagem(
        personagem_id
    )

    proficiencias = buscar_proficiencias_personagem(
        personagem_id
    )

    inventario = buscar_inventario_personagem(
        personagem_id
    )

    embed = discord.Embed(
        title=f"📜 {personagem['nome']}",
        description=(
            f"Ficha #{personagem['id']}"
        )
    )

    raca = personagem["raca"]

    if personagem["subraca"]:
        raca += (
            f" ({personagem['subraca']})"
        )

    classe = personagem["classe"]

    if personagem["subclasse"]:
        classe += (
            f" — {personagem['subclasse']}"
        )

    embed.add_field(
        name="🧬 Raça",
        value=raca,
        inline=True
    )

    embed.add_field(
        name="⚔️ Classe",
        value=(
            f"{classe}\n"
            f"Nível {personagem['nivel']}"
        ),
        inline=True
    )

    embed.add_field(
        name="📖 Antecedente",
        value=(
            personagem["antecedente"]
            or "—"
        ),
        inline=True
    )

    embed.add_field(
        name="❤️ Pontos de Vida",
        value=(
            f"{personagem['pv_atual']}"
            f"/"
            f"{personagem['pv_maximo']}"
        ),
        inline=True
    )

    embed.add_field(
        name="🛡️ CA",
        value=str(
            personagem["ca"]
        ),
        inline=True
    )

    iniciativa = personagem[
        "iniciativa"
    ]

    sinal = (
        "+"
        if iniciativa >= 0
        else ""
    )

    embed.add_field(
        name="⚡ Iniciativa",
        value=(
            f"{sinal}{iniciativa}"
        ),
        inline=True
    )

    embed.add_field(
        name="👣 Deslocamento",
        value=(
            f"{personagem['deslocamento']} pés"
        ),
        inline=True
    )

    if atributos:
        linhas = []

        for atributo, nome in NOMES_ATRIBUTOS.items():
            valor = atributos[
                atributo
            ]

            modificador = calcular_modificador(
                valor
            )

            sinal = (
                "+"
                if modificador >= 0
                else ""
            )

            linhas.append(
                (
                    f"**{nome}:** "
                    f"{valor} "
                    f"({sinal}{modificador})"
                )
            )

        embed.add_field(
            name="🎲 Atributos",
            value="\n".join(
                linhas
            ),
            inline=False
        )

    if pericias:
        nomes = [
            NOMES_PERICIAS.get(
                pericia,
                pericia
            )
            for pericia in pericias
        ]

        embed.add_field(
            name="🎯 Perícias proficientes",
            value=", ".join(
                nomes
            ),
            inline=False
        )

    if salvaguardas:
        nomes = [
            NOMES_ATRIBUTOS.get(
                atributo,
                atributo
            )
            for atributo in salvaguardas
        ]

        embed.add_field(
            name="🛡️ Salvaguardas proficientes",
            value=", ".join(
                nomes
            ),
            inline=False
        )

    if proficiencias:
        texto = "\n".join(
            (
                f"• {item['tipo']}: "
                f"{item['nome']}"
            )
            for item in proficiencias
        )

        embed.add_field(
            name="📚 Proficiências",
            value=texto[:1024],
            inline=False
        )

    if inventario:
        linhas = []

        for item in inventario:
            texto = (
                f"• {item['nome']}"
            )

            if item["quantidade"] > 1:
                texto += (
                    f" x{item['quantidade']}"
                )

            if item["equipado"]:
                texto += " ✅"

            linhas.append(
                texto
            )

        embed.add_field(
            name="🎒 Inventário",
            value="\n".join(
                linhas
            )[:1024],
            inline=False
        )

    embed.set_footer(
        text=(
            "Mini Mestre • D&D 5e 2014"
        )
    )

    return embed


class SelecionarFichaView(
    discord.ui.View
):

    def __init__(
        self,
        user_id,
        personagens
    ):
        super().__init__(
            timeout=300
        )

        self.user_id = user_id

        select = discord.ui.Select(
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
                for personagem in personagens[:25]
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

        if not pode_acessar_personagem(
            interaction.user.id,
            personagem_id
        ):
            await interaction.response.send_message(
                "❌ Você não pode acessar essa ficha.",
                ephemeral=True
            )

            return

        embed = criar_embed_ficha(
            personagem_id
        )

        if embed is None:
            await interaction.response.send_message(
                "❌ Ficha não encontrada.",
                ephemeral=True
            )

            return

        await interaction.response.edit_message(
            content=None,
            embed=embed,
            view=None
        )


class ConsultarFicha(
    commands.Cog
):

    def __init__(
        self,
        bot
    ):
        self.bot = bot

    @app_commands.command(
        name="ficha",
        description="Mostra sua ficha de personagem."
    )
    async def ficha(
        self,
        interaction: discord.Interaction
    ):
        personagens = listar_personagens_jogador(
            interaction.user.id
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

            embed = criar_embed_ficha(
                personagem["id"]
            )

            await interaction.response.send_message(
                embed=embed,
                ephemeral=True
            )

            return

        view = SelecionarFichaView(
            interaction.user.id,
            personagens
        )

        await interaction.response.send_message(
            (
                "📜 Você possui mais de uma ficha.\n\n"
                "Escolha qual deseja visualizar:"
            ),
            view=view,
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(
        ConsultarFicha(bot)
    )