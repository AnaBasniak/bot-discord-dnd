from mini_mestre.database import conectar


PROFICIENCIAS = {
    "Bárbaro": {
        "armadura": [
            "Armaduras leves",
            "Armaduras médias",
            "Escudos",
        ],

        "arma": [
            "Armas simples",
            "Armas marciais",
        ],

        "ferramenta": [],
    },

    "Bardo": {
        "armadura": [
            "Armaduras leves",
        ],

        "arma": [
            "Armas simples",
            "Bestas de mão",
            "Espadas longas",
            "Rapieiras",
            "Espadas curtas",
        ],

        "ferramenta": [
            "Três instrumentos musicais à escolha",
        ],
    },

    "Bruxo": {
        "armadura": [
            "Armaduras leves",
        ],

        "arma": [
            "Armas simples",
        ],

        "ferramenta": [],
    },

    "Clérigo": {
        "armadura": [
            "Armaduras leves",
            "Armaduras médias",
            "Escudos",
        ],

        "arma": [
            "Armas simples",
        ],

        "ferramenta": [],
    },

    "Druida": {
        "armadura": [
            "Armaduras leves",
            "Armaduras médias",
            "Escudos",
        ],

        "arma": [
            "Clavas",
            "Adagas",
            "Dardos",
            "Azagaias",
            "Maças",
            "Bordões",
            "Cimitarras",
            "Foices",
            "Fundas",
            "Lanças",
        ],

        "ferramenta": [
            "Kit de herbalismo",
        ],
    },

    "Feiticeiro": {
        "armadura": [],

        "arma": [
            "Adagas",
            "Dardos",
            "Fundas",
            "Bordões",
            "Bestas leves",
        ],

        "ferramenta": [],
    },

    "Guerreiro": {
        "armadura": [
            "Todas as armaduras",
            "Escudos",
        ],

        "arma": [
            "Armas simples",
            "Armas marciais",
        ],

        "ferramenta": [],
    },

    "Ladino": {
        "armadura": [
            "Armaduras leves",
        ],

        "arma": [
            "Armas simples",
            "Bestas de mão",
            "Espadas longas",
            "Rapieiras",
            "Espadas curtas",
        ],

        "ferramenta": [
            "Ferramentas de ladrão",
        ],
    },

    "Mago": {
        "armadura": [],

        "arma": [
            "Adagas",
            "Dardos",
            "Fundas",
            "Bordões",
            "Bestas leves",
        ],

        "ferramenta": [],
    },

    "Monge": {
        "armadura": [],

        "arma": [
            "Armas simples",
            "Espadas curtas",
        ],

        "ferramenta": [
            "Uma ferramenta de artesão ou instrumento musical à escolha",
        ],
    },

    "Paladino": {
        "armadura": [
            "Todas as armaduras",
            "Escudos",
        ],

        "arma": [
            "Armas simples",
            "Armas marciais",
        ],

        "ferramenta": [],
    },

    "Patrulheiro": {
        "armadura": [
            "Armaduras leves",
            "Armaduras médias",
            "Escudos",
        ],

        "arma": [
            "Armas simples",
            "Armas marciais",
        ],

        "ferramenta": [],
    },
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


def popular_proficiencias_classes():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            DELETE FROM proficiencias_classes;
            """
        )

        for nome_classe, grupos in PROFICIENCIAS.items():

            classe_id = buscar_classe(
                cursor,
                nome_classe
            )

            for tipo, nomes in grupos.items():

                for nome in nomes:

                    cursor.execute(
                        """
                        INSERT INTO proficiencias_classes (
                            classe_id,
                            tipo,
                            nome
                        )
                        VALUES (%s, %s, %s);
                        """,
                        (
                            classe_id,
                            tipo,
                            nome
                        )
                    )

        conexao.commit()

        print(
            "Proficiências das classes "
            "cadastradas com sucesso!"
        )

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


if __name__ == "__main__":
    popular_proficiencias_classes()