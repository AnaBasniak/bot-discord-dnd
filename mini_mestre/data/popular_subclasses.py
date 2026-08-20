from mini_mestre.database import conectar


SUBCLASSES = {
    "Bárbaro": [
        ("Caminho do Berserker", 3),
        ("Caminho do Guerreiro Totêmico", 3),
    ],

    "Bardo": [
        ("Colégio do Conhecimento", 3),
        ("Colégio da Bravura", 3),
    ],

    "Bruxo": [
        ("Arquifada", 1),
        ("Corruptor", 1),
        ("Grande Antigo", 1),
    ],

    "Clérigo": [
        ("Domínio do Conhecimento", 1),
        ("Domínio da Guerra", 1),
        ("Domínio da Luz", 1),
        ("Domínio da Natureza", 1),
        ("Domínio da Tempestade", 1),
        ("Domínio da Trapaça", 1),
        ("Domínio da Vida", 1),
    ],

    "Druida": [
        ("Círculo da Terra", 2),
        ("Círculo da Lua", 2),
    ],

    "Feiticeiro": [
        ("Linhagem Dracônica", 1),
        ("Magia Selvagem", 1),
    ],

    "Guerreiro": [
        ("Campeão", 3),
        ("Mestre de Batalha", 3),
        ("Cavaleiro Arcano", 3),
    ],

    "Ladino": [
        ("Assassino", 3),
        ("Ladrão", 3),
        ("Trapaceiro Arcano", 3),
    ],

    "Mago": [
        ("Escola de Abjuração", 2),
        ("Escola de Adivinhação", 2),
        ("Escola de Conjuração", 2),
        ("Escola de Encantamento", 2),
        ("Escola de Evocação", 2),
        ("Escola de Ilusão", 2),
        ("Escola de Necromancia", 2),
        ("Escola de Transmutação", 2),
    ],

    "Monge": [
        ("Caminho da Mão Aberta", 3),
        ("Caminho da Sombra", 3),
        ("Caminho dos Quatro Elementos", 3),
    ],

    "Paladino": [
        ("Juramento de Devoção", 3),
        ("Juramento dos Anciões", 3),
        ("Juramento de Vingança", 3),
    ],

    "Patrulheiro": [
        ("Conclave do Caçador", 3),
        ("Conclave do Mestre das Bestas", 3),
    ],
}


def buscar_classe(cursor, nome):
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


def popular_subclasses():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        for nome_classe, subclasses in SUBCLASSES.items():

            classe_id = buscar_classe(
                cursor,
                nome_classe
            )

            for nome, nivel_escolha in subclasses:

                cursor.execute(
                    """
                    INSERT INTO subclasses (
                        classe_id,
                        nome,
                        descricao,
                        nivel_escolha
                    )
                    VALUES (%s, %s, NULL, %s)

                    ON CONFLICT (classe_id, nome)
                    DO UPDATE SET
                        nivel_escolha =
                            EXCLUDED.nivel_escolha;
                    """,
                    (
                        classe_id,
                        nome,
                        nivel_escolha
                    )
                )

        conexao.commit()

        print(
            "Subclasses cadastradas com sucesso!"
        )

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


if __name__ == "__main__":
    popular_subclasses()