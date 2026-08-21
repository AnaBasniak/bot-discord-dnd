import discord
from discord import app_commands
from discord.ext import commands

from elfo_domestico.services.magia_service import (
    adicionar_magia_personagem,
    buscar_magia,
    buscar_personagem,
    despreparar_magia,
    listar_magias_classe,
    listar_magias_personagem,
    listar_slots,
    magia_pertence_classe,
    preparar_magia,
    remover_magia_personagem,
)

from elfo_domestico.services.regras_magia_service import (
    obter_tipo_conjurador,
    resumo_regras_magia,
    validar_nova_magia_conhecida,
    validar_novo_truque,
    validar_preparar_magia,
)


# =========================================================
# UTIL
# =========================================================

def texto_nivel_magia(
    nivel
):
    if nivel == 0:
        return "Truque"

    return f"{nivel}º nível"


def sim_nao(
    valor
):
    return "Sim" if valor else "Não"


def buscar_magia_do_personagem(
    personagem_id,
    magia_id,
    origem="classe"
):
    magias = listar_magias_personagem(
        personagem_id
    )

    for magia in magias:

        if (
            magia["id"] == magia_id
            and
            magia["origem"] == origem
        ):
            return magia

    return None


# =========================================================
# COG
# =========================================================

class MagiasCog(
    commands.Cog
):

    def __init__(
        self,
        bot
    ):
        self.bot = bot


    # =====================================================
    # /MAGIA
    # =====================================================

    @app_commands.command(
        name="magia",
        description=(
            "Mostra as informações de uma magia."
        )
    )
    @app_commands.describe(
        nome="Nome da magia"
    )
    async def magia(
        self,
        interaction: discord.Interaction,
        nome: str
    ):

        magia = buscar_magia(
            nome
        )

        if magia is None:

            await interaction.response.send_message(
                (
                    "❌ Não encontrei essa magia "
                    "no catálogo."
                ),
                ephemeral=True
            )

            return

        embed = discord.Embed(
            title=f"✨ {magia['nome']}",
            description=(
                magia["descricao"]
                or
                "Descrição ainda não cadastrada."
            )
        )

        embed.add_field(
            name="Nível",
            value=texto_nivel_magia(
                magia["nivel"]
            ),
            inline=True
        )

        embed.add_field(
            name="Escola",
            value=(
                magia["escola"]
                or
                "Não informado"
            ),
            inline=True
        )

        embed.add_field(
            name="Ritual",
            value=sim_nao(
                magia["ritual"]
            ),
            inline=True
        )

        embed.add_field(
            name="Concentração",
            value=sim_nao(
                magia["concentracao"]
            ),
            inline=True
        )

        embed.add_field(
            name="Tempo de Conjuração",
            value=(
                magia["tempo_conjuracao"]
                or
                "Não informado"
            ),
            inline=False
        )

        embed.add_field(
            name="Alcance",
            value=(
                magia["alcance"]
                or
                "Não informado"
            ),
            inline=True
        )

        embed.add_field(
            name="Duração",
            value=(
                magia["duracao"]
                or
                "Não informado"
            ),
            inline=True
        )

        embed.add_field(
            name="Componentes",
            value=(
                magia["componentes"]
                or
                "Não informado"
            ),
            inline=False
        )

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )


    # =====================================================
    # /MAGIAS
    # =====================================================

    @app_commands.command(
        name="magias",
        description=(
            "Mostra as magias de um personagem."
        )
    )
    @app_commands.describe(
        personagem="Nome do personagem"
    )
    async def magias(
        self,
        interaction: discord.Interaction,
        personagem: str
    ):

        ficha = buscar_personagem(
            interaction.user.id,
            personagem
        )

        if ficha is None:

            await interaction.response.send_message(
                (
                    "❌ Não encontrei um personagem "
                    "seu com esse nome."
                ),
                ephemeral=True
            )

            return

        magias = listar_magias_personagem(
            ficha["id"]
        )

        regras = resumo_regras_magia(
            personagem_id=
                ficha["id"],

            classe=
                ficha["classe"],

            nivel=
                ficha["nivel"],
        )

        linhas = []

        for magia in magias:

            marcadores = []

            if magia["preparada"]:
                marcadores.append(
                    "Preparada"
                )

            if magia["origem"] != "classe":
                marcadores.append(
                    magia["origem"]
                )

            extra = ""

            if marcadores:
                extra = (
                    " — "
                    + ", ".join(
                        marcadores
                    )
                )

            linhas.append(
                (
                    f"• **{magia['nome']}** "
                    f"({texto_nivel_magia(magia['nivel'])})"
                    f"{extra}"
                )
            )

        if not linhas:
            linhas = [
                "Nenhuma magia registrada ainda."
            ]

        texto = "\n".join(
            linhas
        )

        if len(texto) > 3800:
            texto = (
                texto[:3800]
                + "\n\n..."
            )

        embed = discord.Embed(
            title=(
                f"📖 Magias de "
                f"{ficha['nome']}"
            ),
            description=texto
        )

        embed.add_field(
            name="Classe",
            value=ficha["classe"],
            inline=True
        )

        embed.add_field(
            name="Nível",
            value=str(
                ficha["nivel"]
            ),
            inline=True
        )

        embed.add_field(
            name="Habilidade",
            value=(
                regras["habilidade"]
                or
                "Nenhuma"
            ).capitalize(),
            inline=True
        )

        embed.add_field(
            name="Truques permitidos",
            value=str(
                regras["truques"]
            ),
            inline=True
        )

        if (
            regras[
                "magias_conhecidas"
            ]
            is not None
        ):

            embed.add_field(
                name="Magias conhecidas",
                value=str(
                    regras[
                        "magias_conhecidas"
                    ]
                ),
                inline=True
            )

        if (
            regras[
                "magias_preparadas"
            ]
            is not None
        ):

            embed.add_field(
                name="Magias preparáveis",
                value=str(
                    regras[
                        "magias_preparadas"
                    ]
                ),
                inline=True
            )

        if (
            regras[
                "grimorio_minimo_mago"
            ]
            is not None
        ):

            embed.add_field(
                name="Magias mínimas no grimório",
                value=str(
                    regras[
                        "grimorio_minimo_mago"
                    ]
                ),
                inline=True
            )

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )


    # =====================================================
    # /SLOTS
    # =====================================================

    @app_commands.command(
        name="slots",
        description=(
            "Mostra os espaços de magia "
            "de um personagem."
        )
    )
    @app_commands.describe(
        personagem="Nome do personagem"
    )
    async def slots(
        self,
        interaction: discord.Interaction,
        personagem: str
    ):

        ficha = buscar_personagem(
            interaction.user.id,
            personagem
        )

        if ficha is None:

            await interaction.response.send_message(
                (
                    "❌ Não encontrei um personagem "
                    "seu com esse nome."
                ),
                ephemeral=True
            )

            return

        slots = listar_slots(
            ficha["id"]
        )

        if not slots:

            await interaction.response.send_message(
                (
                    f"📘 **{ficha['nome']}** "
                    "não possui espaços de magia "
                    "nesse nível."
                ),
                ephemeral=True
            )

            return

        linhas = []

        for slot in slots:

            linhas.append(
                (
                    f"**{slot['nivel']}º nível:** "
                    f"{slot['disponiveis']}/"
                    f"{slot['total']} disponíveis"
                )
            )

        embed = discord.Embed(
            title=(
                f"🔵 Slots de "
                f"{ficha['nome']}"
            ),
            description="\n".join(
                linhas
            )
        )

        embed.add_field(
            name="Classe",
            value=ficha["classe"],
            inline=True
        )

        embed.add_field(
            name="Nível",
            value=str(
                ficha["nivel"]
            ),
            inline=True
        )

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )


    # =====================================================
    # /MAGIAS_CLASSE
    # =====================================================

    @app_commands.command(
        name="magias_classe",
        description=(
            "Lista as magias disponíveis "
            "para uma classe."
        )
    )
    @app_commands.describe(
        classe="Nome da classe",
        nivel_magia=(
            "Nível da magia. "
            "Use 0 para truques."
        )
    )
    async def magias_classe(
        self,
        interaction: discord.Interaction,
        classe: str,
        nivel_magia: int
    ):

        if (
            nivel_magia < 0
            or
            nivel_magia > 9
        ):

            await interaction.response.send_message(
                (
                    "❌ O nível da magia deve "
                    "estar entre 0 e 9."
                ),
                ephemeral=True
            )

            return

        magias = listar_magias_classe(
            classe,
            nivel_magia
        )

        if not magias:

            await interaction.response.send_message(
                (
                    "❌ Não encontrei magias "
                    "para essa classe e nível."
                ),
                ephemeral=True
            )

            return

        linhas = [
            (
                f"• **{magia['nome']}**"
                + (
                    " *(ritual)*"
                    if magia["ritual"]
                    else ""
                )
            )
            for magia in magias
        ]

        texto = "\n".join(
            linhas
        )

        if len(texto) > 3800:
            texto = (
                texto[:3800]
                + "\n\n..."
            )

        embed = discord.Embed(
            title=(
                f"📚 {classe} — "
                f"{texto_nivel_magia(nivel_magia)}"
            ),
            description=texto
        )

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )


    # =====================================================
    # /APRENDER_MAGIA
    # =====================================================

    @app_commands.command(
        name="aprender_magia",
        description=(
            "Adiciona uma magia conhecida "
            "ou uma magia ao grimório."
        )
    )
    @app_commands.describe(
        personagem="Nome do personagem",
        magia="Nome da magia"
    )
    async def aprender_magia(
        self,
        interaction: discord.Interaction,
        personagem: str,
        magia: str
    ):

        ficha = buscar_personagem(
            interaction.user.id,
            personagem
        )

        if ficha is None:

            await interaction.response.send_message(
                "❌ Personagem não encontrado.",
                ephemeral=True
            )

            return

        dados_magia = buscar_magia(
            magia
        )

        if dados_magia is None:

            await interaction.response.send_message(
                "❌ Magia não encontrada no catálogo.",
                ephemeral=True
            )

            return

        pertence = magia_pertence_classe(
            dados_magia["id"],
            ficha["classe"]
        )

        if not pertence:

            await interaction.response.send_message(
                (
                    f"❌ **{dados_magia['nome']}** "
                    f"não pertence à lista normal "
                    f"de magias de **{ficha['classe']}**."
                ),
                ephemeral=True
            )

            return

        existente = buscar_magia_do_personagem(
            ficha["id"],
            dados_magia["id"],
            "classe"
        )

        if existente is not None:

            await interaction.response.send_message(
                (
                    f"📖 **{ficha['nome']}** já possui "
                    f"**{dados_magia['nome']}**."
                ),
                ephemeral=True
            )

            return

        # ================================================
        # TRUQUE
        # ================================================

        if dados_magia["nivel"] == 0:

            validacao = validar_novo_truque(
                personagem_id=
                    ficha["id"],

                classe=
                    ficha["classe"],

                nivel=
                    ficha["nivel"],
            )

        # ================================================
        # MAGIA DE NÍVEL 1+
        # ================================================

        else:

            validacao = validar_nova_magia_conhecida(
                personagem_id=
                    ficha["id"],

                classe=
                    ficha["classe"],

                nivel_personagem=
                    ficha["nivel"],

                nivel_magia=
                    dados_magia["nivel"],
            )

        if not validacao["permitido"]:

            await interaction.response.send_message(
                (
                    "❌ "
                    + validacao["motivo"]
                ),
                ephemeral=True
            )

            return

        adicionar_magia_personagem(
            personagem_id=
                ficha["id"],

            magia_id=
                dados_magia["id"],

            preparada=False,

            origem="classe",
        )

        if ficha["classe"] == "Mago":

            mensagem = (
                f"📕 **{dados_magia['nome']}** foi "
                f"adicionada ao grimório de "
                f"**{ficha['nome']}**."
            )

        else:

            mensagem = (
                f"✨ **{ficha['nome']}** aprendeu "
                f"**{dados_magia['nome']}**."
            )

        await interaction.response.send_message(
            mensagem,
            ephemeral=True
        )


    # =====================================================
    # /REMOVER_MAGIA
    # =====================================================

    @app_commands.command(
        name="remover_magia",
        description=(
            "Remove uma magia conhecida "
            "do personagem."
        )
    )
    @app_commands.describe(
        personagem="Nome do personagem",
        magia="Nome da magia"
    )
    async def remover_magia(
        self,
        interaction: discord.Interaction,
        personagem: str,
        magia: str
    ):

        ficha = buscar_personagem(
            interaction.user.id,
            personagem
        )

        if ficha is None:

            await interaction.response.send_message(
                "❌ Personagem não encontrado.",
                ephemeral=True
            )

            return

        dados_magia = buscar_magia(
            magia
        )

        if dados_magia is None:

            await interaction.response.send_message(
                "❌ Magia não encontrada.",
                ephemeral=True
            )

            return

        existente = buscar_magia_do_personagem(
            ficha["id"],
            dados_magia["id"],
            "classe"
        )

        if existente is None:

            await interaction.response.send_message(
                (
                    f"❌ **{ficha['nome']}** não possui "
                    f"essa magia como magia de classe."
                ),
                ephemeral=True
            )

            return

        tipo = obter_tipo_conjurador(
            ficha["classe"]
        )

        # Truques não são substituídos normalmente
        # pela regra básica de 2014.

        if dados_magia["nivel"] == 0:

            await interaction.response.send_message(
                (
                    "❌ Truques não são removidos "
                    "por este comando."
                ),
                ephemeral=True
            )

            return

        # Classes preparadoras simplesmente
        # preparam/despreparam magias.

        if tipo == "preparadas":

            await interaction.response.send_message(
                (
                    "❌ Essa classe prepara magias. "
                    "Use `/despreparar_magia`."
                ),
                ephemeral=True
            )

            return

        # O Mago não esquece normalmente uma magia
        # já registrada no grimório.

        if tipo == "grimorio":

            await interaction.response.send_message(
                (
                    "❌ Magias do grimório não são "
                    "removidas normalmente."
                ),
                ephemeral=True
            )

            return

        removida = remover_magia_personagem(
            personagem_id=
                ficha["id"],

            magia_id=
                dados_magia["id"],

            origem="classe",
        )

        if not removida:

            await interaction.response.send_message(
                "❌ Não foi possível remover a magia.",
                ephemeral=True
            )

            return

        await interaction.response.send_message(
            (
                f"📖 **{dados_magia['nome']}** foi "
                f"removida das magias conhecidas "
                f"de **{ficha['nome']}**."
            ),
            ephemeral=True
        )


    # =====================================================
    # /PREPARAR_MAGIA
    # =====================================================

    @app_commands.command(
        name="preparar_magia",
        description=(
            "Prepara uma magia para o personagem."
        )
    )
    @app_commands.describe(
        personagem="Nome do personagem",
        magia="Nome da magia"
    )
    async def preparar_magia_comando(
        self,
        interaction: discord.Interaction,
        personagem: str,
        magia: str
    ):

        ficha = buscar_personagem(
            interaction.user.id,
            personagem
        )

        if ficha is None:

            await interaction.response.send_message(
                "❌ Personagem não encontrado.",
                ephemeral=True
            )

            return

        dados_magia = buscar_magia(
            magia
        )

        if dados_magia is None:

            await interaction.response.send_message(
                "❌ Magia não encontrada.",
                ephemeral=True
            )

            return

        tipo = obter_tipo_conjurador(
            ficha["classe"]
        )

        if tipo not in (
            "preparadas",
            "grimorio",
        ):

            await interaction.response.send_message(
                (
                    f"❌ **{ficha['classe']}** não utiliza "
                    "o sistema de preparação de magias."
                ),
                ephemeral=True
            )

            return

        if dados_magia["nivel"] == 0:

            await interaction.response.send_message(
                "❌ Truques não precisam ser preparados.",
                ephemeral=True
            )

            return

        pertence = magia_pertence_classe(
            dados_magia["id"],
            ficha["classe"]
        )

        if not pertence:

            await interaction.response.send_message(
                (
                    f"❌ **{dados_magia['nome']}** "
                    f"não pertence à lista normal "
                    f"de **{ficha['classe']}**."
                ),
                ephemeral=True
            )

            return

        existente = buscar_magia_do_personagem(
            ficha["id"],
            dados_magia["id"],
            "classe"
        )

        if (
            existente is not None
            and
            existente["preparada"]
        ):

            await interaction.response.send_message(
                (
                    f"✅ **{dados_magia['nome']}** "
                    "já está preparada."
                ),
                ephemeral=True
            )

            return

        # Mago só prepara magias que já estão
        # registradas no grimório.

        if (
            ficha["classe"] == "Mago"
            and
            existente is None
        ):

            await interaction.response.send_message(
                (
                    "❌ Essa magia ainda não está "
                    "no grimório.\n\n"
                    "Use `/aprender_magia` primeiro."
                ),
                ephemeral=True
            )

            return

        validacao = validar_preparar_magia(
            personagem_id=
                ficha["id"],

            classe=
                ficha["classe"],

            nivel_personagem=
                ficha["nivel"],

            nivel_magia=
                dados_magia["nivel"],
        )

        if not validacao["permitido"]:

            await interaction.response.send_message(
                (
                    "❌ "
                    + validacao["motivo"]
                ),
                ephemeral=True
            )

            return

        # Clérigo, Druida e Paladino:
        # a entrada representa a magia atualmente preparada.

        if existente is None:

            adicionar_magia_personagem(
                personagem_id=
                    ficha["id"],

                magia_id=
                    dados_magia["id"],

                preparada=True,

                origem="classe",
            )

        # Mago:
        # a magia já existe no grimório,
        # então apenas marca como preparada.

        else:

            preparar_magia(
                personagem_id=
                    ficha["id"],

                magia_id=
                    dados_magia["id"],
            )

        await interaction.response.send_message(
            (
                f"✨ **{dados_magia['nome']}** foi "
                f"preparada por **{ficha['nome']}**."
            ),
            ephemeral=True
        )


    # =====================================================
    # /DESPREPARAR_MAGIA
    # =====================================================

    @app_commands.command(
        name="despreparar_magia",
        description=(
            "Remove uma magia da lista preparada."
        )
    )
    @app_commands.describe(
        personagem="Nome do personagem",
        magia="Nome da magia"
    )
    async def despreparar_magia_comando(
        self,
        interaction: discord.Interaction,
        personagem: str,
        magia: str
    ):

        ficha = buscar_personagem(
            interaction.user.id,
            personagem
        )

        if ficha is None:

            await interaction.response.send_message(
                "❌ Personagem não encontrado.",
                ephemeral=True
            )

            return

        dados_magia = buscar_magia(
            magia
        )

        if dados_magia is None:

            await interaction.response.send_message(
                "❌ Magia não encontrada.",
                ephemeral=True
            )

            return

        tipo = obter_tipo_conjurador(
            ficha["classe"]
        )

        if tipo not in (
            "preparadas",
            "grimorio",
        ):

            await interaction.response.send_message(
                (
                    f"❌ **{ficha['classe']}** não utiliza "
                    "preparação de magias."
                ),
                ephemeral=True
            )

            return

        existente = buscar_magia_do_personagem(
            ficha["id"],
            dados_magia["id"],
            "classe"
        )

        if (
            existente is None
            or
            not existente["preparada"]
        ):

            await interaction.response.send_message(
                "❌ Essa magia não está preparada.",
                ephemeral=True
            )

            return

        # Mago precisa manter a magia no grimório.
        # Apenas retiramos da lista preparada.

        if ficha["classe"] == "Mago":

            alterada = despreparar_magia(
                personagem_id=
                    ficha["id"],

                magia_id=
                    dados_magia["id"],
            )

        # Clérigo, Druida e Paladino não possuem
        # uma lista individual de magias conhecidas.
        # A entrada existe apenas enquanto preparada.

        else:

            alterada = remover_magia_personagem(
                personagem_id=
                    ficha["id"],

                magia_id=
                    dados_magia["id"],

                origem="classe",
            )

        if not alterada:

            await interaction.response.send_message(
                (
                    "❌ Não foi possível "
                    "despreparar essa magia."
                ),
                ephemeral=True
            )

            return

        await interaction.response.send_message(
            (
                f"📕 **{dados_magia['nome']}** não está "
                f"mais preparada por "
                f"**{ficha['nome']}**."
            ),
            ephemeral=True
        )


# =========================================================
# SETUP
# =========================================================

async def setup(
    bot
):

    await bot.add_cog(
        MagiasCog(
            bot
        )
    )