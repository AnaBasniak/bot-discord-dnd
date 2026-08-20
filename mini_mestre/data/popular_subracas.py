from mini_mestre.database import conectar


SUBRACAS = {
    "Anão": [
        (
            "Anão da Colina",
            "Anões da Colina possuem sentidos aguçados, grande resistência e profunda intuição.",
        ),
        (
            "Anão da Montanha",
            "Anões da Montanha são fortes e acostumados a uma vida difícil em terrenos montanhosos.",
        ),
    ],

    "Elfo": [
        (
            "Alto Elfo",
            "Altos elfos possuem mente aguçada e domínio natural de formas básicas de magia.",
        ),
        (
            "Elfo da Floresta",
            "Elfos da Floresta são rápidos, furtivos e possuem forte ligação com ambientes naturais.",
        ),
        (
            "Drow",
            "Drow são elfos associados ao Subterrâneo e possuem capacidades mágicas próprias.",
        ),
    ],

    "Halfling": [
        (
            "Pés-Leves",
            "Halflings Pés-Leves são discretos, sociáveis e naturalmente furtivos.",
        ),
        (
            "Robusto",
            "Halflings Robustos possuem resistência acima do comum e grande vigor.",
        ),
    ],

    "Gnomo": [
        (
            "Gnomo da Floresta",
            "Gnomos da Floresta possuem talento natural para ilusões e afinidade com pequenos animais.",
        ),
        (
            "Gnomo das Rochas",
            "Gnomos das Rochas são inventivos e possuem grande conhecimento sobre mecanismos e objetos.",
        ),
    ],
}


def popular_subracas():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        for nome_raca, subracas in SUBRACAS.items():

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
                    f"AVISO: raça '{nome_raca}' não encontrada. "
                    "Execute popular_racas primeiro."
                )
                continue

            raca_id = resultado[0]

            for nome, descricao in subracas:
                cursor.execute(
                    """
                    INSERT INTO subracas (
                        raca_id,
                        nome,
                        descricao
                    )
                    VALUES (%s, %s, %s)

                    ON CONFLICT (raca_id, nome)
                    DO UPDATE SET
                        descricao = EXCLUDED.descricao;
                    """,
                    (
                        raca_id,
                        nome,
                        descricao,
                    ),
                )

        conexao.commit()

        print("Sub-raças cadastradas com sucesso!")

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


if __name__ == "__main__":
    popular_subracas()