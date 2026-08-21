# =========================================================
# MAGIAS RACIAIS
# D&D 5e - Livro do Jogador usado pelo projeto
# =========================================================
#
# Este arquivo NÃO popula o banco sozinho.
#
# Ele guarda as regras das magias recebidas através
# de raça/sub-raça para posteriormente serem vinculadas
# aos personagens.
#
# nivel_personagem:
# nível em que a magia é desbloqueada
#
# habilidade:
# atributo usado para conjuração
#
# usa_slot:
# indica se o uso racial consome slot normal da classe
#
# usos:
# None = uso livre como truque
# 1 = um uso antes da recuperação indicada
#
# descanso:
# quando os usos raciais são recuperados
#
# nivel_conjuracao:
# nível em que a magia é conjurada quando a característica
# racial especifica isso.
# =========================================================


MAGIAS_RACIAIS = {

    # =====================================================
    # DROW
    # =====================================================
    #
    # Magia Drow:
    #
    # Nível 1:
    # Globos de Luz
    #
    # Nível 3:
    # Fogo das Fadas
    # 1 vez por descanso longo
    #
    # Nível 5:
    # Escuridão
    # 1 vez por descanso longo
    #
    # Habilidade: Carisma
    # =====================================================

    "Drow": [

        {
            "nome": "Globos de Luz",
            "nivel_personagem": 1,
            "habilidade": "carisma",
            "usa_slot": False,
            "usos": None,
            "descanso": None,
            "nivel_conjuracao": 0,
        },

        {
            "nome": "Fogo das Fadas",
            "nivel_personagem": 3,
            "habilidade": "carisma",
            "usa_slot": False,
            "usos": 1,
            "descanso": "longo",
            "nivel_conjuracao": 1,
        },

        {
            "nome": "Escuridão",
            "nivel_personagem": 5,
            "habilidade": "carisma",
            "usa_slot": False,
            "usos": 1,
            "descanso": "longo",
            "nivel_conjuracao": 2,
        },
    ],


    # =====================================================
    # TIEFLING
    # =====================================================
    #
    # Legado Infernal:
    #
    # Nível 1:
    # Taumaturgia
    #
    # Nível 3:
    # Repreensão Infernal
    # conjurada como magia de 2º nível
    # 1 vez por descanso longo
    #
    # Nível 5:
    # Escuridão
    # 1 vez por descanso longo
    #
    # Habilidade: Carisma
    # =====================================================

    "Tiefling": [

        {
            "nome": "Taumaturgia",
            "nivel_personagem": 1,
            "habilidade": "carisma",
            "usa_slot": False,
            "usos": None,
            "descanso": None,
            "nivel_conjuracao": 0,
        },

        {
            "nome": "Repreensão Infernal",
            "nivel_personagem": 3,
            "habilidade": "carisma",
            "usa_slot": False,
            "usos": 1,
            "descanso": "longo",
            "nivel_conjuracao": 2,
        },

        {
            "nome": "Escuridão",
            "nivel_personagem": 5,
            "habilidade": "carisma",
            "usa_slot": False,
            "usos": 1,
            "descanso": "longo",
            "nivel_conjuracao": 2,
        },
    ],


    # =====================================================
    # GNOMO DA FLORESTA
    # =====================================================
    #
    # Ilusionista Nato:
    #
    # conhece Ilusão Menor
    #
    # Habilidade: Inteligência
    # =====================================================

    "Gnomo da Floresta": [

        {
            "nome": "Ilusão Menor",
            "nivel_personagem": 1,
            "habilidade": "inteligencia",
            "usa_slot": False,
            "usos": None,
            "descanso": None,
            "nivel_conjuracao": 0,
        },
    ],
}