from mini_mestre.database import conectar


CARACTERISTICAS_RACAS = {
    "Anão": [
        (
            "Visão no Escuro",
            "Acostumado à vida subterrânea, você enxerga no escuro a até 18 metros."
        ),
        (
            "Resiliência Anã",
            "Você possui vantagem em testes de resistência contra veneno e resistência contra dano de veneno."
        ),
        (
            "Treinamento Anão em Combate",
            "Você possui proficiência com machado de batalha, machadinha, martelo leve e martelo de guerra."
        ),
        (
            "Especialização em Rochas",
            "Você possui conhecimento especial relacionado à origem de trabalhos em pedra."
        ),
    ],

    "Elfo": [
        (
            "Visão no Escuro",
            "Você enxerga no escuro a até 18 metros."
        ),
        (
            "Sentidos Aguçados",
            "Você possui proficiência na perícia Percepção."
        ),
        (
            "Ancestral Feérico",
            "Você possui vantagem contra ser enfeitiçado e magia não pode colocá-lo para dormir."
        ),
        (
            "Transe",
            "Elfos não precisam dormir e meditam profundamente durante cerca de quatro horas por dia."
        ),
    ],

    "Halfling": [
        (
            "Sortudo",
            "Quando você obtém 1 natural em determinados testes com d20, pode jogar o dado novamente."
        ),
        (
            "Bravura",
            "Você possui vantagem em testes de resistência contra ficar amedrontado."
        ),
        (
            "Agilidade Halfling",
            "Você pode mover-se através do espaço de criaturas maiores que você."
        ),
    ],

    "Humano": [
        (
            "Versatilidade Humana",
            "Humanos possuem grande capacidade de adaptação e recebem melhoria em todos os atributos."
        ),
    ],

    "Draconato": [
        (
            "Ancestral Dracônico",
            "Você possui uma ancestralidade ligada a uma espécie de dragão."
        ),
        (
            "Arma de Sopro",
            "Você pode usar sua ação para liberar energia destrutiva associada à sua ancestralidade dracônica."
        ),
        (
            "Resistência a Dano",
            "Sua ancestralidade dracônica concede resistência a um tipo de dano."
        ),
    ],

    "Gnomo": [
        (
            "Visão no Escuro",
            "Você enxerga no escuro a até 18 metros."
        ),
        (
            "Esperteza Gnômica",
            "Você possui vantagem em determinados testes de resistência mentais contra magia."
        ),
    ],

    "Meio-Elfo": [
        (
            "Visão no Escuro",
            "Sua herança élfica permite enxergar no escuro a até 18 metros."
        ),
        (
            "Ancestral Feérico",
            "Você possui vantagem contra ser enfeitiçado e magia não pode colocá-lo para dormir."
        ),
        (
            "Versatilidade em Perícias",
            "Você adquire proficiência em duas perícias à sua escolha."
        ),
    ],

    "Meio-Orc": [
        (
            "Visão no Escuro",
            "Você enxerga no escuro a até 18 metros."
        ),
        (
            "Ameaçador",
            "Você possui proficiência na perícia Intimidação."
        ),
        (
            "Resistência Implacável",
            "Quando seria reduzido a 0 pontos de vida sem morrer imediatamente, pode permanecer com 1 ponto de vida, respeitando o limite de uso da característica."
        ),
        (
            "Ataques Selvagens",
            "Seus acertos críticos com armas corpo a corpo podem causar dano adicional."
        ),
    ],

    "Tiefling": [
        (
            "Visão no Escuro",
            "Sua herança infernal permite enxergar no escuro a até 18 metros."
        ),
        (
            "Resistência Infernal",
            "Você possui resistência a dano de fogo."
        ),
        (
            "Legado Infernal",
            "Sua herança concede capacidades mágicas conforme seu nível aumenta."
        ),
    ],
}


CARACTERISTICAS_SUBRACAS = {
    "Anão da Colina": [
        (
            "Tenacidade Anã",
            "Seu máximo de pontos de vida aumenta e continua aumentando conforme você ganha níveis."
        ),
    ],

    "Anão da Montanha": [
        (
            "Treinamento Anão com Armaduras",
            "Você possui proficiência com armaduras leves e médias."
        ),
    ],

    "Alto Elfo": [
        (
            "Treinamento Élfico com Armas",
            "Você possui treinamento com armas tradicionais élficas."
        ),
        (
            "Truque",
            "Você conhece um truque da lista de magias de mago."
        ),
        (
            "Idioma Adicional",
            "Você pode falar, ler e escrever um idioma adicional."
        ),
    ],

    "Elfo da Floresta": [
        (
            "Treinamento Élfico com Armas",
            "Você possui treinamento com armas tradicionais élficas."
        ),
        (
            "Pés Ligeiros",
            "Seu deslocamento base aumenta."
        ),
        (
            "Máscara da Natureza",
            "Você possui capacidade especial de se esconder em fenômenos naturais."
        ),
    ],

    "Drow": [
        (
            "Visão no Escuro Superior",
            "Seu alcance de visão no escuro é superior ao da maioria dos elfos."
        ),
        (
            "Sensibilidade à Luz Solar",
            "A luz solar direta pode prejudicar determinadas jogadas de ataque e testes de percepção visual."
        ),
        (
            "Magia Drow",
            "Sua herança drow concede capacidades mágicas conforme seu nível aumenta."
        ),
        (
            "Treinamento Drow com Armas",
            "Você possui proficiência com determinadas armas tradicionais dos drow."
        ),
    ],

    "Pés-Leves": [
        (
            "Furtividade Natural",
            "Você pode tentar esconder-se mesmo quando estiver obscurecido apenas por uma criatura maior."
        ),
    ],

    "Robusto": [
        (
            "Resiliência dos Robustos",
            "Você possui resistência adicional contra venenos."
        ),
    ],

    "Gnomo da Floresta": [
        (
            "Ilusionista Nato",
            "Você conhece um truque de ilusão."
        ),
        (
            "Falar com Animais Pequenos",
            "Você consegue comunicar ideias simples a pequenos animais."
        ),
    ],

    "Gnomo das Rochas": [
        (
            "Conhecimento de Artífice",
            "Você possui conhecimento especializado relacionado a objetos mágicos, alquímicos e tecnológicos."
        ),
        (
            "Engenhoqueiro",
            "Você pode construir pequenos dispositivos mecânicos."
        ),
    ],
}


def inserir_caracteristica_raca(
    cursor,
    nome_raca,
    nome,
    descricao
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
        INSERT INTO caracteristicas_raciais (
            raca_id,
            subraca_id,
            nome,
            descricao
        )
        VALUES (%s, NULL, %s, %s);
        """,
        (
            raca_id,
            nome,
            descricao
        )
    )


def inserir_caracteristica_subraca(
    cursor,
    nome_subraca,
    nome,
    descricao
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
        INSERT INTO caracteristicas_raciais (
            raca_id,
            subraca_id,
            nome,
            descricao
        )
        VALUES (NULL, %s, %s, %s);
        """,
        (
            subraca_id,
            nome,
            descricao
        )
    )


def popular_caracteristicas_raciais():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        # Evita duplicação se o script for executado novamente.
        cursor.execute(
            """
            DELETE FROM caracteristicas_raciais;
            """
        )

        for nome_raca, caracteristicas in CARACTERISTICAS_RACAS.items():
            for nome, descricao in caracteristicas:
                inserir_caracteristica_raca(
                    cursor,
                    nome_raca,
                    nome,
                    descricao
                )

        for nome_subraca, caracteristicas in CARACTERISTICAS_SUBRACAS.items():
            for nome, descricao in caracteristicas:
                inserir_caracteristica_subraca(
                    cursor,
                    nome_subraca,
                    nome,
                    descricao
                )

        conexao.commit()

        print(
            "Características raciais cadastradas com sucesso!"
        )

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


if __name__ == "__main__":
    popular_caracteristicas_raciais()