from mini_mestre.database import conectar

# =========================================================
# PROGRESSÃO DE ESPAÇOS DE MAGIA
# Fonte: tabelas de classe do Livro do Jogador do projeto.
# =========================================================

CONJURADORES_COMPLETOS = [
    "Bardo",
    "Clérigo",
    "Druida",
    "Feiticeiro",
    "Mago",
]

ESPACOS_COMPLETOS = {
    1: [2, 0, 0, 0, 0, 0, 0, 0, 0],
    2: [3, 0, 0, 0, 0, 0, 0, 0, 0],
    3: [4, 2, 0, 0, 0, 0, 0, 0, 0],
    4: [4, 3, 0, 0, 0, 0, 0, 0, 0],
    5: [4, 3, 2, 0, 0, 0, 0, 0, 0],
    6: [4, 3, 3, 0, 0, 0, 0, 0, 0],
    7: [4, 3, 3, 1, 0, 0, 0, 0, 0],
    8: [4, 3, 3, 2, 0, 0, 0, 0, 0],
    9: [4, 3, 3, 3, 1, 0, 0, 0, 0],
    10: [4, 3, 3, 3, 2, 0, 0, 0, 0],
    11: [4, 3, 3, 3, 2, 1, 0, 0, 0],
    12: [4, 3, 3, 3, 2, 1, 0, 0, 0],
    13: [4, 3, 3, 3, 2, 1, 1, 0, 0],
    14: [4, 3, 3, 3, 2, 1, 1, 0, 0],
    15: [4, 3, 3, 3, 2, 1, 1, 1, 0],
    16: [4, 3, 3, 3, 2, 1, 1, 1, 0],
    17: [4, 3, 3, 3, 2, 1, 1, 1, 1],
    18: [4, 3, 3, 3, 3, 1, 1, 1, 1],
    19: [4, 3, 3, 3, 3, 2, 1, 1, 1],
    20: [4, 3, 3, 3, 3, 2, 2, 1, 1],
}

ESPACOS_PALADINO = {
    1: [0, 0, 0, 0, 0],
    2: [2, 0, 0, 0, 0],
    3: [3, 0, 0, 0, 0],
    4: [3, 0, 0, 0, 0],
    5: [4, 2, 0, 0, 0],
    6: [4, 2, 0, 0, 0],
    7: [4, 3, 0, 0, 0],
    8: [4, 3, 0, 0, 0],
    9: [4, 3, 2, 0, 0],
    10: [4, 3, 2, 0, 0],
    11: [4, 3, 3, 0, 0],
    12: [4, 3, 3, 0, 0],
    13: [4, 3, 3, 1, 0],
    14: [4, 3, 3, 1, 0],
    15: [4, 3, 3, 2, 0],
    16: [4, 3, 3, 2, 0],
    17: [4, 3, 3, 3, 1],
    18: [4, 3, 3, 3, 1],
    19: [4, 3, 3, 3, 2],
    20: [4, 3, 3, 3, 2],
}

ESPACOS_PATRULHEIRO = {
    1: [0, 0, 0, 0, 0],
    2: [2, 0, 0, 0, 0],
    3: [3, 0, 0, 0, 0],
    4: [3, 0, 0, 0, 0],
    5: [4, 2, 0, 0, 0],
    6: [4, 2, 0, 0, 0],
    7: [4, 3, 0, 0, 0],
    8: [4, 3, 0, 0, 0],
    9: [4, 3, 2, 0, 0],
    10: [4, 3, 2, 0, 0],
    11: [4, 3, 3, 0, 0],
    12: [4, 3, 3, 0, 0],
    13: [4, 3, 3, 1, 0],
    14: [4, 3, 3, 1, 0],
    15: [4, 3, 3, 2, 0],
    16: [4, 3, 3, 2, 0],
    17: [4, 3, 3, 3, 1],
    18: [4, 3, 3, 3, 1],
    19: [4, 3, 3, 3, 2],
    20: [4, 3, 3, 3, 2],
}

PACTO_BRUXO = {
    1: (1, 1),
    2: (1, 2),
    3: (2, 2),
    4: (2, 2),
    5: (3, 2),
    6: (3, 2),
    7: (4, 2),
    8: (4, 2),
    9: (5, 2),
    10: (5, 2),
    11: (5, 3),
    12: (5, 3),
    13: (5, 3),
    14: (5, 3),
    15: (5, 3),
    16: (5, 3),
    17: (5, 4),
    18: (5, 4),
    19: (5, 4),
    20: (5, 4),
}

ARCANA_MISTICA_BRUXO = {
    11: 6,
    13: 7,
    15: 8,
    17: 9,
}


def buscar_classe_id(cursor, nome):
    cursor.execute(
        "SELECT id FROM classes WHERE nome = %s;",
        (nome,)
    )
    resultado = cursor.fetchone()

    if resultado is None:
        raise ValueError(
            f"Classe não encontrada: {nome}"
        )

    return resultado[0]


def _inserir_progressao_normal(
    cursor,
    classe_id,
    progressao
):
    for nivel_classe, quantidades in progressao.items():
        for indice, quantidade in enumerate(
            quantidades,
            start=1
        ):
            if quantidade <= 0:
                continue

            cursor.execute(
                '''
                INSERT INTO slots_magia_classes (
                    classe_id,
                    nivel_classe,
                    nivel_magia,
                    quantidade
                )
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (
                    classe_id,
                    nivel_classe,
                    nivel_magia
                )
                DO UPDATE SET
                    quantidade = EXCLUDED.quantidade;
                ''',
                (
                    classe_id,
                    nivel_classe,
                    indice,
                    quantidade,
                )
            )


def popular_slots_magia():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        # Evita resíduos de versões anteriores.
        cursor.execute(
            "DELETE FROM slots_magia_classes;"
        )

        for nome_classe in CONJURADORES_COMPLETOS:
            classe_id = buscar_classe_id(
                cursor,
                nome_classe
            )
            _inserir_progressao_normal(
                cursor,
                classe_id,
                ESPACOS_COMPLETOS
            )

        classe_id = buscar_classe_id(
            cursor,
            "Paladino"
        )
        _inserir_progressao_normal(
            cursor,
            classe_id,
            ESPACOS_PALADINO
        )

        classe_id = buscar_classe_id(
            cursor,
            "Patrulheiro"
        )
        _inserir_progressao_normal(
            cursor,
            classe_id,
            ESPACOS_PATRULHEIRO
        )

        # Bruxo: todos os espaços de Pacto do nível
        # de classe têm o mesmo nível de magia.
        classe_id = buscar_classe_id(
            cursor,
            "Bruxo"
        )

        for (
            nivel_classe,
            (
                nivel_magia,
                quantidade
            )
        ) in PACTO_BRUXO.items():
            cursor.execute(
                '''
                INSERT INTO slots_magia_classes (
                    classe_id,
                    nivel_classe,
                    nivel_magia,
                    quantidade
                )
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (
                    classe_id,
                    nivel_classe,
                    nivel_magia
                )
                DO UPDATE SET
                    quantidade = EXCLUDED.quantidade;
                ''',
                (
                    classe_id,
                    nivel_classe,
                    nivel_magia,
                    quantidade,
                )
            )

        conexao.commit()

        print(
            "Progressão de espaços de magia "
            "cadastrada com sucesso!"
        )

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


if __name__ == "__main__":
    popular_slots_magia()