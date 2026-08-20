from mini_mestre.database import conectar


RACAS = [
    (
        "Anão",
        "Anões são resistentes, determinados e conhecidos por sua tradição, habilidade artesanal e vida nas montanhas.",
        25,
    ),
    (
        "Elfo",
        "Elfos são ágeis, perceptivos e possuem forte ligação com magia e natureza.",
        30,
    ),
    (
        "Halfling",
        "Halflings são pequenos, ágeis e conhecidos por sua coragem e sorte.",
        25,
    ),
    (
        "Humano",
        "Humanos são versáteis, ambiciosos e encontrados em praticamente todos os lugares.",
        30,
    ),
    (
        "Draconato",
        "Draconatos descendem de dragões e possuem características dracônicas marcantes.",
        30,
    ),
    (
        "Gnomo",
        "Gnomos são pequenos, curiosos, inventivos e possuem grande entusiasmo pela vida.",
        25,
    ),
    (
        "Meio-Elfo",
        "Meio-elfos combinam características humanas e élficas e são naturalmente versáteis.",
        30,
    ),
    (
        "Meio-Orc",
        "Meio-orcs são fortes, resistentes e conhecidos por sua ferocidade em combate.",
        30,
    ),
    (
        "Tiefling",
        "Tieflings possuem uma herança infernal que lhes concede características e poderes incomuns.",
        30,
    ),
]


def popular_racas():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        for nome, descricao, deslocamento in RACAS:
            cursor.execute(
                """
                INSERT INTO racas (
                    nome,
                    descricao,
                    deslocamento
                )
                VALUES (%s, %s, %s)

                ON CONFLICT (nome)
                DO UPDATE SET
                    descricao = EXCLUDED.descricao,
                    deslocamento = EXCLUDED.deslocamento;
                """,
                (
                    nome,
                    descricao,
                    deslocamento,
                ),
            )

        conexao.commit()

        print("Raças cadastradas com sucesso!")

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


if __name__ == "__main__":
    popular_racas()