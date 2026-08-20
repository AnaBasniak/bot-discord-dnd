from mini_mestre.database import conectar


CLASSES = [
    (
        "Bárbaro",
        "Um guerreiro feroz que utiliza força, resistência e fúria em combate.",
        12,
        2,
    ),
    (
        "Bardo",
        "Um artista versátil que utiliza música, conhecimento e magia.",
        8,
        3,
    ),
    (
        "Bruxo",
        "Um conjurador que recebe poder através de um pacto com uma entidade sobrenatural.",
        8,
        2,
    ),
    (
        "Clérigo",
        "Um conjurador divino que recebe poder de sua fé e divindade.",
        8,
        2,
    ),
    (
        "Druida",
        "Um guardião da natureza capaz de conjurar magia e assumir formas animais.",
        8,
        2,
    ),
    (
        "Feiticeiro",
        "Um conjurador cujo poder mágico surge de sua própria origem sobrenatural.",
        6,
        2,
    ),
    (
        "Guerreiro",
        "Um combatente especializado em armas, armaduras e técnicas de batalha.",
        10,
        2,
    ),
    (
        "Ladino",
        "Um especialista em furtividade, perícias e ataques precisos.",
        8,
        4,
    ),
    (
        "Mago",
        "Um estudioso da magia arcana que registra suas magias em um grimório.",
        6,
        2,
    ),
    (
        "Monge",
        "Um combatente disciplinado que utiliza artes marciais e energia espiritual.",
        8,
        2,
    ),
    (
        "Paladino",
        "Um guerreiro sagrado que combina combate, cura e poderes divinos.",
        10,
        2,
    ),
    (
        "Patrulheiro",
        "Um explorador e guerreiro especializado em sobrevivência e caça.",
        10,
        3,
    ),
]


def popular_classes():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        for (
            nome,
            descricao,
            dado_vida,
            quantidade_pericias
        ) in CLASSES:

            cursor.execute(
                """
                INSERT INTO classes (
                    nome,
                    descricao,
                    dado_vida,
                    nivel_maximo,
                    quantidade_pericias
                )
                VALUES (%s, %s, %s, 20, %s)

                ON CONFLICT (nome)
                DO UPDATE SET
                    descricao = EXCLUDED.descricao,
                    dado_vida = EXCLUDED.dado_vida,
                    quantidade_pericias =
                        EXCLUDED.quantidade_pericias;
                """,
                (
                    nome,
                    descricao,
                    dado_vida,
                    quantidade_pericias,
                )
            )

        conexao.commit()

        print("Classes cadastradas com sucesso!")

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


if __name__ == "__main__":
    popular_classes()