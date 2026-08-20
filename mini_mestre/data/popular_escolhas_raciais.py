from mini_mestre.database import conectar


ESCOLHAS_RACAS = {
    "Anão": [
        (
            "ferramenta_anao",
            "Escolha uma proficiência com ferramenta de artesão",
            1
        ),
    ],

    "Meio-Elfo": [
        (
            "atributo",
            "Escolha dois atributos diferentes para receber +1",
            2
        ),
        (
            "pericia",
            "Escolha duas perícias",
            2
        ),
    ],

    "Draconato": [
        (
            "ancestralidade_draconica",
            "Escolha sua ancestralidade dracônica",
            1
        ),
    ],
}


ESCOLHAS_SUBRACAS = {
    "Alto Elfo": [
        (
            "truque_mago",
            "Escolha um truque da lista de magias de Mago",
            1
        ),
        (
            "idioma",
            "Escolha um idioma adicional",
            1
        ),
    ],
}


def inserir_escolha_raca(
    cursor,
    nome_raca,
    tipo,
    titulo,
    quantidade
):
    cursor.execute(
        """
        SELECT id
        FROM racas
        WHERE nome = %s;
        """,
        (nome_raca,)
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
        INSERT INTO escolhas_raciais (
            raca_id,
            subraca_id,
            tipo,
            titulo,
            quantidade
        )
        VALUES (%s, NULL, %s, %s, %s);
        """,
        (
            raca_id,
            tipo,
            titulo,
            quantidade
        )
    )


def inserir_escolha_subraca(
    cursor,
    nome_subraca,
    tipo,
    titulo,
    quantidade
):
    cursor.execute(
        """
        SELECT id
        FROM subracas
        WHERE nome = %s;
        """,
        (nome_subraca,)
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
        INSERT INTO escolhas_raciais (
            raca_id,
            subraca_id,
            tipo,
            titulo,
            quantidade
        )
        VALUES (NULL, %s, %s, %s, %s);
        """,
        (
            subraca_id,
            tipo,
            titulo,
            quantidade
        )
    )


def popular_escolhas_raciais():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            DELETE FROM escolhas_raciais;
            """
        )

        for nome_raca, escolhas in ESCOLHAS_RACAS.items():

            for tipo, titulo, quantidade in escolhas:

                inserir_escolha_raca(
                    cursor,
                    nome_raca,
                    tipo,
                    titulo,
                    quantidade
                )

        for nome_subraca, escolhas in ESCOLHAS_SUBRACAS.items():

            for tipo, titulo, quantidade in escolhas:

                inserir_escolha_subraca(
                    cursor,
                    nome_subraca,
                    tipo,
                    titulo,
                    quantidade
                )

        conexao.commit()

        print(
            "Escolhas raciais cadastradas com sucesso!"
        )

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


if __name__ == "__main__":
    popular_escolhas_raciais()