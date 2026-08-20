from mini_mestre.database import conectar


ANTECEDENTES = [
    (
        "Acólito",
        "Você passou sua vida a serviço de um templo, igreja ou organização religiosa."
    ),
    (
        "Artesão de Guilda",
        "Você aprendeu um ofício e pertence a uma guilda de artesãos ou comerciantes."
    ),
    (
        "Artista",
        "Você vive de apresentações, música, dança, atuação ou outras formas de entretenimento."
    ),
    (
        "Charlatão",
        "Você sabe manipular pessoas, criar histórias falsas e assumir identidades."
    ),
    (
        "Criminoso",
        "Você possui experiência com o submundo do crime e mantém contatos nesse meio."
    ),
    (
        "Eremita",
        "Você viveu afastado da sociedade em isolamento, contemplação ou busca espiritual."
    ),
    (
        "Forasteiro",
        "Você cresceu longe das cidades e possui grande experiência em sobrevivência."
    ),
    (
        "Herói do Povo",
        "Você veio de uma origem humilde e ganhou a confiança das pessoas comuns."
    ),
    (
        "Marinheiro",
        "Você passou parte de sua vida navegando e trabalhando a bordo de embarcações."
    ),
    (
        "Nobre",
        "Você nasceu em uma família de posição social elevada ou foi criado entre a elite."
    ),
    (
        "Órfão",
        "Você cresceu nas ruas e aprendeu a sobreviver utilizando esperteza e agilidade."
    ),
    (
        "Sábio",
        "Você passou anos estudando e acumulando conhecimento sobre diferentes assuntos."
    ),
    (
        "Soldado",
        "Você recebeu treinamento militar e participou de uma organização ou força armada."
    ),
]


def popular_antecedentes():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        for nome, descricao in ANTECEDENTES:

            cursor.execute(
                """
                INSERT INTO antecedentes (
                    nome,
                    descricao
                )
                VALUES (%s, %s)

                ON CONFLICT (nome)
                DO UPDATE SET
                    descricao = EXCLUDED.descricao;
                """,
                (
                    nome,
                    descricao
                )
            )

        conexao.commit()

        print(
            "Antecedentes cadastrados com sucesso!"
        )

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


if __name__ == "__main__":
    popular_antecedentes()