from mini_mestre.database import conectar


DADOS_CLASSES = {

    "Bárbaro": [
        {
            "titulo": "Escolha sua arma principal",
            "opcoes": [
                [
                    {
                        "equipamento": "Machado Grande",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "categoria": "arma_marcial_corpo_a_corpo",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Escolha seu segundo conjunto de armas",
            "opcoes": [
                [
                    {
                        "equipamento": "Machadinha",
                        "quantidade": 2
                    }
                ],
                [
                    {
                        "categoria": "arma_simples",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Equipamento fixo do Bárbaro",
            "opcoes": [
                [
                    {
                        "equipamento": "Pacote de Aventureiro",
                        "quantidade": 1
                    },
                    {
                        "equipamento": "Azagaia",
                        "quantidade": 4
                    },
                ]
            ],
        },
    ],

    "Bardo": [
        {
            "titulo": "Escolha sua arma",
            "opcoes": [
                [
                    {
                        "equipamento": "Rapieira",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "equipamento": "Espada Longa",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "categoria": "arma_simples",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Escolha seu pacote",
            "opcoes": [
                [
                    {
                        "equipamento": "Pacote de Diplomata",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "equipamento": "Pacote de Artista",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Escolha seu instrumento musical",
            "opcoes": [
                [
                    {
                        "equipamento": "Lute",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "categoria": "instrumento_musical",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Equipamento fixo do Bardo",
            "opcoes": [
                [
                    {
                        "equipamento": "Armadura de Couro",
                        "quantidade": 1
                    },
                    {
                        "equipamento": "Adaga",
                        "quantidade": 1
                    },
                ]
            ],
        },
    ],

    "Bruxo": [
        {
            "titulo": "Escolha sua arma inicial",
            "opcoes": [
                [
                    {
                        "equipamento": "Besta Leve",
                        "quantidade": 1
                    },
                    {
                        "equipamento": "Virotes",
                        "quantidade": 20
                    },
                ],
                [
                    {
                        "categoria": "arma_simples",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Escolha seu foco de conjuração",
            "opcoes": [
                [
                    {
                        "equipamento": "Bolsa de Componentes",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "equipamento": "Foco Arcano",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Escolha seu pacote",
            "opcoes": [
                [
                    {
                        "equipamento": "Pacote de Estudioso",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "equipamento": "Pacote de Explorador",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Equipamento fixo do Bruxo",
            "opcoes": [
                [
                    {
                        "equipamento": "Armadura de Couro",
                        "quantidade": 1
                    },
                    {
                        "categoria": "arma_simples",
                        "quantidade": 1
                    },
                    {
                        "equipamento": "Adaga",
                        "quantidade": 2
                    },
                ]
            ],
        },
    ],

    "Clérigo": [
        {
            "titulo": "Escolha sua arma",
            "opcoes": [
                [
                    {
                        "equipamento": "Maça",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "equipamento": "Martelo de Guerra",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Escolha sua armadura",
            "opcoes": [
                [
                    {
                        "equipamento": "Brunea",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "equipamento": "Armadura de Couro",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "equipamento": "Cota de Malha",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Escolha seu armamento adicional",
            "opcoes": [
                [
                    {
                        "equipamento": "Besta Leve",
                        "quantidade": 1
                    },
                    {
                        "equipamento": "Virotes",
                        "quantidade": 20
                    },
                ],
                [
                    {
                        "categoria": "arma_simples",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Escolha seu pacote",
            "opcoes": [
                [
                    {
                        "equipamento": "Pacote de Sacerdote",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "equipamento": "Pacote de Aventureiro",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Equipamento fixo do Clérigo",
            "opcoes": [
                [
                    {
                        "equipamento": "Escudo",
                        "quantidade": 1
                    },
                    {
                        "equipamento": "Símbolo Sagrado",
                        "quantidade": 1
                    },
                ]
            ],
        },
    ],

    "Druida": [
        {
            "titulo": "Escolha seu primeiro equipamento",
            "opcoes": [
                [
                    {
                        "equipamento": "Escudo de Madeira",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "categoria": "arma_simples",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Escolha sua arma",
            "opcoes": [
                [
                    {
                        "equipamento": "Cimitarra",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "categoria": "arma_simples_corpo_a_corpo",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Equipamento fixo do Druida",
            "opcoes": [
                [
                    {
                        "equipamento": "Armadura de Couro",
                        "quantidade": 1
                    },
                    {
                        "equipamento": "Pacote de Aventureiro",
                        "quantidade": 1
                    },
                    {
                        "equipamento": "Foco Druídico",
                        "quantidade": 1
                    },
                ]
            ],
        },
    ],

    "Feiticeiro": [
        {
            "titulo": "Escolha sua arma",
            "opcoes": [
                [
                    {
                        "equipamento": "Besta Leve",
                        "quantidade": 1
                    },
                    {
                        "equipamento": "Virotes",
                        "quantidade": 20
                    },
                ],
                [
                    {
                        "categoria": "arma_simples",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Escolha seu foco de conjuração",
            "opcoes": [
                [
                    {
                        "equipamento": "Bolsa de Componentes",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "equipamento": "Foco Arcano",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Escolha seu pacote",
            "opcoes": [
                [
                    {
                        "equipamento": "Pacote de Explorador",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "equipamento": "Pacote de Aventureiro",
                        "quantidade": 1
                    }
                ],
            ],
        },
    ],

    "Guerreiro": [
        {
            "titulo": "Escolha seu conjunto de armadura",
            "opcoes": [
                [
                    {
                        "equipamento": "Cota de Malha",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "equipamento": "Gibão de Peles",
                        "quantidade": 1
                    },
                    {
                        "equipamento": "Arco Longo",
                        "quantidade": 1
                    },
                    {
                        "equipamento": "Flechas",
                        "quantidade": 20
                    },
                ],
            ],
        },

        {
            "titulo": "Escolha suas armas marciais",
            "opcoes": [
                [
                    {
                        "categoria": "arma_marcial",
                        "quantidade": 1
                    },
                    {
                        "equipamento": "Escudo",
                        "quantidade": 1
                    },
                ],
                [
                    {
                        "categoria": "arma_marcial",
                        "quantidade": 2
                    }
                ],
            ],
        },

        {
            "titulo": "Escolha seu equipamento à distância",
            "opcoes": [
                [
                    {
                        "equipamento": "Besta Leve",
                        "quantidade": 1
                    },
                    {
                        "equipamento": "Virotes",
                        "quantidade": 20
                    },
                ],
                [
                    {
                        "equipamento": "Machadinha",
                        "quantidade": 2
                    }
                ],
            ],
        },

        {
            "titulo": "Escolha seu pacote",
            "opcoes": [
                [
                    {
                        "equipamento": "Pacote de Aventureiro",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "equipamento": "Pacote de Explorador",
                        "quantidade": 1
                    }
                ],
            ],
        },
    ],

    "Ladino": [
        {
            "titulo": "Escolha sua arma principal",
            "opcoes": [
                [
                    {
                        "equipamento": "Rapieira",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "equipamento": "Espada Longa",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Escolha seu segundo armamento",
            "opcoes": [
                [
                    {
                        "equipamento": "Arco Curto",
                        "quantidade": 1
                    },
                    {
                        "equipamento": "Aljava",
                        "quantidade": 1
                    },
                    {
                        "equipamento": "Flechas",
                        "quantidade": 20
                    },
                ],
                [
                    {
                        "equipamento": "Espada Curta",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Escolha seu pacote",
            "opcoes": [
                [
                    {
                        "equipamento": "Pacote de Assaltante",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "equipamento": "Pacote de Aventureiro",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "equipamento": "Pacote de Explorador",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Equipamento fixo do Ladino",
            "opcoes": [
                [
                    {
                        "equipamento": "Armadura de Couro",
                        "quantidade": 1
                    },
                    {
                        "equipamento": "Adaga",
                        "quantidade": 2
                    },
                    {
                        "equipamento": "Ferramentas de Ladrão",
                        "quantidade": 1
                    },
                ]
            ],
        },
    ],

    "Mago": [
        {
            "titulo": "Escolha sua arma",
            "opcoes": [
                [
                    {
                        "equipamento": "Bordão",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "equipamento": "Adaga",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Escolha seu foco",
            "opcoes": [
                [
                    {
                        "equipamento": "Bolsa de Componentes",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "equipamento": "Foco Arcano",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Escolha seu pacote",
            "opcoes": [
                [
                    {
                        "equipamento": "Pacote de Estudioso",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "equipamento": "Pacote de Explorador",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Equipamento fixo do Mago",
            "opcoes": [
                [
                    {
                        "equipamento": "Livro de Magias",
                        "quantidade": 1
                    }
                ]
            ],
        },
    ],

    "Monge": [
        {
            "titulo": "Escolha sua arma",
            "opcoes": [
                [
                    {
                        "equipamento": "Espada Curta",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "categoria": "arma_simples",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Escolha seu pacote",
            "opcoes": [
                [
                    {
                        "equipamento": "Pacote de Explorador",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "equipamento": "Pacote de Aventureiro",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Equipamento fixo do Monge",
            "opcoes": [
                [
                    {
                        "equipamento": "Dardo",
                        "quantidade": 10
                    }
                ]
            ],
        },
    ],

    "Paladino": [
        {
            "titulo": "Escolha suas armas principais",
            "opcoes": [
                [
                    {
                        "categoria": "arma_marcial",
                        "quantidade": 1
                    },
                    {
                        "equipamento": "Escudo",
                        "quantidade": 1
                    },
                ],
                [
                    {
                        "categoria": "arma_marcial",
                        "quantidade": 2
                    }
                ],
            ],
        },

        {
            "titulo": "Escolha seu segundo armamento",
            "opcoes": [
                [
                    {
                        "equipamento": "Azagaia",
                        "quantidade": 5
                    }
                ],
                [
                    {
                        "categoria": "arma_simples_corpo_a_corpo",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Escolha seu pacote",
            "opcoes": [
                [
                    {
                        "equipamento": "Pacote de Sacerdote",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "equipamento": "Pacote de Aventureiro",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Equipamento fixo do Paladino",
            "opcoes": [
                [
                    {
                        "equipamento": "Cota de Malha",
                        "quantidade": 1
                    },
                    {
                        "equipamento": "Símbolo Sagrado",
                        "quantidade": 1
                    },
                ]
            ],
        },
    ],

    "Patrulheiro": [
        {
            "titulo": "Escolha sua armadura",
            "opcoes": [
                [
                    {
                        "equipamento": "Brunea",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "equipamento": "Armadura de Couro",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Escolha suas armas corpo a corpo",
            "opcoes": [
                [
                    {
                        "equipamento": "Espada Curta",
                        "quantidade": 2
                    }
                ],
                [
                    {
                        "categoria": "arma_simples_corpo_a_corpo",
                        "quantidade": 2
                    }
                ],
            ],
        },

        {
            "titulo": "Escolha seu pacote",
            "opcoes": [
                [
                    {
                        "equipamento": "Pacote de Explorador",
                        "quantidade": 1
                    }
                ],
                [
                    {
                        "equipamento": "Pacote de Aventureiro",
                        "quantidade": 1
                    }
                ],
            ],
        },

        {
            "titulo": "Equipamento fixo do Patrulheiro",
            "opcoes": [
                [
                    {
                        "equipamento": "Arco Longo",
                        "quantidade": 1
                    },
                    {
                        "equipamento": "Aljava",
                        "quantidade": 1
                    },
                    {
                        "equipamento": "Flechas",
                        "quantidade": 20
                    },
                ]
            ],
        },
    ],
}


def buscar_classe(
    cursor,
    nome
):
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


def buscar_equipamento(
    cursor,
    nome
):
    cursor.execute(
        """
        SELECT id
        FROM equipamentos
        WHERE nome = %s;
        """,
        (nome,)
    )

    resultado = cursor.fetchone()

    if resultado is None:
        raise ValueError(
            f"Equipamento não encontrado: {nome}"
        )

    return resultado[0]


def popular_equipamentos_classes():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            DELETE FROM opcoes_equipamentos_classes;
            """
        )

        cursor.execute(
            """
            DELETE FROM escolhas_equipamentos_classes;
            """
        )

        for nome_classe, escolhas in DADOS_CLASSES.items():

            classe_id = buscar_classe(
                cursor,
                nome_classe
            )

            for numero_grupo, escolha in enumerate(
                escolhas,
                start=1
            ):

                cursor.execute(
                    """
                    INSERT INTO escolhas_equipamentos_classes (
                        classe_id,
                        grupo,
                        quantidade,
                        titulo
                    )
                    VALUES (%s, %s, 1, %s)
                    RETURNING id;
                    """,
                    (
                        classe_id,
                        numero_grupo,
                        escolha["titulo"]
                    )
                )

                escolha_id = cursor.fetchone()[0]

                for numero_opcao, pacote in enumerate(
                    escolha["opcoes"],
                    start=1
                ):

                    for item in pacote:

                        equipamento_id = None
                        categoria = item.get(
                            "categoria"
                        )

                        nome_equipamento = item.get(
                            "equipamento"
                        )

                        if nome_equipamento:
                            equipamento_id = buscar_equipamento(
                                cursor,
                                nome_equipamento
                            )

                        cursor.execute(
                            """
                            INSERT INTO opcoes_equipamentos_classes (
                                escolha_id,
                                opcao,
                                equipamento_id,
                                categoria,
                                quantidade
                            )
                            VALUES (%s, %s, %s, %s, %s);
                            """,
                            (
                                escolha_id,
                                numero_opcao,
                                equipamento_id,
                                categoria,
                                item.get(
                                    "quantidade",
                                    1
                                )
                            )
                        )

        conexao.commit()

        print(
            "Escolhas de equipamento "
            "das classes cadastradas com sucesso!"
        )

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


if __name__ == "__main__":
    popular_equipamentos_classes()