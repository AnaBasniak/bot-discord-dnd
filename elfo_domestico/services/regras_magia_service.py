from mini_mestre.database import conectar


# =========================================================
# TIPOS DE CONJURADOR
# =========================================================

TIPO_CONJURADOR = {

    "Bardo": "conhecidas",

    "Bruxo": "conhecidas",

    "Clérigo": "preparadas",

    "Druida": "preparadas",

    "Feiticeiro": "conhecidas",

    "Mago": "grimorio",

    "Paladino": "preparadas",

    "Patrulheiro": "conhecidas",
}


# =========================================================
# HABILIDADE DE CONJURAÇÃO
# =========================================================

HABILIDADE_CONJURACAO = {

    "Bardo": "carisma",

    "Bruxo": "carisma",

    "Clérigo": "sabedoria",

    "Druida": "sabedoria",

    "Feiticeiro": "carisma",

    "Mago": "inteligencia",

    "Paladino": "carisma",

    "Patrulheiro": "sabedoria",
}


# =========================================================
# NÍVEL EM QUE A CLASSE COMEÇA A CONJURAR
# =========================================================

NIVEL_INICIO_CONJURACAO = {

    "Bardo": 1,

    "Bruxo": 1,

    "Clérigo": 1,

    "Druida": 1,

    "Feiticeiro": 1,

    "Mago": 1,

    "Paladino": 2,

    "Patrulheiro": 2,
}


# =========================================================
# TRUQUES CONHECIDOS
# =========================================================
#
# Paladino e Patrulheiro não recebem truques pela
# característica normal de Conjuração desta versão.
# =========================================================

TRUQUES_CONHECIDOS = {

    "Bardo": {
        1: 2,
        2: 2,
        3: 2,
        4: 3,
        5: 3,
        6: 3,
        7: 3,
        8: 3,
        9: 3,
        10: 4,
        11: 4,
        12: 4,
        13: 4,
        14: 4,
        15: 4,
        16: 4,
        17: 4,
        18: 4,
        19: 4,
        20: 4,
    },

    "Bruxo": {
        1: 2,
        2: 2,
        3: 2,
        4: 3,
        5: 3,
        6: 3,
        7: 3,
        8: 3,
        9: 3,
        10: 4,
        11: 4,
        12: 4,
        13: 4,
        14: 4,
        15: 4,
        16: 4,
        17: 4,
        18: 4,
        19: 4,
        20: 4,
    },

    "Clérigo": {
        1: 3,
        2: 3,
        3: 3,
        4: 4,
        5: 4,
        6: 4,
        7: 4,
        8: 4,
        9: 4,
        10: 5,
        11: 5,
        12: 5,
        13: 5,
        14: 5,
        15: 5,
        16: 5,
        17: 5,
        18: 5,
        19: 5,
        20: 5,
    },

    "Druida": {
        1: 2,
        2: 2,
        3: 2,
        4: 3,
        5: 3,
        6: 3,
        7: 3,
        8: 3,
        9: 3,
        10: 4,
        11: 4,
        12: 4,
        13: 4,
        14: 4,
        15: 4,
        16: 4,
        17: 4,
        18: 4,
        19: 4,
        20: 4,
    },

    "Feiticeiro": {
        1: 4,
        2: 4,
        3: 4,
        4: 5,
        5: 5,
        6: 5,
        7: 5,
        8: 5,
        9: 5,
        10: 6,
        11: 6,
        12: 6,
        13: 6,
        14: 6,
        15: 6,
        16: 6,
        17: 6,
        18: 6,
        19: 6,
        20: 6,
    },

    "Mago": {
        1: 3,
        2: 3,
        3: 3,
        4: 4,
        5: 4,
        6: 4,
        7: 4,
        8: 4,
        9: 4,
        10: 5,
        11: 5,
        12: 5,
        13: 5,
        14: 5,
        15: 5,
        16: 5,
        17: 5,
        18: 5,
        19: 5,
        20: 5,
    },
}


# =========================================================
# MAGIAS CONHECIDAS
# =========================================================
#
# Usado por:
#
# Bardo
# Bruxo
# Feiticeiro
# Patrulheiro
#
# Não inclui truques.
# =========================================================

MAGIAS_CONHECIDAS = {

    "Bardo": {
        1: 4,
        2: 5,
        3: 6,
        4: 7,
        5: 8,
        6: 9,
        7: 10,
        8: 11,
        9: 12,
        10: 14,
        11: 15,
        12: 15,
        13: 16,
        14: 18,
        15: 19,
        16: 19,
        17: 20,
        18: 22,
        19: 22,
        20: 22,
    },

    "Bruxo": {
        1: 2,
        2: 3,
        3: 4,
        4: 5,
        5: 6,
        6: 7,
        7: 8,
        8: 9,
        9: 10,
        10: 10,
        11: 11,
        12: 11,
        13: 12,
        14: 12,
        15: 13,
        16: 13,
        17: 14,
        18: 14,
        19: 15,
        20: 15,
    },

    "Feiticeiro": {
        1: 2,
        2: 3,
        3: 4,
        4: 5,
        5: 6,
        6: 7,
        7: 8,
        8: 9,
        9: 10,
        10: 11,
        11: 12,
        12: 12,
        13: 13,
        14: 13,
        15: 14,
        16: 14,
        17: 15,
        18: 15,
        19: 15,
        20: 15,
    },

    "Patrulheiro": {
        1: 0,
        2: 2,
        3: 3,
        4: 3,
        5: 4,
        6: 4,
        7: 5,
        8: 5,
        9: 6,
        10: 6,
        11: 7,
        12: 7,
        13: 8,
        14: 8,
        15: 9,
        16: 9,
        17: 10,
        18: 10,
        19: 11,
        20: 11,
    },
}

# =========================================================
# BARDO - SEGREDOS MÁGICOS
# =========================================================

def limite_segredos_magicos(nivel):
    """
    Segredos Mágicos da classe Bardo.

    Nível 10:
        2 magias

    Nível 14:
        +2 magias

    Nível 18:
        +2 magias

    Essas magias contam no total normal de
    magias conhecidas do Bardo.
    """

    if nivel >= 18:
        return 6

    if nivel >= 14:
        return 4

    if nivel >= 10:
        return 2

    return 0


def contar_segredos_magicos(personagem_id):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM magias_personagens
            WHERE personagem_id = %s
              AND origem = 'segredo_magico';
            """,
            (personagem_id,)
        )

        return cursor.fetchone()[0]

    finally:
        cursor.close()
        conexao.close()


def validar_segredo_magico(
    personagem_id,
    classe,
    nivel_personagem,
    nivel_magia
):
    """
    Valida um Segredo Mágico normal do Bardo.

    Regras:
    - apenas Bardo;
    - disponível a partir do nível 10;
    - 2 escolhas no nível 10;
    - 4 escolhas no nível 14;
    - 6 escolhas no nível 18;
    - pode escolher magia de qualquer classe;
    - pode escolher truque;
    - deve respeitar o nível de magia que o Bardo
      consegue conjurar;
    - Segredos Mágicos normais contam dentro do
      total de magias conhecidas do Bardo.
    """

    if classe != "Bardo":
        return {
            "permitido": False,
            "motivo":
                "Apenas Bardos possuem Segredos Mágicos.",
        }

    limite_segredos = limite_segredos_magicos(
        nivel_personagem
    )

    if limite_segredos == 0:
        return {
            "permitido": False,
            "motivo":
                "O Bardo ainda não possui "
                "Segredos Mágicos.",
        }

    atuais_segredos = contar_segredos_magicos(
        personagem_id
    )

    if atuais_segredos >= limite_segredos:
        return {
            "permitido": False,
            "motivo":
                "Você já escolheu todos os Segredos "
                "Mágicos disponíveis nesse nível.",
        }

    if nivel_magia > 0:
        if not pode_acessar_nivel_magia(
            "Bardo",
            nivel_personagem,
            nivel_magia
        ):
            return {
                "permitido": False,
                "motivo":
                    "O Bardo ainda não consegue "
                    "conjurar magias desse nível.",
            }

    limite_total = limite_magias_conhecidas(
        "Bardo",
        nivel_personagem
    )

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM magias_personagens mp
            JOIN magias m
                ON m.id = mp.magia_id
            WHERE mp.personagem_id = %s
              AND m.nivel >= 1
              AND mp.origem IN (
                  'classe',
                  'segredo_magico'
              );
            """,
            (personagem_id,)
        )

        magias_niveladas = cursor.fetchone()[0]

    finally:
        cursor.close()
        conexao.close()

    if (
        nivel_magia >= 1
        and
        magias_niveladas >= limite_total
    ):
        return {
            "permitido": False,
            "motivo":
                "Você já atingiu o número máximo "
                "de magias conhecidas do Bardo "
                "para esse nível.",
        }

    return {
        "permitido": True,
        "motivo": None,
    }


# =========================================================
# UTIL
# =========================================================

def calcular_modificador(
    valor
):
    return (
        valor - 10
    ) // 2


# =========================================================
# REGRA DA CLASSE
# =========================================================

def obter_tipo_conjurador(
    classe
):
    return TIPO_CONJURADOR.get(
        classe
    )


def obter_habilidade_conjuracao(
    classe
):
    return HABILIDADE_CONJURACAO.get(
        classe
    )


def classe_conjura(
    classe,
    nivel
):
    inicio = NIVEL_INICIO_CONJURACAO.get(
        classe
    )

    if inicio is None:
        return False

    return nivel >= inicio


# =========================================================
# TRUQUES
# =========================================================

def limite_truques(
    classe,
    nivel
):
    tabela = TRUQUES_CONHECIDOS.get(
        classe
    )

    if tabela is None:
        return 0

    return tabela.get(
        nivel,
        0
    )


# =========================================================
# MAGIAS CONHECIDAS
# =========================================================

def limite_magias_conhecidas(
    classe,
    nivel
):
    tabela = MAGIAS_CONHECIDAS.get(
        classe
    )

    if tabela is None:
        return None

    return tabela.get(
        nivel,
        0
    )


# =========================================================
# ATRIBUTOS DO PERSONAGEM
# =========================================================

def buscar_atributos_magicos(
    personagem_id
):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT
                inteligencia,
                sabedoria,
                carisma
            FROM atributos
            WHERE personagem_id = %s;
            """,
            (personagem_id,)
        )

        resultado = cursor.fetchone()

        if resultado is None:
            return None

        return {
            "inteligencia": resultado[0],
            "sabedoria": resultado[1],
            "carisma": resultado[2],
        }

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# LIMITE DE MAGIAS PREPARADAS
# =========================================================

def limite_magias_preparadas(
    personagem_id,
    classe,
    nivel
):
    atributos = buscar_atributos_magicos(
        personagem_id
    )

    if atributos is None:
        return 0

    habilidade = obter_habilidade_conjuracao(
        classe
    )

    if habilidade is None:
        return 0

    modificador = calcular_modificador(
        atributos[
            habilidade
        ]
    )

    # Clérigo:
    # Sabedoria + nível de Clérigo

    if classe == "Clérigo":
        return max(
            1,
            modificador + nivel
        )

    # Druida:
    # Sabedoria + nível de Druida

    if classe == "Druida":
        return max(
            1,
            modificador + nivel
        )

    # Mago:
    # Inteligência + nível de Mago

    if classe == "Mago":
        return max(
            1,
            modificador + nivel
        )

    # Paladino:
    # Carisma + metade do nível,
    # arredondado para baixo.
    #
    # Paladino não conjura no nível 1.

    if classe == "Paladino":

        if nivel < 2:
            return 0

        return max(
            1,
            modificador
            + (nivel // 2)
        )

    return None


# =========================================================
# NÍVEL MÁXIMO DE MAGIA DISPONÍVEL
# =========================================================

def nivel_maximo_magia(
    classe,
    nivel_classe
):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT MAX(nivel_magia)
            FROM slots_magia_classes sc
            JOIN classes c
                ON c.id = sc.classe_id
            WHERE LOWER(c.nome) = LOWER(%s)
              AND sc.nivel_classe = %s
              AND sc.quantidade > 0;
            """,
            (
                classe,
                nivel_classe,
            )
        )

        resultado = cursor.fetchone()

        if (
            resultado is None
            or resultado[0] is None
        ):
            return 0

        return resultado[0]

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# QUANTIDADE ATUAL DE MAGIAS
# =========================================================

def contar_magias_personagem(
    personagem_id,
    nivel_magia=None,
    preparada=None,
    origem="classe"
):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        sql = """
            SELECT COUNT(*)
            FROM magias_personagens mp
            JOIN magias m
                ON m.id = mp.magia_id
            WHERE mp.personagem_id = %s
              AND mp.origem = %s
        """

        parametros = [
            personagem_id,
            origem,
        ]

        if nivel_magia is not None:
            sql += """
                AND m.nivel = %s
            """

            parametros.append(
                nivel_magia
            )

        if preparada is not None:
            sql += """
                AND mp.preparada = %s
            """

            parametros.append(
                preparada
            )

        cursor.execute(
            sql,
            tuple(parametros)
        )

        return cursor.fetchone()[0]

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# CONTAR TRUQUES DE CLASSE
# =========================================================

def contar_truques_personagem(
    personagem_id
):
    return contar_magias_personagem(
        personagem_id=
            personagem_id,

        nivel_magia=0,

        origem="classe",
    )


# =========================================================
# CONTAR MAGIAS DE NÍVEL 1+
# =========================================================

def contar_magias_niveladas(
    personagem_id
):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM magias_personagens mp
            JOIN magias m
                ON m.id = mp.magia_id
            WHERE mp.personagem_id = %s
              AND mp.origem = 'classe'
              AND m.nivel >= 1;
            """,
            (personagem_id,)
        )

        return cursor.fetchone()[0]

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# CONTAR PREPARADAS
# =========================================================

def contar_magias_preparadas(
    personagem_id
):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM magias_personagens mp
            JOIN magias m
                ON m.id = mp.magia_id
            WHERE mp.personagem_id = %s
              AND mp.origem = 'classe'
              AND mp.preparada = TRUE
              AND m.nivel >= 1;
            """,
            (personagem_id,)
        )

        return cursor.fetchone()[0]

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# MAGO - GRIMÓRIO
# =========================================================

def magias_minimas_grimorio_mago(
    nivel
):
    """
    Quantidade obtida apenas pela progressão normal:

    nível 1:
        6 magias

    cada nível adicional:
        +2 magias

    Isso NÃO é um limite máximo.

    Um Mago pode copiar outras magias encontradas
    durante a aventura para o grimório.
    """

    if nivel < 1:
        return 0

    return (
        6
        + (
            (nivel - 1)
            * 2
        )
    )


# =========================================================
# VALIDAR NÍVEL DA MAGIA
# =========================================================

def pode_acessar_nivel_magia(
    classe,
    nivel_classe,
    nivel_magia
):
    # Truques possuem suas próprias regras.

    if nivel_magia == 0:
        return (
            limite_truques(
                classe,
                nivel_classe
            )
            > 0
        )

    maximo = nivel_maximo_magia(
        classe,
        nivel_classe
    )

    return (
        nivel_magia
        <= maximo
    )


# =========================================================
# VALIDAR NOVO TRUQUE
# =========================================================

def validar_novo_truque(
    personagem_id,
    classe,
    nivel
):
    limite = limite_truques(
        classe,
        nivel
    )

    if limite <= 0:
        return {
            "permitido": False,
            "motivo": (
                "Essa classe não possui "
                "truques disponíveis nesse nível."
            ),
        }

    atuais = contar_truques_personagem(
        personagem_id
    )

    if atuais >= limite:
        return {
            "permitido": False,
            "motivo": (
                "Você já conhece o número máximo "
                "de truques permitido para esse nível."
            ),
        }

    return {
        "permitido": True,
        "motivo": None,
    }


# =========================================================
# VALIDAR MAGIA CONHECIDA
# =========================================================

def validar_nova_magia_conhecida(
    personagem_id,
    classe,
    nivel_personagem,
    nivel_magia
):
    if not classe_conjura(
        classe,
        nivel_personagem
    ):
        return {
            "permitido": False,
            "motivo": (
                "Essa classe ainda não possui "
                "a característica Conjuração."
            ),
        }

    if not pode_acessar_nivel_magia(
        classe,
        nivel_personagem,
        nivel_magia
    ):
        return {
            "permitido": False,
            "motivo": (
                "Seu nível ainda não permite "
                "magias desse nível."
            ),
        }

    tipo = obter_tipo_conjurador(
        classe
    )

    # =====================================================
    # CLASSES DE MAGIAS CONHECIDAS
    # =====================================================

    if tipo == "conhecidas":

        limite = limite_magias_conhecidas(
            classe,
            nivel_personagem
        )

        if limite is None:
            return {
                "permitido": False,
                "motivo": (
                    "Não foi encontrada a progressão "
                    "de magias conhecidas dessa classe."
                ),
            }

        atuais = contar_magias_niveladas(
            personagem_id
        )

        if atuais >= limite:
            return {
                "permitido": False,
                "motivo": (
                    "Você já conhece o número máximo "
                    "de magias permitido para esse nível."
                ),
            }

        return {
            "permitido": True,
            "motivo": None,
        }

    # =====================================================
    # MAGO
    # =====================================================
    #
    # Não existe limite máximo simples de grimório,
    # porque outras magias podem ser copiadas durante
    # a aventura.
    # =====================================================

    if tipo == "grimorio":

        return {
            "permitido": True,
            "motivo": None,
        }

    # =====================================================
    # CLASSES QUE PREPARAM DA LISTA
    # =====================================================
    #
    # Clérigo, Druida e Paladino não precisam
    # "aprender" individualmente a lista normal.
    #
    # Elas escolhem quais estarão preparadas.
    # =====================================================

    if tipo == "preparadas":

        return {
            "permitido": False,
            "motivo": (
                "Essa classe não aprende magias "
                "dessa forma. Use preparação de magias."
            ),
        }

    return {
        "permitido": False,
        "motivo": (
            "Classe sem regra de conjuração cadastrada."
        ),
    }


# =========================================================
# VALIDAR PREPARAÇÃO
# =========================================================

def validar_preparar_magia(
    personagem_id,
    classe,
    nivel_personagem,
    nivel_magia
):
    tipo = obter_tipo_conjurador(
        classe
    )

    if tipo not in (
        "preparadas",
        "grimorio",
    ):
        return {
            "permitido": False,
            "motivo": (
                "Essa classe não utiliza "
                "preparação de magias."
            ),
        }

    if nivel_magia == 0:

        return {
            "permitido": False,
            "motivo": (
                "Truques não precisam ser preparados."
            ),
        }

    if not pode_acessar_nivel_magia(
        classe,
        nivel_personagem,
        nivel_magia
    ):

        return {
            "permitido": False,
            "motivo": (
                "Seu personagem ainda não possui "
                "acesso a esse nível de magia."
            ),
        }

    limite = limite_magias_preparadas(
        personagem_id,
        classe,
        nivel_personagem
    )

    if limite is None:
        return {
            "permitido": False,
            "motivo": (
                "Essa classe não possui regra "
                "de preparação cadastrada."
            ),
        }

    atuais = contar_magias_preparadas(
        personagem_id
    )

    if atuais >= limite:

        return {
            "permitido": False,
            "motivo": (
                "Você já atingiu o limite "
                "de magias preparadas."
            ),
        }

    return {
        "permitido": True,
        "motivo": None,
    }


# =========================================================
# RESUMO DAS REGRAS DO PERSONAGEM
# =========================================================

def resumo_regras_magia(
    personagem_id,
    classe,
    nivel
):
    tipo = obter_tipo_conjurador(
        classe
    )

    habilidade = obter_habilidade_conjuracao(
        classe
    )

    conjura = classe_conjura(
        classe,
        nivel
    )

    truques = limite_truques(
        classe,
        nivel
    )

    nivel_maximo = nivel_maximo_magia(
        classe,
        nivel
    )

    conhecidas = limite_magias_conhecidas(
        classe,
        nivel
    )

    preparadas = None

    if tipo in (
        "preparadas",
        "grimorio",
    ):
        preparadas = limite_magias_preparadas(
            personagem_id,
            classe,
            nivel
        )

    grimorio_minimo = None

    if classe == "Mago":
        grimorio_minimo = (
            magias_minimas_grimorio_mago(
                nivel
            )
        )

    return {
        "classe": classe,
        "nivel": nivel,
        "conjura": conjura,
        "tipo": tipo,
        "habilidade": habilidade,
        "truques": truques,
        "magias_conhecidas": conhecidas,
        "magias_preparadas": preparadas,
        "nivel_maximo_magia": nivel_maximo,
        "grimorio_minimo_mago": grimorio_minimo,
    }