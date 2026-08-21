import random
from collections import Counter

import discord
from discord import app_commands
from discord.ext import commands

from mini_mestre.services.ficha_service import (
    calcular_ca_personagem,
    calcular_modificador,
    criar_personagem,
    garantir_jogador,
    listar_antecedentes,
    listar_bonus_atributos_raciais,
    listar_classes,
    listar_equipamentos_categoria,
    listar_escolhas_equipamento_classe,
    listar_escolhas_raciais,
    listar_pericias_antecedente,
    listar_pericias_classe,
    listar_proficiencias_antecedente,
    listar_proficiencias_classe,
    listar_racas,
    listar_salvaguardas_classe,
    listar_subclasses,
    listar_truques_mago,
    listar_subracas,
    salvar_inventario,
    inicializar_sistema_magico_personagem,
)


# =========================================================
# NOMES BONITOS
# =========================================================

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


TODOS_ATRIBUTOS = list(
    NOMES_ATRIBUTOS.keys()
)

TODAS_PERICIAS = list(
    NOMES_PERICIAS.keys()
)


# =========================================================
# PERÍCIAS RACIAIS FIXAS
# =========================================================
#
# Algumas raças recebem perícia automaticamente.
# Meio-Elfo é tratado pelas escolhas raciais.
# =========================================================

PERICIAS_RACIAIS_FIXAS = {
    "Elfo": [
        "percepcao",
    ],

    "Meio-Orc": [
        "intimidacao",
    ],
}


# =========================================================
# FUNÇÕES AUXILIARES DE INTERAÇÃO
# =========================================================

async def mostrar_etapa(
    interaction,
    texto,
    view=None
):
    """
    Mostra a próxima etapa.

    Se a interação veio de uma mensagem com View,
    edita essa mensagem.

    Se veio de Modal, envia uma nova resposta.
    """

    if interaction.response.is_done():

        await interaction.followup.send(
            texto,
            view=view,
            ephemeral=True
        )

        return

    if interaction.message is not None:

        await interaction.response.edit_message(
            content=texto,
            embed=None,
            view=view
        )

        return

    await interaction.response.send_message(
        texto,
        view=view,
        ephemeral=True
    )


async def mostrar_erro(
    interaction,
    texto
):
    if interaction.response.is_done():

        await interaction.followup.send(
            f"❌ {texto}",
            ephemeral=True
        )

    else:

        await interaction.response.send_message(
            f"❌ {texto}",
            ephemeral=True
        )


# =========================================================
# VIEW BASE
# =========================================================

class ViewDaFicha(
    discord.ui.View
):

    def __init__(
        self,
        user_id,
        estado
    ):
        super().__init__(
            timeout=900
        )

        self.user_id = user_id
        self.estado = estado

    async def interaction_check(
        self,
        interaction
    ):
        if (
            interaction.user.id
            != self.user_id
        ):

            await interaction.response.send_message(
                (
                    "❌ Essa criação de ficha "
                    "pertence a outro jogador."
                ),
                ephemeral=True
            )

            return False

        return True


# =========================================================
# MODAL - NOME DO PERSONAGEM
# =========================================================

class NomePersonagemModal(
    discord.ui.Modal,
    title="Criar personagem"
):

    nome = discord.ui.TextInput(
        label="Nome do personagem",
        placeholder="Ex.: Citrino",
        min_length=1,
        max_length=80,
        required=True
    )

    async def on_submit(
        self,
        interaction
    ):
        nome = str(
            self.nome.value
        ).strip()

        estado = {
            "nome": nome,

            "raca": None,
            "subraca": None,

            "classe": None,
            "subclasse": None,

            "antecedente": None,

            "pericias_raciais": [],
            "pericias_classe": [],
            "pericias_antecedente": [],
            "proficiencias_raciais": [],

            "rolagens": [],

            "atributos_base": {},
            "atributos_finais": {},

            "escolhas_atributos_raciais": [],

            "truque_alto_elfo": None,

            "equipamentos_escolhidos": [],

            "escolhas_equipamento": [],
            "indice_equipamento": 0,

            "categorias_pendentes": [],
            "indice_categoria": 0,
        }

        racas = listar_racas()

        if not racas:

            await mostrar_erro(
                interaction,
                "Nenhuma raça foi encontrada no banco."
            )

            return

        view = EscolhaRacaView(
            interaction.user.id,
            estado,
            racas
        )

        await mostrar_etapa(
            interaction,
            (
                f"📜 Vamos criar **{nome}**!\n\n"
                "Primeiro, escolha a raça:"
            ),
            view
        )


# =========================================================
# RAÇA
# =========================================================

class EscolhaRacaView(
    ViewDaFicha
):

    def __init__(
        self,
        user_id,
        estado,
        racas
    ):
        super().__init__(
            user_id,
            estado
        )

        self.racas = racas

        self.select = discord.ui.Select(
            placeholder="Escolha a raça",
            min_values=1,
            max_values=1,
            options=[
                discord.SelectOption(
                    label=raca["nome"],
                    value=str(
                        raca["id"]
                    )
                )
                for raca in racas
            ]
        )

        self.select.callback = (
            self.escolher
        )

        self.add_item(
            self.select
        )

    async def escolher(
        self,
        interaction
    ):
        raca_id = int(
            self.select.values[0]
        )

        raca = next(
            item
            for item in self.racas
            if item["id"] == raca_id
        )

        self.estado[
            "raca"
        ] = raca

        # Perícias raciais automáticas.
        self.estado[
            "pericias_raciais"
        ] = list(
            PERICIAS_RACIAIS_FIXAS.get(
                raca["nome"],
                []
            )
        )

        subracas = listar_subracas(
            raca_id
        )

        if subracas:

            view = EscolhaSubracaView(
                self.user_id,
                self.estado,
                subracas
            )

            await mostrar_etapa(
                interaction,
                (
                    f"✅ Raça: **{raca['nome']}**\n\n"
                    "Agora escolha a sub-raça:"
                ),
                view
            )

            return

        await mostrar_classes(
            interaction,
            self.user_id,
            self.estado
        )


# =========================================================
# SUB-RAÇA
# =========================================================

class EscolhaSubracaView(
    ViewDaFicha
):

    def __init__(
        self,
        user_id,
        estado,
        subracas
    ):
        super().__init__(
            user_id,
            estado
        )

        self.subracas = subracas

        self.select = discord.ui.Select(
            placeholder="Escolha a sub-raça",
            min_values=1,
            max_values=1,
            options=[
                discord.SelectOption(
                    label=item["nome"],
                    value=str(
                        item["id"]
                    )
                )
                for item in subracas
            ]
        )

        self.select.callback = (
            self.escolher
        )

        self.add_item(
            self.select
        )

    async def escolher(
        self,
        interaction
    ):
        subraca_id = int(
            self.select.values[0]
        )

        subraca = next(
            item
            for item in self.subracas
            if item["id"] == subraca_id
        )

        self.estado[
            "subraca"
        ] = subraca

        await mostrar_classes(
            interaction,
            self.user_id,
            self.estado
        )


# =========================================================
# CLASSE
# =========================================================

async def mostrar_classes(
    interaction,
    user_id,
    estado
):
    classes = listar_classes()

    if not classes:

        await mostrar_erro(
            interaction,
            "Nenhuma classe foi encontrada no banco."
        )

        return

    view = EscolhaClasseView(
        user_id,
        estado,
        classes
    )

    await mostrar_etapa(
        interaction,
        (
            "✅ Raça definida.\n\n"
            "Agora escolha sua classe:"
        ),
        view
    )


class EscolhaClasseView(
    ViewDaFicha
):

    def __init__(
        self,
        user_id,
        estado,
        classes
    ):
        super().__init__(
            user_id,
            estado
        )

        self.classes = classes

        self.select = discord.ui.Select(
            placeholder="Escolha a classe",
            min_values=1,
            max_values=1,
            options=[
                discord.SelectOption(
                    label=classe["nome"],
                    value=str(
                        classe["id"]
                    ),
                    description=(
                        f"Dado de Vida: "
                        f"d{classe['dado_vida']}"
                    )
                )
                for classe in classes
            ]
        )

        self.select.callback = (
            self.escolher
        )

        self.add_item(
            self.select
        )

    async def escolher(
        self,
        interaction
    ):
        classe_id = int(
            self.select.values[0]
        )

        classe = next(
            item
            for item in self.classes
            if item["id"] == classe_id
        )

        self.estado[
            "classe"
        ] = classe

        subclasses = listar_subclasses(
            classe_id
        )

        subclasses_nivel_1 = [
            item
            for item in subclasses
            if (
                item["nivel_escolha"]
                == 1
            )
        ]

        if subclasses_nivel_1:

            view = EscolhaSubclasseView(
                self.user_id,
                self.estado,
                subclasses_nivel_1
            )

            await mostrar_etapa(
                interaction,
                (
                    f"✅ Classe: **{classe['nome']}**\n\n"
                    "Essa classe escolhe sua "
                    "subclasse no nível 1:"
                ),
                view
            )

            return

        await mostrar_antecedentes(
            interaction,
            self.user_id,
            self.estado
        )


# =========================================================
# SUBCLASSE NÍVEL 1
# =========================================================

class EscolhaSubclasseView(
    ViewDaFicha
):

    def __init__(
        self,
        user_id,
        estado,
        subclasses
    ):
        super().__init__(
            user_id,
            estado
        )

        self.subclasses = subclasses

        self.select = discord.ui.Select(
            placeholder="Escolha a subclasse",
            min_values=1,
            max_values=1,
            options=[
                discord.SelectOption(
                    label=item["nome"],
                    value=str(
                        item["id"]
                    )
                )
                for item in subclasses
            ]
        )

        self.select.callback = (
            self.escolher
        )

        self.add_item(
            self.select
        )

    async def escolher(
        self,
        interaction
    ):
        subclasse_id = int(
            self.select.values[0]
        )

        subclasse = next(
            item
            for item in self.subclasses
            if item["id"] == subclasse_id
        )

        self.estado[
            "subclasse"
        ] = subclasse

        await mostrar_antecedentes(
            interaction,
            self.user_id,
            self.estado
        )


# =========================================================
# ANTECEDENTE
# =========================================================

async def mostrar_antecedentes(
    interaction,
    user_id,
    estado
):
    antecedentes = listar_antecedentes()

    if not antecedentes:

        await mostrar_erro(
            interaction,
            "Nenhum antecedente foi encontrado."
        )

        return

    view = EscolhaAntecedenteView(
        user_id,
        estado,
        antecedentes
    )

    await mostrar_etapa(
        interaction,
        (
            "✅ Classe definida.\n\n"
            "Agora escolha o antecedente:"
        ),
        view
    )


class EscolhaAntecedenteView(
    ViewDaFicha
):

    def __init__(
        self,
        user_id,
        estado,
        antecedentes
    ):
        super().__init__(
            user_id,
            estado
        )

        self.antecedentes = antecedentes

        self.select = discord.ui.Select(
            placeholder="Escolha o antecedente",
            min_values=1,
            max_values=1,
            options=[
                discord.SelectOption(
                    label=item["nome"],
                    value=str(
                        item["id"]
                    )
                )
                for item in antecedentes
            ]
        )

        self.select.callback = (
            self.escolher
        )

        self.add_item(
            self.select
        )

    async def escolher(
        self,
        interaction
    ):
        antecedente_id = int(
            self.select.values[0]
        )

        antecedente = next(
            item
            for item in self.antecedentes
            if item["id"] == antecedente_id
        )

        self.estado[
            "antecedente"
        ] = antecedente

        self.estado[
            "pericias_antecedente"
        ] = listar_pericias_antecedente(
            antecedente_id
        )

        await tratar_escolhas_raciais_pericia(
            interaction,
            self.user_id,
            self.estado
        )


# =========================================================
# ESCOLHAS RACIAIS DE PERÍCIA
# =========================================================

async def tratar_escolhas_raciais_pericia(
    interaction,
    user_id,
    estado
):
    raca = estado[
        "raca"
    ]

    subraca = estado[
        "subraca"
    ]

    subraca_id = (
        subraca["id"]
        if subraca
        else None
    )

    escolhas = listar_escolhas_raciais(
        raca["id"],
        subraca_id
    )

    escolhas_pericia = [
        item
        for item in escolhas
        if item["tipo"] == "pericia"
    ]

    quantidade = sum(
        item["quantidade"]
        for item in escolhas_pericia
    )

    if quantidade <= 0:

        await tratar_ferramenta_racial(
            interaction,
            user_id,
            estado
        )

        return

    ja_possui = set(
        estado[
            "pericias_antecedente"
        ]
    )

    ja_possui.update(
        estado[
            "pericias_raciais"
        ]
    )

    disponiveis = [
        pericia
        for pericia in TODAS_PERICIAS
        if pericia not in ja_possui
    ]

    view = EscolhaPericiasRaciaisView(
        user_id,
        estado,
        disponiveis,
        quantidade
    )

    await mostrar_etapa(
        interaction,
        (
            f"🧬 Sua raça permite escolher "
            f"**{quantidade} perícia(s)**.\n\n"
            "Escolha:"
        ),
        view
    )


class EscolhaPericiasRaciaisView(
    ViewDaFicha
):

    def __init__(
        self,
        user_id,
        estado,
        pericias,
        quantidade
    ):
        super().__init__(
            user_id,
            estado
        )

        self.select = discord.ui.Select(
            placeholder=(
                f"Escolha {quantidade} perícia(s)"
            ),
            min_values=quantidade,
            max_values=quantidade,
            options=[
                discord.SelectOption(
                    label=NOMES_PERICIAS[
                        pericia
                    ],
                    value=pericia
                )
                for pericia in pericias
            ]
        )

        self.select.callback = (
            self.escolher
        )

        self.add_item(
            self.select
        )

    async def escolher(
        self,
        interaction
    ):
        self.estado[
            "pericias_raciais"
        ].extend(
            self.select.values
        )

        await tratar_ferramenta_racial(
            interaction,
            self.user_id,
            self.estado
        )

# =========================================================
# ESCOLHA DE FERRAMENTA RACIAL - ANÃO
# =========================================================

async def tratar_ferramenta_racial(
    interaction,
    user_id,
    estado
):
    raca = estado[
        "raca"
    ]

    subraca = estado[
        "subraca"
    ]

    subraca_id = (
        subraca["id"]
        if subraca
        else None
    )

    escolhas = listar_escolhas_raciais(
        raca["id"],
        subraca_id
    )

    possui_escolha = any(
        item["tipo"] == "ferramenta_anao"
        for item in escolhas
    )

    if not possui_escolha:

        await mostrar_pericias_classe(
            interaction,
            user_id,
            estado
        )

        return

    view = EscolhaFerramentaAnaoView(
        user_id,
        estado
    )

    await mostrar_etapa(
        interaction,
        (
            "🔨 Como Anão, escolha uma "
            "proficiência com ferramenta de artesão:"
        ),
        view
    )


class EscolhaFerramentaAnaoView(
    ViewDaFicha
):

    def __init__(
        self,
        user_id,
        estado
    ):
        super().__init__(
            user_id,
            estado
        )

        self.select = discord.ui.Select(
            placeholder="Escolha a ferramenta",
            min_values=1,
            max_values=1,
            options=[
                discord.SelectOption(
                    label="Ferramentas de Ferreiro",
                    value="Ferramentas de Ferreiro"
                ),

                discord.SelectOption(
                    label="Suprimentos de Cervejeiro",
                    value="Suprimentos de Cervejeiro"
                ),

                discord.SelectOption(
                    label="Ferramentas de Pedreiro",
                    value="Ferramentas de Pedreiro"
                ),
            ]
        )

        self.select.callback = (
            self.escolher
        )

        self.add_item(
            self.select
        )

    async def escolher(
        self,
        interaction
    ):
        ferramenta = (
            self.select.values[0]
        )

        self.estado[
            "proficiencias_raciais"
        ].append(
            {
                "tipo": "ferramenta",
                "nome": ferramenta,
            }
        )

        await mostrar_pericias_classe(
            interaction,
            self.user_id,
            self.estado
        )
# =========================================================
# PERÍCIAS DA CLASSE
# =========================================================

async def mostrar_pericias_classe(
    interaction,
    user_id,
    estado
):
    classe = estado[
        "classe"
    ]

    opcoes = listar_pericias_classe(
        classe["id"]
    )

    if "todas" in opcoes:

        opcoes = list(
            TODAS_PERICIAS
        )

    ja_possui = set(
        estado[
            "pericias_raciais"
        ]
    )

    ja_possui.update(
        estado[
            "pericias_antecedente"
        ]
    )

    opcoes = [
        pericia
        for pericia in opcoes
        if pericia not in ja_possui
    ]

    quantidade = classe[
        "quantidade_pericias"
    ]

    if len(opcoes) < quantidade:

        await mostrar_erro(
            interaction,
            (
                "Não existem perícias suficientes "
                "disponíveis para completar "
                "essa ficha."
            )
        )

        return

    view = EscolhaPericiasClasseView(
        user_id,
        estado,
        opcoes,
        quantidade
    )

    await mostrar_etapa(
        interaction,
        (
            f"🎯 Escolha **{quantidade} "
            "perícia(s)** da classe "
            f"**{classe['nome']}**:"
        ),
        view
    )


class EscolhaPericiasClasseView(
    ViewDaFicha
):

    def __init__(
        self,
        user_id,
        estado,
        pericias,
        quantidade
    ):
        super().__init__(
            user_id,
            estado
        )

        self.select = discord.ui.Select(
            placeholder=(
                f"Escolha {quantidade} perícia(s)"
            ),
            min_values=quantidade,
            max_values=quantidade,
            options=[
                discord.SelectOption(
                    label=NOMES_PERICIAS.get(
                        pericia,
                        pericia
                    ),
                    value=pericia
                )
                for pericia in pericias
            ]
        )

        self.select.callback = (
            self.escolher
        )

        self.add_item(
            self.select
        )

    async def escolher(
        self,
        interaction
    ):
        self.estado[
            "pericias_classe"
        ] = list(
            self.select.values
        )

        await iniciar_rolagem_atributos(
            interaction,
            self.user_id,
            self.estado
        )


# =========================================================
# ROLAGEM DE ATRIBUTOS
# =========================================================

def rolar_atributo():
    dados = [
        random.randint(
            1,
            6
        )
        for _ in range(4)
    ]

    dados.sort(
        reverse=True
    )

    return sum(
        dados[:3]
    )


async def iniciar_rolagem_atributos(
    interaction,
    user_id,
    estado
):
    rolagens = [
        rolar_atributo()
        for _ in range(6)
    ]

    estado[
        "rolagens"
    ] = rolagens

    valores = ", ".join(
        str(valor)
        for valor in rolagens
    )

    view = DistribuirAtributosView(
        user_id,
        estado
    )

    await mostrar_etapa(
        interaction,
        (
            "🎲 **Atributos rolados!**\n\n"
            f"`{valores}`\n\n"
            "Cada valor foi obtido com "
            "**4d6 descartando o menor dado**.\n\n"
            "Clique abaixo para distribuir "
            "os valores."
        ),
        view
    )


class DistribuirAtributosView(
    ViewDaFicha
):

    @discord.ui.button(
        label="Distribuir atributos",
        style=discord.ButtonStyle.primary,
        emoji="🎲"
    )
    async def distribuir(
        self,
        interaction,
        button
    ):
        await interaction.response.send_modal(
            DistribuirAtributosModal(
                self.estado
            )
        )


# =========================================================
# MODAL DE DISTRIBUIÇÃO
# =========================================================

class DistribuirAtributosModal(
    discord.ui.Modal,
    title="Distribuir atributos"
):

    primeiros = discord.ui.TextInput(
        label="FOR, DES, CON",
        placeholder="Ex.: 15, 14, 13",
        required=True
    )

    segundos = discord.ui.TextInput(
        label="INT, SAB, CAR",
        placeholder="Ex.: 12, 10, 8",
        required=True
    )

    def __init__(
        self,
        estado
    ):
        super().__init__()

        self.estado = estado

    async def on_submit(
        self,
        interaction
    ):
        try:

            primeira_metade = [
                int(
                    item.strip()
                )
                for item in str(
                    self.primeiros.value
                ).split(",")
            ]

            segunda_metade = [
                int(
                    item.strip()
                )
                for item in str(
                    self.segundos.value
                ).split(",")
            ]

        except ValueError:

            await mostrar_erro(
                interaction,
                (
                    "Digite somente números "
                    "separados por vírgulas.\n\n"
                    "Exemplo: `15, 14, 13`"
                )
            )

            return

        if (
            len(primeira_metade) != 3
            or
            len(segunda_metade) != 3
        ):

            await mostrar_erro(
                interaction,
                (
                    "Você precisa informar "
                    "exatamente três valores "
                    "em cada campo."
                )
            )

            return

        valores = (
            primeira_metade
            +
            segunda_metade
        )

        if (
            Counter(valores)
            !=
            Counter(
                self.estado[
                    "rolagens"
                ]
            )
        ):

            rolados = ", ".join(
                str(item)
                for item in self.estado[
                    "rolagens"
                ]
            )

            await mostrar_erro(
                interaction,
                (
                    "Você precisa usar exatamente "
                    "os valores que foram rolados.\n\n"
                    f"Rolagens: `{rolados}`"
                )
            )

            return

        self.estado[
            "atributos_base"
        ] = {
            "forca":
                primeira_metade[0],

            "destreza":
                primeira_metade[1],

            "constituicao":
                primeira_metade[2],

            "inteligencia":
                segunda_metade[0],

            "sabedoria":
                segunda_metade[1],

            "carisma":
                segunda_metade[2],
        }

        await aplicar_bonus_raciais(
            interaction,
            self.estado
        )


# =========================================================
# BÔNUS RACIAIS FIXOS
# =========================================================

async def aplicar_bonus_raciais(
    interaction,
    estado
):
    raca = estado[
        "raca"
    ]

    subraca = estado[
        "subraca"
    ]

    subraca_id = (
        subraca["id"]
        if subraca
        else None
    )

    bonus = listar_bonus_atributos_raciais(
        raca["id"],
        subraca_id
    )

    atributos = dict(
        estado[
            "atributos_base"
        ]
    )

    atributos_com_bonus_fixo = set()

    for item in bonus:

        atributo = item[
            "atributo"
        ]

        valor_bonus = item[
            "bonus"
        ]

        if atributo in atributos:

            atributos[
                atributo
            ] += valor_bonus

            atributos_com_bonus_fixo.add(
                atributo
            )

    estado[
        "atributos_finais"
    ] = atributos

    escolhas = listar_escolhas_raciais(
        raca["id"],
        subraca_id
    )

    escolhas_atributo = [
        item
        for item in escolhas
        if item["tipo"] == "atributo"
    ]

    quantidade = sum(
        item["quantidade"]
        for item in escolhas_atributo
    )

    if quantidade <= 0:

        await iniciar_equipamentos(
            interaction,
            interaction.user.id,
            estado
        )

        return

    disponiveis = [
        atributo
        for atributo in TODOS_ATRIBUTOS
        if atributo not in atributos_com_bonus_fixo
    ]

    quantidade = min(
        quantidade,
        len(disponiveis)
    )

    view = EscolhaBonusAtributosRaciaisView(
        interaction.user.id,
        estado,
        disponiveis,
        quantidade
    )

    await mostrar_etapa(
        interaction,
        (
            "🧬 Sua raça permite escolher "
            "atributos adicionais.\n\n"
            f"Escolha **{quantidade}**:"
        ),
        view
    )


class EscolhaBonusAtributosRaciaisView(
    ViewDaFicha
):

    def __init__(
        self,
        user_id,
        estado,
        atributos,
        quantidade
    ):
        super().__init__(
            user_id,
            estado
        )

        self.select = discord.ui.Select(
            placeholder="Escolha os atributos",
            min_values=quantidade,
            max_values=quantidade,
            options=[
                discord.SelectOption(
                    label=NOMES_ATRIBUTOS[
                        atributo
                    ],
                    value=atributo
                )
                for atributo in atributos
            ]
        )

        self.select.callback = (
            self.escolher
        )

        self.add_item(
            self.select
        )

    async def escolher(
        self,
        interaction
    ):
        escolhidos = list(
            self.select.values
        )

        self.estado[
            "escolhas_atributos_raciais"
        ] = escolhidos

        for atributo in escolhidos:

            self.estado[
                "atributos_finais"
            ][atributo] += 1

        await iniciar_equipamentos(
            interaction,
            self.user_id,
            self.estado
        )


# =========================================================
# EQUIPAMENTOS
# =========================================================

async def iniciar_equipamentos(
    interaction,
    user_id,
    estado
):
    escolhas = listar_escolhas_equipamento_classe(
        estado[
            "classe"
        ]["id"]
    )

    estado[
        "escolhas_equipamento"
    ] = escolhas

    estado[
        "indice_equipamento"
    ] = 0

    estado[
        "equipamentos_escolhidos"
    ] = []

    if not escolhas:

        await tratar_truque_alto_elfo(
            interaction,
            user_id,
            estado
        )

        return

    await mostrar_proxima_escolha_equipamento(
        interaction,
        user_id,
        estado
    )


async def mostrar_proxima_escolha_equipamento(
    interaction,
    user_id,
    estado
):
    indice = estado[
        "indice_equipamento"
    ]

    escolhas = estado[
        "escolhas_equipamento"
    ]

    if indice >= len(escolhas):

        await tratar_truque_alto_elfo(
            interaction,
            user_id,
            estado
        )

        return

    escolha = escolhas[
        indice
    ]

    opcoes = escolha[
        "opcoes"
    ]

    # Se só existe uma opção,
    # é equipamento fixo.
    if len(opcoes) == 1:

        pacote = next(
            iter(
                opcoes.values()
            )
        )

        await processar_pacote_equipamento(
            interaction,
            user_id,
            estado,
            pacote
        )

        return

    view = EscolhaEquipamentoView(
        user_id,
        estado,
        escolha
    )

    await mostrar_etapa(
        interaction,
        (
            "🎒 **Equipamento inicial**\n\n"
            f"{escolha['titulo']}"
        ),
        view
    )


class EscolhaEquipamentoView(
    ViewDaFicha
):

    def __init__(
        self,
        user_id,
        estado,
        escolha
    ):
        super().__init__(
            user_id,
            estado
        )

        self.escolha = escolha

        opcoes_discord = []

        for numero, pacote in (
            escolha[
                "opcoes"
            ].items()
        ):

            partes = []

            for item in pacote:

                if item["nome"]:

                    quantidade = item[
                        "quantidade"
                    ]

                    if quantidade > 1:

                        partes.append(
                            (
                                f"{quantidade}x "
                                f"{item['nome']}"
                            )
                        )

                    else:

                        partes.append(
                            item["nome"]
                        )

                else:

                    categoria = (
                        item["categoria"]
                        .replace(
                            "_",
                            " "
                        )
                        .title()
                    )

                    quantidade = item[
                        "quantidade"
                    ]

                    if quantidade > 1:

                        partes.append(
                            (
                                f"{quantidade}x "
                                f"{categoria}"
                            )
                        )

                    else:

                        partes.append(
                            categoria
                        )

            texto = " + ".join(
                partes
            )

            opcoes_discord.append(
                discord.SelectOption(
                    label=texto[:100],
                    value=str(
                        numero
                    )
                )
            )

        self.select = discord.ui.Select(
            placeholder="Escolha uma opção",
            min_values=1,
            max_values=1,
            options=opcoes_discord
        )

        self.select.callback = (
            self.escolher
        )

        self.add_item(
            self.select
        )

    async def escolher(
        self,
        interaction
    ):
        numero = int(
            self.select.values[0]
        )

        pacote = self.escolha[
            "opcoes"
        ][numero]

        await processar_pacote_equipamento(
            interaction,
            self.user_id,
            self.estado,
            pacote
        )


# =========================================================
# PROCESSAR PACOTE
# =========================================================

async def processar_pacote_equipamento(
    interaction,
    user_id,
    estado,
    pacote
):
    categorias = []

    for item in pacote:

        # Item específico.
        if item[
            "equipamento_id"
        ] is not None:

            estado[
                "equipamentos_escolhidos"
            ].append(
                {
                    "equipamento_id":
                        item[
                            "equipamento_id"
                        ],

                    "nome":
                        item[
                            "nome"
                        ],

                    "quantidade":
                        item[
                            "quantidade"
                        ],
                }
            )

        # Categoria.
        elif item[
            "categoria"
        ]:

            quantidade = item[
                "quantidade"
            ]

            # Cria uma escolha por unidade.
            # Assim "2 armas marciais"
            # permite escolher duas diferentes.
            for _ in range(
                quantidade
            ):

                categorias.append(
                    {
                        "categoria":
                            item[
                                "categoria"
                            ],

                        "quantidade": 1,
                    }
                )

    if categorias:

        estado[
            "categorias_pendentes"
        ] = categorias

        estado[
            "indice_categoria"
        ] = 0

        await mostrar_categoria_pendente(
            interaction,
            user_id,
            estado
        )

        return

    estado[
        "indice_equipamento"
    ] += 1

    await mostrar_proxima_escolha_equipamento(
        interaction,
        user_id,
        estado
    )


# =========================================================
# CATEGORIAS DE EQUIPAMENTO
# =========================================================

async def mostrar_categoria_pendente(
    interaction,
    user_id,
    estado
):
    indice = estado[
        "indice_categoria"
    ]

    categorias = estado[
        "categorias_pendentes"
    ]

    if indice >= len(categorias):

        estado[
            "indice_equipamento"
        ] += 1

        await mostrar_proxima_escolha_equipamento(
            interaction,
            user_id,
            estado
        )

        return

    categoria_info = categorias[
        indice
    ]

    categoria = categoria_info[
        "categoria"
    ]

    equipamentos = listar_equipamentos_categoria(
        categoria
    )

    if not equipamentos:

        await mostrar_erro(
            interaction,
            (
                "Nenhum equipamento foi encontrado "
                f"para a categoria `{categoria}`."
            )
        )

        return

    view = EscolhaCategoriaEquipamentoView(
        user_id,
        estado,
        categoria_info,
        equipamentos
    )

    nome_categoria = (
        categoria
        .replace(
            "_",
            " "
        )
        .title()
    )

    await mostrar_etapa(
        interaction,
        (
            "🎒 Escolha um equipamento de:\n\n"
            f"**{nome_categoria}**"
        ),
        view
    )


class EscolhaCategoriaEquipamentoView(
    ViewDaFicha
):

    def __init__(
        self,
        user_id,
        estado,
        categoria_info,
        equipamentos
    ):
        super().__init__(
            user_id,
            estado
        )

        self.categoria_info = (
            categoria_info
        )

        self.equipamentos = equipamentos

        self.select = discord.ui.Select(
            placeholder="Escolha o equipamento",
            min_values=1,
            max_values=1,
            options=[
                discord.SelectOption(
                    label=item["nome"],
                    value=str(
                        item["id"]
                    )
                )
                for item in equipamentos
            ]
        )

        self.select.callback = (
            self.escolher
        )

        self.add_item(
            self.select
        )

    async def escolher(
        self,
        interaction
    ):
        equipamento_id = int(
            self.select.values[0]
        )

        equipamento = next(
            item
            for item in self.equipamentos
            if item[
                "id"
            ] == equipamento_id
        )

        self.estado[
            "equipamentos_escolhidos"
        ].append(
            {
                "equipamento_id":
                    equipamento[
                        "id"
                    ],

                "nome":
                    equipamento[
                        "nome"
                    ],

                "quantidade": 1,
            }
        )

        self.estado[
            "indice_categoria"
        ] += 1

        await mostrar_categoria_pendente(
            interaction,
            self.user_id,
            self.estado
        )



# =========================================================
# TRUQUE RACIAL - ALTO ELFO
# =========================================================

async def tratar_truque_alto_elfo(
    interaction,
    user_id,
    estado
):
    subraca = estado[
        "subraca"
    ]

    nome_subraca = (
        subraca["nome"]
        if subraca
        else None
    )

    if nome_subraca != "Alto Elfo":

        await finalizar_ficha(
            interaction,
            estado
        )

        return

    truques = listar_truques_mago()

    if not truques:

        await mostrar_erro(
            interaction,
            (
                "Nenhum truque de Mago foi "
                "encontrado no banco. Rode os "
                "populadores de magias primeiro."
            )
        )

        return

    view = EscolhaTruqueAltoElfoView(
        user_id,
        estado,
        truques
    )

    await mostrar_etapa(
        interaction,
        (
            "✨ Como **Alto Elfo**, escolha "
            "**1 truque da lista de Mago**.\n\n"
            "Inteligência será a habilidade "
            "de conjuração desse truque."
        ),
        view
    )


class EscolhaTruqueAltoElfoView(
    ViewDaFicha
):

    def __init__(
        self,
        user_id,
        estado,
        truques
    ):
        super().__init__(
            user_id,
            estado
        )

        self.truques = truques

        self.select = discord.ui.Select(
            placeholder="Escolha seu truque de Mago",
            min_values=1,
            max_values=1,
            options=[
                discord.SelectOption(
                    label=item["nome"],
                    value=item["nome"],
                    description=(
                        item["escola"].capitalize()
                        if item["escola"]
                        else None
                    )
                )
                for item in truques[:25]
            ]
        )

        self.select.callback = (
            self.escolher
        )

        self.add_item(
            self.select
        )

    async def escolher(
        self,
        interaction
    ):
        self.estado[
            "truque_alto_elfo"
        ] = self.select.values[0]

        await finalizar_ficha(
            interaction,
            self.estado
        )

# =========================================================
# FINALIZAR PERSONAGEM
# =========================================================

async def finalizar_ficha(
    interaction,
    estado
):
    raca = estado[
        "raca"
    ]

    subraca = estado[
        "subraca"
    ]

    classe = estado[
        "classe"
    ]

    subclasse = estado[
        "subclasse"
    ]

    antecedente = estado[
        "antecedente"
    ]

    nome_subraca = (
        subraca["nome"]
        if subraca
        else None
    )

    nome_subclasse = (
        subclasse["nome"]
        if subclasse
        else None
    )

    # =====================================================
    # PERÍCIAS FINAIS
    # =====================================================

    pericias = set()

    pericias.update(
        estado[
            "pericias_raciais"
        ]
    )

    pericias.update(
        estado[
            "pericias_antecedente"
        ]
    )

    pericias.update(
        estado[
            "pericias_classe"
        ]
    )

    # =====================================================
    # SALVAGUARDAS
    # =====================================================

    salvaguardas = (
        listar_salvaguardas_classe(
            classe["id"]
        )
    )

    # =====================================================
    # PROFICIÊNCIAS
    # =====================================================

    proficiencias = (
        listar_proficiencias_classe(
            classe["id"]
        )
    )

    proficiencias += (
        listar_proficiencias_antecedente(
            antecedente["id"]
        )
    )

    proficiencias += estado[
    "proficiencias_raciais"
    ]

    # =====================================================
    # JOGADOR
    # =====================================================

    garantir_jogador(
        interaction.user.id,
        interaction.user.name
    )

    # =====================================================
    # SALVAR PERSONAGEM
    # =====================================================

    try:

        resultado = criar_personagem(
            discord_id=
                interaction.user.id,

            nome_personagem=
                estado["nome"],

            raca=
                raca["nome"],

            subraca=
                nome_subraca,

            classe=
                classe,

            subclasse=
                nome_subclasse,

            antecedente=
                antecedente["nome"],

            deslocamento=(
                35
                if nome_subraca == "Elfo da Floresta"
                else raca["deslocamento"]
            ),

            atributos=
                estado[
                    "atributos_finais"
                ],

            pericias=
                list(
                    pericias
                ),

            salvaguardas=
                salvaguardas,

            proficiencias=
                proficiencias,
        )

        personagem_id = resultado[
            "id"
        ]

        # ================================================
        # SISTEMA MÁGICO
        # ================================================

        inicializar_sistema_magico_personagem(
            personagem_id=personagem_id,
            classe_nome=classe["nome"],
            raca_nome=raca["nome"],
            subraca_nome=nome_subraca,
            nivel_personagem=1,
            truque_alto_elfo=estado.get(
                "truque_alto_elfo"
            ),
        )

        # ================================================
        # INVENTÁRIO
        # ================================================

        salvar_inventario(
            personagem_id,
            estado[
                "equipamentos_escolhidos"
            ]
        )

        # ================================================
        # CA
        # ================================================

        ca = calcular_ca_personagem(
            personagem_id,
            classe["nome"],
            estado[
                "atributos_finais"
            ]
        )

    except Exception as erro:

        print(
            "Erro ao criar ficha:"
        )

        print(
            erro
        )

        await mostrar_erro(
            interaction,
            (
                "Ocorreu um erro ao salvar "
                "a ficha. Veja o terminal "
                "do Mini Mestre."
            )
        )

        return

    # =====================================================
    # EMBED FINAL
    # =====================================================

    embed = discord.Embed(
        title="📜 Ficha criada!",
        description=(
            f"**{estado['nome']}** está pronto "
            "para começar a aventura."
        )
    )

    embed.add_field(
        name="Raça",
        value=raca["nome"],
        inline=True
    )

    embed.add_field(
        name="Sub-raça",
        value=(
            nome_subraca
            or "—"
        ),
        inline=True
    )

    embed.add_field(
        name="Classe",
        value=classe["nome"],
        inline=True
    )

    embed.add_field(
        name="Subclasse",
        value=(
            nome_subclasse
            or "Ainda não escolhida"
        ),
        inline=True
    )

    embed.add_field(
        name="Antecedente",
        value=antecedente["nome"],
        inline=True
    )

    embed.add_field(
        name="Nível",
        value="1",
        inline=True
    )

    # =====================================================
    # ATRIBUTOS
    # =====================================================

    atributos = estado[
        "atributos_finais"
    ]

    linhas_atributos = []

    for atributo in TODOS_ATRIBUTOS:

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

        linhas_atributos.append(
            (
                f"**{NOMES_ATRIBUTOS[atributo]}:** "
                f"{valor} "
                f"({sinal}{modificador})"
            )
        )

    embed.add_field(
        name="🎲 Atributos",
        value="\n".join(
            linhas_atributos
        ),
        inline=False
    )

    # =====================================================
    # COMBATE
    # =====================================================

    embed.add_field(
        name="❤️ PV",
        value=(
            f"{resultado['pv_maximo']}"
            f"/"
            f"{resultado['pv_maximo']}"
        ),
        inline=True
    )

    embed.add_field(
        name="🛡️ CA",
        value=str(
            ca
        ),
        inline=True
    )

    iniciativa = resultado[
        "iniciativa"
    ]

    sinal_iniciativa = (
        "+"
        if iniciativa >= 0
        else ""
    )

    embed.add_field(
        name="⚡ Iniciativa",
        value=(
            f"{sinal_iniciativa}"
            f"{iniciativa}"
        ),
        inline=True
    )

    # =====================================================
    # PERÍCIAS
    # =====================================================

    nomes_pericias = [
        NOMES_PERICIAS[
            pericia
        ]
        for pericia in sorted(
            pericias
        )
    ]

    embed.add_field(
        name="🎯 Perícias",
        value=(
            ", ".join(
                nomes_pericias
            )
            if nomes_pericias
            else "Nenhuma"
        ),
        inline=False
    )

    # =====================================================
    # EQUIPAMENTOS
    # =====================================================

    itens = estado[
        "equipamentos_escolhidos"
    ]

    if itens:

        linhas_itens = []

        for item in itens:

            quantidade = item.get(
                "quantidade",
                1
            )

            if quantidade > 1:

                linhas_itens.append(
                    (
                        f"{quantidade}x "
                        f"{item['nome']}"
                    )
                )

            else:

                linhas_itens.append(
                    item[
                        "nome"
                    ]
                )

        embed.add_field(
            name="🎒 Equipamento inicial",
            value="\n".join(
                linhas_itens
            ),
            inline=False
        )

    embed.set_footer(
        text=(
            f"ID da ficha: "
            f"{personagem_id}"
        )
    )

    # =====================================================
    # MOSTRAR RESULTADO
    # =====================================================

    if interaction.response.is_done():

        await interaction.followup.send(
            embed=embed,
            ephemeral=True
        )

    elif interaction.message is not None:

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


# =========================================================
# COG
# =========================================================

class Fichas(
    commands.Cog
):

    def __init__(
        self,
        bot
    ):
        self.bot = bot

    @app_commands.command(
        name="criar_ficha",
        description=(
            "Cria uma ficha de personagem "
            "de D&D 5e."
        )
    )
    async def criar_ficha(
        self,
        interaction
    ):
        await interaction.response.send_modal(
            NomePersonagemModal()
        )


# =========================================================
# SETUP
# =========================================================

async def setup(
    bot
):
    await bot.add_cog(
        Fichas(bot)
    )