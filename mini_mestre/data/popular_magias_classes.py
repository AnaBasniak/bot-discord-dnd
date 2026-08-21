from mini_mestre.database import conectar
from mini_mestre.data.popular_magias import LISTAS_MAGIAS


# =========================================================
# RELAÇÃO COMPLETA MAGIA <-> CLASSE
# =========================================================


def buscar_classe_id(cursor, nome_classe):
    cursor.execute(
        """
        SELECT id
        FROM classes
        WHERE nome = %s;
        """,
        (nome_classe,)
    )

    resultado = cursor.fetchone()

    if resultado is None:
        raise ValueError(
            f"Classe não encontrada: {nome_classe}"
        )

    return resultado[0]


def buscar_magia_id(cursor, nome_magia):
    cursor.execute(
        """
        SELECT id
        FROM magias
        WHERE LOWER(nome) = LOWER(%s);
        """,
        (nome_magia,)
    )

    resultado = cursor.fetchone()

    if resultado is None:
        raise ValueError(
            f"Magia não encontrada: {nome_magia}"
        )

    return resultado[0]


def popular_magias_classes():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        total_relacoes = 0

        for nome_classe, niveis in LISTAS_MAGIAS.items():
            classe_id = buscar_classe_id(
                cursor,
                nome_classe
            )

            for magias in niveis.values():
                for nome_magia, _escola, _ritual in magias:
                    magia_id = buscar_magia_id(
                        cursor,
                        nome_magia
                    )

                    cursor.execute(
                        """
                        INSERT INTO magias_classes (
                            magia_id,
                            classe_id
                        )
                        VALUES (%s, %s)

                        ON CONFLICT (
                            magia_id,
                            classe_id
                        )
                        DO NOTHING;
                        """,
                        (
                            magia_id,
                            classe_id
                        )
                    )

                    total_relacoes += 1

        conexao.commit()

        print(
            f"{total_relacoes} relações magia/classe "
            "processadas com sucesso!"
        )

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


if __name__ == "__main__":
    popular_magias_classes()