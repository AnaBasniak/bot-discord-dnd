from mini_mestre.database import conectar


BONUS_RACAS = {
    "Anão": [
        ("constituicao", 2),
    ],

    "Elfo": [
        ("destreza", 2),
    ],

    "Halfling": [
        ("destreza", 2),
    ],

    "Humano": [
        ("forca", 1),
        ("destreza", 1),
        ("constituicao", 1),
        ("inteligencia", 1),
        ("sabedoria", 1),
        ("carisma", 1),
    ],

    "Draconato": [
        ("forca", 2),
        ("carisma", 1),
    ],

    "Gnomo": [
        ("inteligencia", 2),
    ],

    "Meio-Elfo": [
        ("carisma", 2),
    ],

    "Meio-Orc": [
        ("forca", 2),
        ("constituicao", 1),
    ],

    "Tiefling": [
        ("inteligencia", 1),
        ("carisma", 2),
    ],
}


BONUS_SUBRACAS = {
    "Anão da Colina": [
        ("sabedoria", 1),
    ],

    "Anão da Montanha": [
        ("forca", 2),
    ],

    "Alto Elfo": [
        ("inteligencia", 1),
    ],

    "Elfo da Floresta": [
        ("sabedoria", 1),
    ],

    "Drow": [
        ("carisma", 1),
    ],

    "Pés-Leves": [
        ("carisma", 1),
    ],

    "Robusto": [
        ("constituicao", 1),
    ],

    "Gnomo da Floresta": [
        ("destreza", 1),
    ],

    "Gnomo das Rochas": [
        ("constituicao", 1),
    ],
}


def limpar_bonus(cursor):
    cursor.execute(
        """
        DELETE FROM bonus_atributos_raciais;
        """
    )


def inserir_bonus_raca(
    cursor,
    nome_raca,
    atributo,
    bonus,
):
    cursor.execute(
        """
        SELECT id
        FROM racas
        WHERE nome = %s;
        """,
        (nome_raca,),
    )

    resultado = cursor.fetchone()

    if resultado is None:
        print(
            f"AVISO: raça '{nome_raca}' não encontrada."
        )
        return

    raca_id = resultado[0]

    cursor.execute(
        """
        INSERT INTO bonus_atributos_raciais (
            raca_id,
            subraca_id,
            atributo,
            bonus
        )
        VALUES (%s, NULL, %s, %s);
        """,
        (
            raca_id,
            atributo,
            bonus,
        ),
    )


def inserir_bonus_subraca(
    cursor,
    nome_subraca,
    atributo,
    bonus,
):
    cursor.execute(
        """
        SELECT id
        FROM subracas
        WHERE nome = %s;
        """,
        (nome_subraca,),
    )

    resultado = cursor.fetchone()

    if resultado is None:
        print(
            f"AVISO: sub-raça '{nome_subraca}' não encontrada."
        )
        return

    subraca_id = resultado[0]

    cursor.execute(
        """
        INSERT INTO bonus_atributos_raciais (
            raca_id,
            subraca_id,
            atributo,
            bonus
        )
        VALUES (NULL, %s, %s, %s);
        """,
        (
            subraca_id,
            atributo,
            bonus,
        ),
    )


def popular_bonus_raciais():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        # Essa tabela contém somente dados de referência.
        # Limpamos antes de popular para impedir duplicações.
        limpar_bonus(cursor)

        for nome_raca, bonus_lista in BONUS_RACAS.items():
            for atributo, bonus in bonus_lista:
                inserir_bonus_raca(
                    cursor,
                    nome_raca,
                    atributo,
                    bonus,
                )

        for nome_subraca, bonus_lista in BONUS_SUBRACAS.items():
            for atributo, bonus in bonus_lista:
                inserir_bonus_subraca(
                    cursor,
                    nome_subraca,
                    atributo,
                    bonus,
                )

        conexao.commit()

        print("Bônus raciais cadastrados com sucesso!")

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


if __name__ == "__main__":
    popular_bonus_raciais()