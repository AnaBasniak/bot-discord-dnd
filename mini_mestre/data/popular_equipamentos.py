from mini_mestre.database import conectar


EQUIPAMENTOS = [
    # =====================================================
    # ARMADURAS
    # nome, tipo, descricao, ca_base, limite_destreza, bonus_ca
    # =====================================================

    (
        "Armadura de Couro",
        "armadura",
        "Armadura leve de couro.",
        11,
        None,
        0,
    ),
    (
        "Gibão de Peles",
        "armadura",
        "Armadura média feita com peles grossas.",
        12,
        2,
        0,
    ),
    (
        "Brunea",
        "armadura",
        "Armadura média composta por placas metálicas sobrepostas.",
        14,
        2,
        0,
    ),
    (
        "Cota de Malha",
        "armadura",
        "Armadura pesada composta por anéis metálicos entrelaçados.",
        16,
        0,
        0,
    ),
    (
        "Escudo",
        "escudo",
        "Escudo que concede bônus à Classe de Armadura.",
        None,
        None,
        2,
    ),
    (
        "Escudo de Madeira",
        "escudo",
        "Escudo de madeira usado especialmente por druidas.",
        None,
        None,
        2,
    ),

    # =====================================================
    # ARMAS
    # =====================================================

    ("Adaga", "arma", None, None, None, 0),
    ("Arco Curto", "arma", None, None, None, 0),
    ("Arco Longo", "arma", None, None, None, 0),
    ("Azagaia", "arma", None, None, None, 0),
    ("Besta Leve", "arma", None, None, None, 0),
    ("Besta de Mão", "arma", None, None, None, 0),
    ("Bordão", "arma", None, None, None, 0),
    ("Cimitarra", "arma", None, None, None, 0),
    ("Clava", "arma", None, None, None, 0),
    ("Dardo", "arma", None, None, None, 0),
    ("Espada Curta", "arma", None, None, None, 0),
    ("Espada Longa", "arma", None, None, None, 0),
    ("Foice", "arma", None, None, None, 0),
    ("Funda", "arma", None, None, None, 0),
    ("Lança", "arma", None, None, None, 0),
    ("Machadinha", "arma", None, None, None, 0),
    ("Machado de Batalha", "arma", None, None, None, 0),
    ("Machado Grande", "arma", None, None, None, 0),
    ("Maça", "arma", None, None, None, 0),
    ("Martelo Leve", "arma", None, None, None, 0),
    ("Martelo de Guerra", "arma", None, None, None, 0),
    ("Rapieira", "arma", None, None, None, 0),

    # =====================================================
    # MUNIÇÃO
    # =====================================================

    ("Flechas", "municao", None, None, None, 0),
    ("Virotes", "municao", None, None, None, 0),

    # =====================================================
    # FERRAMENTAS / ITENS
    # =====================================================

    ("Ferramentas de Ladrão", "ferramenta", None, None, None, 0),
    ("Kit de Herbalismo", "ferramenta", None, None, None, 0),
    ("Bolsa de Componentes", "foco", None, None, None, 0),

    # =====================================================
    # FOCOS
    # =====================================================

    ("Foco Arcano", "foco", None, None, None, 0),
    ("Foco Druídico", "foco", None, None, None, 0),
    ("Símbolo Sagrado", "foco", None, None, None, 0),

    # =====================================================
    # LIVROS
    # =====================================================

    ("Livro de Magias", "livro", None, None, None, 0),

    # =====================================================
    # INSTRUMENTOS
    # =====================================================

    ("Lute", "instrumento", None, None, None, 0),
    ("Instrumento Musical", "instrumento", None, None, None, 0),

    # =====================================================
    # RECIPIENTES
    # =====================================================

    ("Aljava", "recipiente", None, None, None, 0),

    # =====================================================
    # PACOTES
    # =====================================================

    ("Pacote de Aventureiro", "pacote", None, None, None, 0),
    ("Pacote de Assaltante", "pacote", None, None, None, 0),
    ("Pacote de Artista", "pacote", None, None, None, 0),
    ("Pacote de Diplomata", "pacote", None, None, None, 0),
    ("Pacote de Estudioso", "pacote", None, None, None, 0),
    ("Pacote de Explorador", "pacote", None, None, None, 0),
    ("Pacote de Sacerdote", "pacote", None, None, None, 0),
]


def popular_equipamentos():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        for (
            nome,
            tipo,
            descricao,
            ca_base,
            limite_destreza,
            bonus_ca,
        ) in EQUIPAMENTOS:

            cursor.execute(
                """
                INSERT INTO equipamentos (
                    nome,
                    tipo,
                    descricao,
                    ca_base,
                    limite_destreza,
                    bonus_ca
                )
                VALUES (%s, %s, %s, %s, %s, %s)

                ON CONFLICT (nome)
                DO UPDATE SET
                    tipo = EXCLUDED.tipo,
                    descricao = EXCLUDED.descricao,
                    ca_base = EXCLUDED.ca_base,
                    limite_destreza = EXCLUDED.limite_destreza,
                    bonus_ca = EXCLUDED.bonus_ca;
                """,
                (
                    nome,
                    tipo,
                    descricao,
                    ca_base,
                    limite_destreza,
                    bonus_ca,
                )
            )

        conexao.commit()

        print(
            "Equipamentos cadastrados com sucesso!"
        )

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


if __name__ == "__main__":
    popular_equipamentos()