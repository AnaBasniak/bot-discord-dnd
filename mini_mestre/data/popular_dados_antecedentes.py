from mini_mestre.database import conectar


DADOS_ANTECEDENTES = {

    "Acólito": {
        "pericias": [
            "intuicao",
            "religiao",
        ],

        "proficiencias": [],

        "idiomas": 2,
    },

    "Artesão de Guilda": {
        "pericias": [
            "intuicao",
            "persuasao",
        ],

        "proficiencias": [
            (
                "ferramenta",
                "Uma ferramenta de artesão à escolha"
            ),
        ],

        "idiomas": 1,
    },

    "Artista": {
        "pericias": [
            "acrobacia",
            "atuacao",
        ],

        "proficiencias": [
            (
                "ferramenta",
                "Kit de disfarce"
            ),
            (
                "instrumento",
                "Um instrumento musical à escolha"
            ),
        ],

        "idiomas": 0,
    },

    "Charlatão": {
        "pericias": [
            "enganacao",
            "prestidigitacao",
        ],

        "proficiencias": [
            (
                "ferramenta",
                "Kit de disfarce"
            ),
            (
                "ferramenta",
                "Kit de falsificação"
            ),
        ],

        "idiomas": 0,
    },

    "Criminoso": {
        "pericias": [
            "enganacao",
            "furtividade",
        ],

        "proficiencias": [
            (
                "jogo",
                "Um kit de jogo à escolha"
            ),
            (
                "ferramenta",
                "Ferramentas de ladrão"
            ),
        ],

        "idiomas": 0,
    },

    "Eremita": {
        "pericias": [
            "medicina",
            "religiao",
        ],

        "proficiencias": [
            (
                "ferramenta",
                "Kit de herbalismo"
            ),
        ],

        "idiomas": 1,
    },

    "Forasteiro": {
        "pericias": [
            "atletismo",
            "sobrevivencia",
        ],

        "proficiencias": [
            (
                "instrumento",
                "Um instrumento musical à escolha"
            ),
        ],

        "idiomas": 1,
    },

    "Herói do Povo": {
        "pericias": [
            "lidar_animais",
            "sobrevivencia",
        ],

        "proficiencias": [
            (
                "ferramenta",
                "Uma ferramenta de artesão à escolha"
            ),
            (
                "veiculo",
                "Veículos terrestres"
            ),
        ],

        "idiomas": 0,
    },

    "Marinheiro": {
        "pericias": [
            "atletismo",
            "percepcao",
        ],

        "proficiencias": [
            (
                "ferramenta",
                "Ferramentas de navegador"
            ),
            (
                "veiculo",
                "Veículos aquáticos"
            ),
        ],

        "idiomas": 0,
    },

    "Nobre": {
        "pericias": [
            "historia",
            "persuasao",
        ],

        "proficiencias": [
            (
                "jogo",
                "Um kit de jogo à escolha"
            ),
        ],

        "idiomas": 1,
    },

    "Órfão": {
        "pericias": [
            "furtividade",
            "prestidigitacao",
        ],

        "proficiencias": [
            (
                "ferramenta",
                "Kit de disfarce"
            ),
            (
                "ferramenta",
                "Ferramentas de ladrão"
            ),
        ],

        "idiomas": 0,
    },

    "Sábio": {
        "pericias": [
            "arcanismo",
            "historia",
        ],

        "proficiencias": [],

        "idiomas": 2,
    },

    "Soldado": {
        "pericias": [
            "atletismo",
            "intimidacao",
        ],

        "proficiencias": [
            (
                "jogo",
                "Um kit de jogo à escolha"
            ),
            (
                "veiculo",
                "Veículos terrestres"
            ),
        ],

        "idiomas": 0,
    },
}


def buscar_antecedente(
    cursor,
    nome
):
    cursor.execute(
        """
        SELECT id
        FROM antecedentes
        WHERE nome = %s;
        """,
        (nome,)
    )

    resultado = cursor.fetchone()

    if resultado is None:
        raise ValueError(
            f"Antecedente não encontrado: {nome}"
        )

    return resultado[0]


def popular_dados_antecedentes():
    conexao = conectar()
    cursor = conexao.cursor()

    try:

        cursor.execute(
            """
            DELETE FROM pericias_antecedentes;
            """
        )

        cursor.execute(
            """
            DELETE FROM proficiencias_antecedentes;
            """
        )

        cursor.execute(
            """
            DELETE FROM idiomas_antecedentes;
            """
        )

        for nome_antecedente, dados in DADOS_ANTECEDENTES.items():

            antecedente_id = buscar_antecedente(
                cursor,
                nome_antecedente
            )

            # =============================================
            # PERÍCIAS
            # =============================================

            for pericia in dados["pericias"]:

                cursor.execute(
                    """
                    INSERT INTO pericias_antecedentes (
                        antecedente_id,
                        pericia
                    )
                    VALUES (%s, %s);
                    """,
                    (
                        antecedente_id,
                        pericia
                    )
                )

            # =============================================
            # PROFICIÊNCIAS
            # =============================================

            for tipo, nome in dados["proficiencias"]:

                cursor.execute(
                    """
                    INSERT INTO proficiencias_antecedentes (
                        antecedente_id,
                        tipo,
                        nome
                    )
                    VALUES (%s, %s, %s);
                    """,
                    (
                        antecedente_id,
                        tipo,
                        nome
                    )
                )

            # =============================================
            # IDIOMAS
            # =============================================

            cursor.execute(
                """
                INSERT INTO idiomas_antecedentes (
                    antecedente_id,
                    quantidade
                )
                VALUES (%s, %s);
                """,
                (
                    antecedente_id,
                    dados["idiomas"]
                )
            )

        conexao.commit()

        print(
            "Dados dos antecedentes "
            "cadastrados com sucesso!"
        )

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


if __name__ == "__main__":
    popular_dados_antecedentes()