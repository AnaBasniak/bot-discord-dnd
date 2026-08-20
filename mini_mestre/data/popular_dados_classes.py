from mini_mestre.database import conectar


SALVAGUARDAS = {
    "Bárbaro": [
        "forca",
        "constituicao",
    ],

    "Bardo": [
        "destreza",
        "carisma",
    ],

    "Bruxo": [
        "sabedoria",
        "carisma",
    ],

    "Clérigo": [
        "sabedoria",
        "carisma",
    ],

    "Druida": [
        "inteligencia",
        "sabedoria",
    ],

    "Feiticeiro": [
        "constituicao",
        "carisma",
    ],

    "Guerreiro": [
        "forca",
        "constituicao",
    ],

    "Ladino": [
        "destreza",
        "inteligencia",
    ],

    "Mago": [
        "inteligencia",
        "sabedoria",
    ],

    "Monge": [
        "forca",
        "destreza",
    ],

    "Paladino": [
        "sabedoria",
        "carisma",
    ],

    "Patrulheiro": [
        "forca",
        "destreza",
    ],
}


PERICIAS = {
    "Bárbaro": [
        "adestrar_animais",
        "atletismo",
        "intimidacao",
        "natureza",
        "percepcao",
        "sobrevivencia",
    ],

    "Bardo": [
        "todas",
    ],

    "Bruxo": [
        "arcanismo",
        "enganacao",
        "historia",
        "intimidacao",
        "investigacao",
        "natureza",
        "religiao",
    ],

    "Clérigo": [
        "historia",
        "intuicao",
        "medicina",
        "persuasao",
        "religiao",
    ],

    "Druida": [
        "adestrar_animais",
        "arcanismo",
        "intuicao",
        "medicina",
        "natureza",
        "percepcao",
        "religiao",
        "sobrevivencia",
    ],

    "Feiticeiro": [
        "arcanismo",
        "enganacao",
        "intuicao",
        "intimidacao",
        "persuasao",
        "religiao",
    ],

    "Guerreiro": [
        "acrobacia",
        "adestrar_animais",
        "atletismo",
        "historia",
        "intuicao",
        "intimidacao",
        "percepcao",
        "sobrevivencia",
    ],

    "Ladino": [
        "acrobacia",
        "atletismo",
        "atuacao",
        "enganacao",
        "furtividade",
        "intimidacao",
        "intuicao",
        "investigacao",
        "percepcao",
        "persuasao",
        "prestidigitacao",
    ],

    "Mago": [
        "arcanismo",
        "historia",
        "intuicao",
        "investigacao",
        "medicina",
        "religiao",
    ],

    "Monge": [
        "acrobacia",
        "atletismo",
        "furtividade",
        "historia",
        "intuicao",
        "religiao",
    ],

    "Paladino": [
        "atletismo",
        "intuicao",
        "intimidacao",
        "medicina",
        "persuasao",
        "religiao",
    ],

    "Patrulheiro": [
        "adestrar_animais",
        "atletismo",
        "furtividade",
        "intuicao",
        "investigacao",
        "natureza",
        "percepcao",
        "sobrevivencia",
    ],
}


def buscar_classe(
    cursor,
    nome
):
    cursor.execute(
        """
        SELECT id
        FROM classes
        WHERE nome = %s;
        """,
        (nome,)
    )

    resultado = cursor.fetchone()

    if resultado is None:
        raise ValueError(
            f"Classe não encontrada: {nome}"
        )

    return resultado[0]


def popular_dados_classes():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        # Como são dados fixos do livro,
        # limpamos antes de recriar.
        cursor.execute(
            """
            DELETE FROM salvaguardas_classes;
            """
        )

        cursor.execute(
            """
            DELETE FROM pericias_classes;
            """
        )

        # =============================================
        # SALVAGUARDAS
        # =============================================

        for nome_classe, atributos in SALVAGUARDAS.items():

            classe_id = buscar_classe(
                cursor,
                nome_classe
            )

            for atributo in atributos:

                cursor.execute(
                    """
                    INSERT INTO salvaguardas_classes (
                        classe_id,
                        atributo
                    )
                    VALUES (%s, %s);
                    """,
                    (
                        classe_id,
                        atributo
                    )
                )

        # =============================================
        # PERÍCIAS
        # =============================================

        for nome_classe, pericias in PERICIAS.items():

            classe_id = buscar_classe(
                cursor,
                nome_classe
            )

            for pericia in pericias:

                cursor.execute(
                    """
                    INSERT INTO pericias_classes (
                        classe_id,
                        pericia
                    )
                    VALUES (%s, %s);
                    """,
                    (
                        classe_id,
                        pericia
                    )
                )

        conexao.commit()

        print(
            "Salvaguardas e perícias "
            "das classes cadastradas com sucesso!"
        )

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


if __name__ == "__main__":
    popular_dados_classes()