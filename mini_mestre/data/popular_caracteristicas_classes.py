from mini_mestre.database import conectar


CARACTERISTICAS = {

    "Bárbaro": [
        (1, "Fúria"),
        (1, "Defesa sem Armadura"),
        (2, "Ataque Descuidado"),
        (2, "Sentido de Perigo"),
        (3, "Caminho Primitivo"),
        (4, "Incremento no Valor de Habilidade"),
        (5, "Ataque Extra"),
        (5, "Movimento Rápido"),
        (6, "Característica de Caminho Primitivo"),
        (7, "Instinto Selvagem"),
        (8, "Incremento no Valor de Habilidade"),
        (9, "Crítico Brutal (+1 dado)"),
        (10, "Característica de Caminho Primitivo"),
        (11, "Fúria Implacável"),
        (12, "Incremento no Valor de Habilidade"),
        (13, "Crítico Brutal (+2 dados)"),
        (14, "Característica de Caminho Primitivo"),
        (15, "Fúria Persistente"),
        (16, "Incremento no Valor de Habilidade"),
        (17, "Crítico Brutal (+3 dados)"),
        (18, "Força Indomável"),
        (19, "Incremento no Valor de Habilidade"),
        (20, "Campeão Primitivo"),
    ],

    "Bardo": [
        (1, "Conjuração"),
        (1, "Inspiração de Bardo (d6)"),
        (2, "Versatilidade"),
        (2, "Canção do Descanso (d6)"),
        (3, "Colégio de Bardo"),
        (3, "Aptidão"),
        (4, "Incremento no Valor de Habilidade"),
        (5, "Inspiração de Bardo (d8)"),
        (5, "Fonte de Inspiração"),
        (6, "Habilidade de Colégio de Bardo"),
        (6, "Canção de Proteção"),
        (8, "Incremento no Valor de Habilidade"),
        (9, "Canção do Descanso (d8)"),
        (10, "Inspiração de Bardo (d10)"),
        (10, "Aptidão"),
        (10, "Segredos Mágicos"),
        (12, "Incremento no Valor de Habilidade"),
        (13, "Canção do Descanso (d10)"),
        (14, "Habilidade de Colégio de Bardo"),
        (14, "Segredos Mágicos"),
        (15, "Inspiração de Bardo (d12)"),
        (16, "Incremento no Valor de Habilidade"),
        (17, "Canção do Descanso (d12)"),
        (18, "Segredos Mágicos"),
        (19, "Incremento no Valor de Habilidade"),
        (20, "Inspiração Superior"),
    ],

    "Bruxo": [
        (1, "Patrono Transcendental"),
        (1, "Magia de Pacto"),
        (2, "Invocações Místicas"),
        (3, "Dádiva do Pacto"),
        (4, "Incremento no Valor de Habilidade"),
        (6, "Característica de Patrono Transcendental"),
        (8, "Incremento no Valor de Habilidade"),
        (10, "Característica de Patrono Transcendental"),
        (11, "Arcana Mística (6° nível)"),
        (12, "Incremento no Valor de Habilidade"),
        (13, "Arcana Mística (7° nível)"),
        (14, "Característica de Patrono Transcendental"),
        (15, "Arcana Mística (8° nível)"),
        (16, "Incremento no Valor de Habilidade"),
        (17, "Arcana Mística (9° nível)"),
        (19, "Incremento no Valor de Habilidade"),
        (20, "Mestre Místico"),
    ],

    "Clérigo": [
        (1, "Conjuração"),
        (1, "Domínio Divino"),
        (2, "Canalizar Divindade"),
        (2, "Característica de Domínio Divino"),
        (4, "Incremento no Valor de Habilidade"),
        (5, "Destruir Mortos-Vivos"),
        (6, "Canalizar Divindade Aprimorada"),
        (6, "Característica de Domínio Divino"),
        (8, "Incremento no Valor de Habilidade"),
        (8, "Característica de Domínio Divino"),
        (10, "Intervenção Divina"),
        (11, "Destruir Mortos-Vivos Aprimorado"),
        (12, "Incremento no Valor de Habilidade"),
        (14, "Destruir Mortos-Vivos Aprimorado"),
        (16, "Incremento no Valor de Habilidade"),
        (17, "Característica de Domínio Divino"),
        (18, "Canalizar Divindade Aprimorada"),
        (19, "Incremento no Valor de Habilidade"),
        (20, "Intervenção Divina Aprimorada"),
    ],

    "Druida": [
        (1, "Druídico"),
        (1, "Conjuração"),
        (2, "Forma Selvagem"),
        (2, "Círculo Druídico"),
        (4, "Aprimoramento de Forma Selvagem"),
        (4, "Incremento no Valor de Habilidade"),
        (6, "Característica de Círculo Druídico"),
        (8, "Aprimoramento de Forma Selvagem"),
        (8, "Incremento no Valor de Habilidade"),
        (10, "Característica de Círculo Druídico"),
        (12, "Incremento no Valor de Habilidade"),
        (14, "Característica de Círculo Druídico"),
        (16, "Incremento no Valor de Habilidade"),
        (18, "Corpo Atemporal"),
        (18, "Magias da Besta"),
        (19, "Incremento no Valor de Habilidade"),
        (20, "Arquidruida"),
    ],

    "Feiticeiro": [
        (1, "Conjuração"),
        (1, "Origem de Feitiçaria"),
        (2, "Fonte de Magia"),
        (3, "Metamágica"),
        (4, "Incremento no Valor de Habilidade"),
        (6, "Característica de Origem de Feitiçaria"),
        (8, "Incremento no Valor de Habilidade"),
        (10, "Metamágica"),
        (12, "Incremento no Valor de Habilidade"),
        (14, "Característica de Origem de Feitiçaria"),
        (16, "Incremento no Valor de Habilidade"),
        (17, "Metamágica"),
        (18, "Característica de Origem de Feitiçaria"),
        (19, "Incremento no Valor de Habilidade"),
        (20, "Restauração Mística"),
    ],

    "Guerreiro": [
        (1, "Estilo de Luta"),
        (1, "Retomar o Fôlego"),
        (2, "Surto de Ação"),
        (3, "Arquétipo Marcial"),
        (4, "Incremento no Valor de Habilidade"),
        (5, "Ataque Extra"),
        (6, "Incremento no Valor de Habilidade"),
        (7, "Característica de Arquétipo Marcial"),
        (8, "Incremento no Valor de Habilidade"),
        (9, "Indomável"),
        (10, "Característica de Arquétipo Marcial"),
        (11, "Ataque Extra (2)"),
        (12, "Incremento no Valor de Habilidade"),
        (13, "Indomável (2 usos)"),
        (14, "Incremento no Valor de Habilidade"),
        (15, "Característica de Arquétipo Marcial"),
        (16, "Incremento no Valor de Habilidade"),
        (17, "Surto de Ação (2 usos)"),
        (17, "Indomável (3 usos)"),
        (18, "Característica de Arquétipo Marcial"),
        (19, "Incremento no Valor de Habilidade"),
        (20, "Ataque Extra (3)"),
    ],

    "Ladino": [
        (1, "Especialização"),
        (1, "Ataque Furtivo"),
        (1, "Gíria de Ladrão"),
        (2, "Ação Ardilosa"),
        (3, "Arquétipo de Ladino"),
        (4, "Incremento no Valor de Habilidade"),
        (5, "Esquiva Sobrenatural"),
        (6, "Especialização"),
        (7, "Evasão"),
        (8, "Incremento no Valor de Habilidade"),
        (9, "Característica de Arquétipo de Ladino"),
        (10, "Incremento no Valor de Habilidade"),
        (11, "Talento Confiável"),
        (12, "Incremento no Valor de Habilidade"),
        (13, "Característica de Arquétipo de Ladino"),
        (14, "Sentido Cego"),
        (15, "Mente Escorregadia"),
        (16, "Incremento no Valor de Habilidade"),
        (17, "Característica de Arquétipo de Ladino"),
        (18, "Elusivo"),
        (19, "Incremento no Valor de Habilidade"),
        (20, "Golpe de Sorte"),
    ],

    "Mago": [
        (1, "Conjuração"),
        (1, "Recuperação Arcana"),
        (1, "Grimório"),
        (2, "Tradição Arcana"),
        (4, "Incremento no Valor de Habilidade"),
        (6, "Característica de Tradição Arcana"),
        (8, "Incremento no Valor de Habilidade"),
        (10, "Característica de Tradição Arcana"),
        (12, "Incremento no Valor de Habilidade"),
        (14, "Característica de Tradição Arcana"),
        (16, "Incremento no Valor de Habilidade"),
        (18, "Dominar Magia"),
        (19, "Incremento no Valor de Habilidade"),
        (20, "Assinatura Mágica"),
    ],

    "Monge": [
        (1, "Defesa sem Armadura"),
        (1, "Artes Marciais"),
        (2, "Chi"),
        (2, "Movimento sem Armadura"),
        (3, "Tradição Monástica"),
        (3, "Defletir Projéteis"),
        (4, "Incremento no Valor de Habilidade"),
        (4, "Queda Lenta"),
        (5, "Ataque Extra"),
        (5, "Ataque Atordoante"),
        (6, "Golpes de Chi"),
        (6, "Característica de Tradição Monástica"),
        (7, "Evasão"),
        (7, "Mente Tranquila"),
        (8, "Incremento no Valor de Habilidade"),
        (9, "Aprimoramento de Movimento sem Armadura"),
        (10, "Pureza Corporal"),
        (11, "Característica de Tradição Monástica"),
        (12, "Incremento no Valor de Habilidade"),
        (13, "Idiomas do Sol e da Lua"),
        (14, "Alma de Diamante"),
        (15, "Corpo Atemporal"),
        (16, "Incremento no Valor de Habilidade"),
        (17, "Característica de Tradição Monástica"),
        (18, "Corpo Vazio"),
        (19, "Incremento no Valor de Habilidade"),
        (20, "Auto Aperfeiçoamento"),
    ],

    "Paladino": [
        (1, "Sentido Divino"),
        (1, "Cura pelas Mãos"),
        (2, "Estilo de Luta"),
        (2, "Conjuração"),
        (2, "Destruição Divina"),
        (3, "Saúde Divina"),
        (3, "Juramento Sagrado"),
        (4, "Incremento no Valor de Habilidade"),
        (5, "Ataque Extra"),
        (6, "Aura de Proteção"),
        (7, "Característica de Juramento Sagrado"),
        (8, "Incremento no Valor de Habilidade"),
        (10, "Aura da Coragem"),
        (11, "Destruição Divina Aprimorada"),
        (12, "Incremento no Valor de Habilidade"),
        (14, "Toque Purificador"),
        (15, "Característica de Juramento Sagrado"),
        (16, "Incremento no Valor de Habilidade"),
        (18, "Aprimoramentos de Aura"),
        (19, "Incremento no Valor de Habilidade"),
        (20, "Característica de Juramento Sagrado"),
    ],

    "Patrulheiro": [
        (1, "Inimigo Favorito"),
        (1, "Explorador Natural"),
        (2, "Estilo de Luta"),
        (2, "Conjuração"),
        (3, "Conclave de Patrulheiro"),
        (3, "Consciência Primitiva"),
        (4, "Incremento no Valor de Habilidade"),
        (5, "Característica de Conclave de Patrulheiro"),
        (6, "Inimigo Favorito Maior"),
        (7, "Característica de Conclave de Patrulheiro"),
        (8, "Incremento no Valor de Habilidade"),
        (8, "Pés Rápidos"),
        (10, "Mimetismo"),
        (11, "Característica de Conclave de Patrulheiro"),
        (12, "Incremento no Valor de Habilidade"),
        (14, "Desaparecer"),
        (15, "Característica de Conclave de Patrulheiro"),
        (16, "Incremento no Valor de Habilidade"),
        (18, "Sentidos Selvagens"),
        (19, "Incremento no Valor de Habilidade"),
        (20, "Matador de Inimigos"),
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


def popular_caracteristicas_classes():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            DELETE FROM caracteristicas_classes;
            """
        )

        for nome_classe, lista in CARACTERISTICAS.items():

            classe_id = buscar_classe(
                cursor,
                nome_classe
            )

            for nivel, nome in lista:

                cursor.execute(
                    """
                    INSERT INTO caracteristicas_classes (
                        classe_id,
                        nivel,
                        nome,
                        descricao
                    )
                    VALUES (%s, %s, %s, NULL);
                    """,
                    (
                        classe_id,
                        nivel,
                        nome
                    )
                )

        conexao.commit()

        print(
            "Progressão das classes cadastrada com sucesso!"
        )

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


if __name__ == "__main__":
    popular_caracteristicas_classes()