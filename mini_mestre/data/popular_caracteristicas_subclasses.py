from mini_mestre.database import conectar


CARACTERISTICAS = {

    "Caminho do Berserker": [
        (3, "Frenesi"),
        (6, "Fúria Inconsciente"),
        (10, "Presença Intimidante"),
        (14, "Retaliação"),
    ],

    "Caminho do Guerreiro Totêmico": [
        (3, "Conselheiro Espiritual"),
        (3, "Totem Espiritual"),
        (6, "Aspecto da Besta"),
        (10, "Andarilho Espiritual"),
        (14, "Sintonia Totêmica"),
    ],

    "Colégio do Conhecimento": [
        (3, "Proficiência Adicional"),
        (3, "Palavras de Interrupção"),
        (6, "Segredos Mágicos Adicionais"),
        (14, "Perícia Inigualável"),
    ],

    "Colégio da Bravura": [
        (3, "Proficiência Adicional"),
        (3, "Inspiração em Combate"),
        (6, "Ataque Extra"),
        (14, "Magia de Batalha"),
    ],

    "Arquifada": [
        (1, "Presença Feérica"),
        (6, "Névoa de Fuga"),
        (10, "Defesas Sedutoras"),
        (14, "Delírio Sombrio"),
    ],

    "Corruptor": [
        (1, "Bênção do Obscuro"),
        (6, "Sorte do Próprio Obscuro"),
        (10, "Resistência Demoníaca"),
        (14, "Lançar no Inferno"),
    ],

    "Grande Antigo": [
        (1, "Mente Desperta"),
        (6, "Proteção Entrópica"),
        (10, "Escudo de Pensamentos"),
        (14, "Criar Lacaio"),
    ],

    "Domínio do Conhecimento": [
        (1, "Bênçãos do Conhecimento"),
        (2, "Conhecimento das Eras"),
        (6, "Ler Pensamentos"),
        (8, "Conjuração Potente"),
        (17, "Visões do Passado"),
    ],

    "Domínio da Guerra": [
        (1, "Proficiência Adicional"),
        (1, "Sacerdote da Guerra"),
        (2, "Ataque Dirigido"),
        (6, "Bênção do Deus da Guerra"),
        (8, "Ataque Divino"),
        (17, "Avatar da Batalha"),
    ],

    "Domínio da Luz": [
        (1, "Truque Adicional"),
        (1, "Labareda Protetora"),
        (2, "Radiação do Amanhecer"),
        (6, "Labareda Protetora Aprimorada"),
        (8, "Conjuração Potente"),
        (17, "Coroa de Luz"),
    ],

    "Domínio da Natureza": [
        (1, "Acólito da Natureza"),
        (1, "Proficiência Adicional"),
        (2, "Enfeitiçar Animais e Plantas"),
        (6, "Amortecer Elementos"),
        (8, "Ataque Divino"),
        (17, "Mestre da Natureza"),
    ],

    "Domínio da Tempestade": [
        (1, "Proficiência Adicional"),
        (1, "Ira da Tormenta"),
        (2, "Ira Destruidora"),
        (6, "Golpe de Relâmpago"),
        (8, "Ataque Divino"),
        (17, "Filho da Tormenta"),
    ],

    "Domínio da Trapaça": [
        (1, "Bênção do Trapaceiro"),
        (2, "Invocar Duplicidade"),
        (6, "Manto de Sombras"),
        (8, "Ataque Divino"),
        (17, "Duplicidade Aprimorada"),
    ],

    "Domínio da Vida": [
        (1, "Proficiência Adicional"),
        (1, "Discípulo da Vida"),
        (2, "Preservar a Vida"),
        (6, "Curandeiro Abençoado"),
        (8, "Ataque Divino"),
        (17, "Cura Suprema"),
    ],

    "Círculo da Terra": [
        (2, "Truque Adicional"),
        (2, "Recuperação Natural"),
        (3, "Magias de Círculo"),
        (6, "Caminho da Floresta"),
        (10, "Proteção Natural"),
        (14, "Santuário Natural"),
    ],

    "Círculo da Lua": [
        (2, "Forma Selvagem de Combate"),
        (2, "Formas de Círculo"),
        (6, "Ataque Primordial"),
        (10, "Forma Selvagem Elemental"),
        (14, "Mil Formas"),
    ],

    "Linhagem Dracônica": [
        (1, "Ancestral Dracônico"),
        (1, "Resiliência Dracônica"),
        (6, "Afinidade Elemental"),
        (14, "Asas de Dragão"),
        (18, "Presença Dracônica"),
    ],

    "Magia Selvagem": [
        (1, "Surto de Magia Selvagem"),
        (1, "Marés de Caos"),
        (6, "Dobrar a Sorte"),
        (14, "Caos Controlado"),
        (18, "Bombardeio de Magia"),
    ],

    "Campeão": [
        (3, "Crítico Aprimorado"),
        (7, "Atleta Extraordinário"),
        (10, "Estilo de Luta Adicional"),
        (15, "Crítico Superior"),
        (18, "Sobrevivente"),
    ],

    "Mestre de Batalha": [
        (3, "Superioridade em Combate"),
        (3, "Estudioso da Guerra"),
        (7, "Conheça seu Inimigo"),
        (10, "Superioridade em Combate Aprimorada"),
        (15, "Implacável"),
        (18, "Superioridade em Combate Aprimorada"),
    ],

    "Cavaleiro Arcano": [
        (3, "Conjuração"),
        (3, "Vínculo com Arma"),
        (7, "Magia de Guerra"),
        (10, "Golpe Místico"),
        (15, "Investida Arcana"),
        (18, "Magia de Guerra Aprimorada"),
    ],

    "Assassino": [
        (3, "Proficiência Adicional"),
        (3, "Assassinar"),
        (9, "Especialização em Infiltração"),
        (13, "Impostor"),
        (17, "Golpe Letal"),
    ],

    "Ladrão": [
        (3, "Mãos Rápidas"),
        (3, "Andarilho de Telhados"),
        (9, "Furtividade Suprema"),
        (13, "Usar Instrumento Mágico"),
        (17, "Reflexos de Ladrão"),
    ],

    "Trapaceiro Arcano": [
        (3, "Conjuração"),
        (3, "Mãos Mágicas Malabaristas"),
        (9, "Emboscada Mágica"),
        (13, "Trapaceiro Versátil"),
        (17, "Ladrão de Magia"),
    ],

    "Escola de Abjuração": [
        (2, "Abjuração Erudita"),
        (2, "Proteção Arcana"),
        (6, "Proteção Projetada"),
        (10, "Abjuração Aprimorada"),
        (14, "Resistência à Magia"),
    ],

    "Escola de Adivinhação": [
        (2, "Adivinhação Erudita"),
        (2, "Portento"),
        (6, "Especialista em Adivinhação"),
        (10, "O Terceiro Olho"),
        (14, "Portento Maior"),
    ],

    "Escola de Conjuração": [
        (2, "Conjuração Erudita"),
        (2, "Conjuração Menor"),
        (6, "Transposição Benigna"),
        (10, "Conjuração Focada"),
        (14, "Invocações Resistentes"),
    ],

    "Escola de Encantamento": [
        (2, "Encantamento Erudito"),
        (2, "Olhar Hipnótico"),
        (6, "Encanto Instintivo"),
        (10, "Dividir Encantamento"),
        (14, "Alterar Memórias"),
    ],

    "Escola de Evocação": [
        (2, "Evocação Erudita"),
        (2, "Esculpir Magias"),
        (6, "Truque Potente"),
        (10, "Evocação Potencializada"),
        (14, "Sobrecarga"),
    ],

    "Escola de Ilusão": [
        (2, "Ilusão Erudita"),
        (2, "Ilusão Menor Aprimorada"),
        (6, "Ilusões Moldáveis"),
        (10, "Eu Ilusório"),
        (14, "Realidade Ilusória"),
    ],

    "Escola de Necromancia": [
        (2, "Necromancia Erudita"),
        (2, "Colheita Sinistra"),
        (6, "Escravos Mortos-Vivos"),
        (10, "Acostumado à Morte"),
        (14, "Comandar Mortos-Vivos"),
    ],

    "Escola de Transmutação": [
        (2, "Transmutação Erudita"),
        (2, "Alquimia Menor"),
        (6, "Pedra de Transmutador"),
        (10, "Metamorfo"),
        (14, "Mestre Transmutador"),
    ],

    "Caminho da Mão Aberta": [
        (3, "Técnica da Mão Aberta"),
        (6, "Integridade Corporal"),
        (11, "Tranquilidade"),
        (17, "Palma Vibrante"),
    ],

    "Caminho da Sombra": [
        (3, "Artes Sombrias"),
        (6, "Passo das Sombras"),
        (11, "Manto de Sombras"),
        (17, "Oportunista"),
    ],

    "Caminho dos Quatro Elementos": [
        (3, "Discípulo dos Elementos"),
        (6, "Disciplina Elemental Adicional"),
        (11, "Disciplina Elemental Adicional"),
        (17, "Disciplina Elemental Adicional"),
    ],

    "Juramento de Devoção": [
        (3, "Canalizar Divindade"),
        (7, "Aura de Devoção"),
        (15, "Pureza de Espírito"),
        (20, "Auréola Sagrada"),
    ],

    "Juramento dos Anciões": [
        (3, "Canalizar Divindade"),
        (7, "Aura de Vigilância"),
        (15, "Sentinela Imortal"),
        (20, "Campeão dos Anciões"),
    ],

    "Juramento de Vingança": [
        (3, "Canalizar Divindade"),
        (7, "Vingador Implacável"),
        (15, "Alma de Vingança"),
        (20, "Anjo Vingador"),
    ],

    "Conclave do Caçador": [
        (3, "Presa do Caçador"),
        (7, "Táticas Defensivas"),
        (11, "Ataque Múltiplo"),
        (15, "Defesa Superior do Caçador"),
    ],

    "Conclave do Mestre das Bestas": [
        (3, "Companheiro do Patrulheiro"),
        (7, "Treinamento Excepcional"),
        (11, "Fúria Bestial"),
        (15, "Partilhar Magias"),
    ],
}


def buscar_subclasse(cursor, nome):
    cursor.execute(
        """
        SELECT id
        FROM subclasses
        WHERE nome = %s;
        """,
        (nome,)
    )

    resultado = cursor.fetchone()

    if resultado is None:
        raise ValueError(
            f"Subclasse não encontrada: {nome}"
        )

    return resultado[0]


def popular_caracteristicas_subclasses():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            DELETE FROM caracteristicas_subclasses;
            """
        )

        for nome_subclasse, lista in CARACTERISTICAS.items():

            subclasse_id = buscar_subclasse(
                cursor,
                nome_subclasse
            )

            for nivel, nome in lista:

                cursor.execute(
                    """
                    INSERT INTO caracteristicas_subclasses (
                        subclasse_id,
                        nivel,
                        nome,
                        descricao
                    )
                    VALUES (%s, %s, %s, NULL);
                    """,
                    (
                        subclasse_id,
                        nivel,
                        nome
                    )
                )

        conexao.commit()

        print(
            "Características das subclasses "
            "cadastradas com sucesso!"
        )

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


if __name__ == "__main__":
    popular_caracteristicas_subclasses()