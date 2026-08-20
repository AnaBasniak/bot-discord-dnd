from mini_mestre.database import conectar


CARACTERISTICAS = {
    "Acólito": (
        "Abrigo dos Fiéis",
        "Você pode receber ajuda e abrigo de pessoas e instituições ligadas à sua fé, dependendo da situação."
    ),

    "Artesão de Guilda": (
        "Membro de Guilda",
        "Sua associação com uma guilda pode fornecer contatos, auxílio profissional e reconhecimento entre membros do ofício."
    ),

    "Artista": (
        "Pela Demanda Popular",
        "Sua capacidade de entreter pode garantir alimentação, hospedagem ou oportunidades de apresentação."
    ),

    "Charlatão": (
        "Identidade Falsa",
        "Você mantém uma identidade alternativa e sabe criar documentos e comportamentos convincentes para sustentá-la."
    ),

    "Criminoso": (
        "Contato Criminal",
        "Você conhece pessoas no submundo e sabe como transmitir e receber informações através de contatos criminosos."
    ),

    "Eremita": (
        "Descoberta",
        "Durante seu período de isolamento, você descobriu uma verdade, informação ou revelação importante."
    ),

    "Forasteiro": (
        "Andarilho",
        "Você possui excelente memória para mapas e terrenos e facilidade para encontrar recursos naturais durante viagens."
    ),

    "Herói do Povo": (
        "Hospitalidade Rústica",
        "Pessoas comuns tendem a reconhecer você como alguém digno de confiança e podem oferecer abrigo ou ajuda."
    ),

    "Marinheiro": (
        "Passagem de Navio",
        "Sua experiência marítima facilita conseguir passagem em embarcações para você e seus companheiros em certas situações."
    ),

    "Nobre": (
        "Posição Privilegiada",
        "Sua posição social permite acesso mais fácil à alta sociedade e costuma gerar tratamento diferenciado."
    ),

    "Órfão": (
        "Segredos da Cidade",
        "Você conhece caminhos, atalhos e rotas urbanas que permitem viajar pelas cidades com maior eficiência."
    ),

    "Sábio": (
        "Pesquisador",
        "Quando você não sabe uma informação, geralmente sabe onde ou com quem procurar por ela."
    ),

    "Soldado": (
        "Patente Militar",
        "Sua posição ou histórico militar pode fazer com que outros soldados reconheçam sua autoridade ou experiência."
    ),
}


def buscar_antecedente(
    cursor,
    nome
):
    cursor.execute(
        """
        SELECT id
        FROM antecedentes
        WHERE nome = %s;
        """,
        (nome,)
    )

    resultado = cursor.fetchone()

    if resultado is None:
        raise ValueError(
            f"Antecedente não encontrado: {nome}"
        )

    return resultado[0]


def popular_caracteristicas_antecedentes():
    conexao = conectar()
    cursor = conexao.cursor()

    try:

        cursor.execute(
            """
            DELETE FROM caracteristicas_antecedentes;
            """
        )

        for (
            nome_antecedente,
            dados
        ) in CARACTERISTICAS.items():

            nome_caracteristica = dados[0]
            descricao = dados[1]

            antecedente_id = buscar_antecedente(
                cursor,
                nome_antecedente
            )

            cursor.execute(
                """
                INSERT INTO caracteristicas_antecedentes (
                    antecedente_id,
                    nome,
                    descricao
                )
                VALUES (%s, %s, %s);
                """,
                (
                    antecedente_id,
                    nome_caracteristica,
                    descricao
                )
            )

        conexao.commit()

        print(
            "Características dos antecedentes "
            "cadastradas com sucesso!"
        )

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


if __name__ == "__main__":
    popular_caracteristicas_antecedentes()