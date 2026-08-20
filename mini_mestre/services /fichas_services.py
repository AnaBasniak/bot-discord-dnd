from mini_mestre.database import conectar


# =========================================================
# CONSTANTES
# =========================================================

PERICIAS_VALIDAS = {
    "acrobacia",
    "arcanismo",
    "atletismo",
    "atuacao",
    "enganacao",
    "furtividade",
    "historia",
    "intimidacao",
    "intuicao",
    "investigacao",
    "adestrar_animais",
    "medicina",
    "natureza",
    "percepcao",
    "persuasao",
    "prestidigitacao",
    "religiao",
    "sobrevivencia",
}

ATRIBUTOS_VALIDOS = {
    "forca",
    "destreza",
    "constituicao",
    "inteligencia",
    "sabedoria",
    "carisma",
}


# =========================================================
# UTIL
# =========================================================

def calcular_modificador(valor):
    return (valor - 10) // 2


# =========================================================
# RAÇAS
# =========================================================

def listar_racas():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT id, nome, descricao, deslocamento
            FROM racas
            ORDER BY nome;
            """
        )

        return [
            {
                "id": linha[0],
                "nome": linha[1],
                "descricao": linha[2],
                "deslocamento": linha[3],
            }
            for linha in cursor.fetchall()
        ]

    finally:
        cursor.close()
        conexao.close()


def listar_subracas(raca_id):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT id, nome, descricao
            FROM subracas
            WHERE raca_id = %s
            ORDER BY nome;
            """,
            (raca_id,)
        )

        return [
            {
                "id": linha[0],
                "nome": linha[1],
                "descricao": linha[2],
            }
            for linha in cursor.fetchall()
        ]

    finally:
        cursor.close()
        conexao.close()


def listar_bonus_atributos_raciais(
    raca_id,
    subraca_id=None
):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        if subraca_id is None:
            cursor.execute(
                """
                SELECT atributo, bonus
                FROM bonus_atributos_raciais
                WHERE raca_id = %s
                  AND subraca_id IS NULL;
                """,
                (raca_id,)
            )

        else:
            cursor.execute(
                """
                SELECT atributo, bonus
                FROM bonus_atributos_raciais
                WHERE
                    (
                        raca_id = %s
                        AND subraca_id IS NULL
                    )
                    OR subraca_id = %s;
                """,
                (
                    raca_id,
                    subraca_id
                )
            )

        return [
            {
                "atributo": linha[0],
                "bonus": linha[1],
            }
            for linha in cursor.fetchall()
        ]

    finally:
        cursor.close()
        conexao.close()


def listar_escolhas_raciais(
    raca_id,
    subraca_id=None
):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        if subraca_id is None:
            cursor.execute(
                """
                SELECT
                    id,
                    tipo,
                    titulo,
                    quantidade
                FROM escolhas_raciais
                WHERE raca_id = %s
                  AND subraca_id IS NULL
                ORDER BY id;
                """,
                (raca_id,)
            )
        else:
            cursor.execute(
                """
                SELECT
                    id,
                    tipo,
                    titulo,
                    quantidade
                FROM escolhas_raciais
                WHERE
                    (
                        raca_id = %s
                        AND subraca_id IS NULL
                    )
                    OR subraca_id = %s
                ORDER BY id;
                """,
                (
                    raca_id,
                    subraca_id
                )
            )

        return [
            {
                "id": linha[0],
                "tipo": linha[1],
                "titulo": linha[2],
                "quantidade": linha[3],
            }
            for linha in cursor.fetchall()
        ]

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# CLASSES
# =========================================================

def listar_classes():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT
                id,
                nome,
                descricao,
                dado_vida,
                nivel_maximo,
                quantidade_pericias
            FROM classes
            ORDER BY nome;
            """
        )

        return [
            {
                "id": linha[0],
                "nome": linha[1],
                "descricao": linha[2],
                "dado_vida": linha[3],
                "nivel_maximo": linha[4],
                "quantidade_pericias": linha[5],
            }
            for linha in cursor.fetchall()
        ]

    finally:
        cursor.close()
        conexao.close()


def listar_subclasses(classe_id):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT
                id,
                nome,
                descricao,
                nivel_escolha
            FROM subclasses
            WHERE classe_id = %s
            ORDER BY nome;
            """,
            (classe_id,)
        )

        return [
            {
                "id": linha[0],
                "nome": linha[1],
                "descricao": linha[2],
                "nivel_escolha": linha[3],
            }
            for linha in cursor.fetchall()
        ]

    finally:
        cursor.close()
        conexao.close()


def listar_pericias_classe(classe_id):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT pericia
            FROM pericias_classes
            WHERE classe_id = %s
            ORDER BY pericia;
            """,
            (classe_id,)
        )

        return [
            linha[0]
            for linha in cursor.fetchall()
        ]

    finally:
        cursor.close()
        conexao.close()


def listar_salvaguardas_classe(classe_id):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT atributo
            FROM salvaguardas_classes
            WHERE classe_id = %s
            ORDER BY atributo;
            """,
            (classe_id,)
        )

        return [
            linha[0]
            for linha in cursor.fetchall()
        ]

    finally:
        cursor.close()
        conexao.close()


def listar_proficiencias_classe(classe_id):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT tipo, nome
            FROM proficiencias_classes
            WHERE classe_id = %s
            ORDER BY tipo, nome;
            """,
            (classe_id,)
        )

        return [
            {
                "tipo": linha[0],
                "nome": linha[1],
            }
            for linha in cursor.fetchall()
        ]

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# ANTECEDENTES
# =========================================================

def listar_antecedentes():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT id, nome, descricao
            FROM antecedentes
            ORDER BY nome;
            """
        )

        return [
            {
                "id": linha[0],
                "nome": linha[1],
                "descricao": linha[2],
            }
            for linha in cursor.fetchall()
        ]

    finally:
        cursor.close()
        conexao.close()


def listar_pericias_antecedente(antecedente_id):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT pericia
            FROM pericias_antecedentes
            WHERE antecedente_id = %s
            ORDER BY pericia;
            """,
            (antecedente_id,)
        )

        return [
            linha[0]
            for linha in cursor.fetchall()
        ]

    finally:
        cursor.close()
        conexao.close()


def listar_proficiencias_antecedente(antecedente_id):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT tipo, nome
            FROM proficiencias_antecedentes
            WHERE antecedente_id = %s
            ORDER BY tipo, nome;
            """,
            (antecedente_id,)
        )

        return [
            {
                "tipo": linha[0],
                "nome": linha[1],
            }
            for linha in cursor.fetchall()
        ]

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# EQUIPAMENTOS
# =========================================================

def listar_escolhas_equipamento_classe(classe_id):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT
                id,
                grupo,
                quantidade,
                titulo
            FROM escolhas_equipamentos_classes
            WHERE classe_id = %s
            ORDER BY grupo, id;
            """,
            (classe_id,)
        )

        escolhas = []

        for linha in cursor.fetchall():
            escolha_id = linha[0]

            cursor.execute(
                """
                SELECT
                    o.opcao,
                    o.equipamento_id,
                    e.nome,
                    o.categoria,
                    o.quantidade
                FROM opcoes_equipamentos_classes o
                LEFT JOIN equipamentos e
                    ON e.id = o.equipamento_id
                WHERE o.escolha_id = %s
                ORDER BY o.opcao, o.id;
                """,
                (escolha_id,)
            )

            grupos = {}

            for opcao in cursor.fetchall():
                numero_opcao = opcao[0]

                if numero_opcao not in grupos:
                    grupos[numero_opcao] = []

                grupos[numero_opcao].append(
                    {
                        "equipamento_id": opcao[1],
                        "nome": opcao[2],
                        "categoria": opcao[3],
                        "quantidade": opcao[4],
                    }
                )

            escolhas.append(
                {
                    "id": escolha_id,
                    "grupo": linha[1],
                    "quantidade": linha[2],
                    "titulo": linha[3],
                    "opcoes": grupos,
                }
            )

        return escolhas

    finally:
        cursor.close()
        conexao.close()


def listar_equipamentos_categoria(categoria):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        categorias = {
            "arma_simples": [
                "Adaga",
                "Azagaia",
                "Bordão",
                "Clava",
                "Dardo",
                "Funda",
                "Lança",
                "Machadinha",
                "Maça",
                "Martelo Leve",
                "Arco Curto",
                "Besta Leve",
            ],

            "arma_simples_corpo_a_corpo": [
                "Adaga",
                "Azagaia",
                "Bordão",
                "Clava",
                "Lança",
                "Machadinha",
                "Maça",
                "Martelo Leve",
            ],

            "arma_marcial": [
                "Arco Longo",
                "Besta de Mão",
                "Cimitarra",
                "Espada Curta",
                "Espada Longa",
                "Machado de Batalha",
                "Machado Grande",
                "Martelo de Guerra",
                "Rapieira",
            ],

            "arma_marcial_corpo_a_corpo": [
                "Cimitarra",
                "Espada Curta",
                "Espada Longa",
                "Machado de Batalha",
                "Machado Grande",
                "Martelo de Guerra",
                "Rapieira",
            ],

            "instrumento_musical": [
                "Lute",
                "Instrumento Musical",
            ],
        }

        nomes = categorias.get(
            categoria,
            []
        )

        if not nomes:
            return []

        cursor.execute(
            """
            SELECT id, nome, tipo
            FROM equipamentos
            WHERE nome = ANY(%s)
            ORDER BY nome;
            """,
            (nomes,)
        )

        return [
            {
                "id": linha[0],
                "nome": linha[1],
                "tipo": linha[2],
            }
            for linha in cursor.fetchall()
        ]

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# JOGADOR
# =========================================================

def garantir_jogador(
    discord_id,
    nome_discord
):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO jogadores (
                discord_id,
                nome_discord
            )
            VALUES (%s, %s)

            ON CONFLICT (discord_id)
            DO UPDATE SET
                nome_discord = EXCLUDED.nome_discord;
            """,
            (
                discord_id,
                nome_discord
            )
        )

        conexao.commit()

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# CRIAR PERSONAGEM
# =========================================================

def criar_personagem(
    discord_id,
    nome_personagem,
    raca,
    subraca,
    classe,
    subclasse,
    antecedente,
    deslocamento,
    atributos,
    pericias,
    salvaguardas,
    proficiencias,
):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        mod_con = calcular_modificador(
            atributos["constituicao"]
        )

        pv_maximo = max(
            1,
            classe["dado_vida"] + mod_con
        )

        iniciativa = calcular_modificador(
            atributos["destreza"]
        )

        cursor.execute(
            """
            INSERT INTO personagens (
                jogador_id,
                nome,
                nivel,
                raca,
                subraca,
                classe,
                subclasse,
                antecedente,
                pv_atual,
                pv_maximo,
                iniciativa,
                deslocamento
            )
            VALUES (
                %s,
                %s,
                1,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            )
            RETURNING id;
            """,
            (
                discord_id,
                nome_personagem,
                raca,
                subraca,
                classe["nome"],
                subclasse,
                antecedente,
                pv_maximo,
                pv_maximo,
                iniciativa,
                deslocamento,
            )
        )

        personagem_id = cursor.fetchone()[0]

        cursor.execute(
            """
            INSERT INTO atributos (
                personagem_id,
                forca,
                destreza,
                constituicao,
                inteligencia,
                sabedoria,
                carisma
            )
            VALUES (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            );
            """,
            (
                personagem_id,
                atributos["forca"],
                atributos["destreza"],
                atributos["constituicao"],
                atributos["inteligencia"],
                atributos["sabedoria"],
                atributos["carisma"],
            )
        )

        cursor.execute(
            """
            INSERT INTO pericias (
                personagem_id
            )
            VALUES (%s);
            """,
            (personagem_id,)
        )

        for pericia in set(pericias):
            if pericia not in PERICIAS_VALIDAS:
                raise ValueError(
                    f"Perícia inválida: {pericia}"
                )

            cursor.execute(
                f"""
                UPDATE pericias
                SET {pericia} = TRUE
                WHERE personagem_id = %s;
                """,
                (personagem_id,)
            )

        cursor.execute(
            """
            INSERT INTO salvaguardas (
                personagem_id
            )
            VALUES (%s);
            """,
            (personagem_id,)
        )

        for atributo in set(salvaguardas):
            if atributo not in ATRIBUTOS_VALIDOS:
                raise ValueError(
                    f"Salvaguarda inválida: {atributo}"
                )

            cursor.execute(
                f"""
                UPDATE salvaguardas
                SET {atributo} = TRUE
                WHERE personagem_id = %s;
                """,
                (personagem_id,)
            )

        for proficiencia in proficiencias:
            cursor.execute(
                """
                INSERT INTO proficiencias (
                    personagem_id,
                    tipo,
                    nome
                )
                VALUES (%s, %s, %s)

                ON CONFLICT (
                    personagem_id,
                    tipo,
                    nome
                )
                DO NOTHING;
                """,
                (
                    personagem_id,
                    proficiencia["tipo"],
                    proficiencia["nome"],
                )
            )

        conexao.commit()

        return {
            "id": personagem_id,
            "pv_maximo": pv_maximo,
            "iniciativa": iniciativa,
        }

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# INVENTÁRIO
# =========================================================

def salvar_inventario(
    personagem_id,
    itens
):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        for item in itens:
            cursor.execute(
                """
                INSERT INTO inventario_personagens (
                    personagem_id,
                    equipamento_id,
                    nome,
                    quantidade,
                    equipado
                )
                VALUES (
                    %s,
                    %s,
                    %s,
                    %s,
                    FALSE
                );
                """,
                (
                    personagem_id,
                    item.get("equipamento_id"),
                    item["nome"],
                    item.get("quantidade", 1),
                )
            )

        conexao.commit()

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# CA
# =========================================================

def calcular_ca_personagem(
    personagem_id,
    classe_nome,
    atributos
):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        mod_des = calcular_modificador(
            atributos["destreza"]
        )

        mod_con = calcular_modificador(
            atributos["constituicao"]
        )

        mod_sab = calcular_modificador(
            atributos["sabedoria"]
        )

        ca = 10 + mod_des

        cursor.execute(
            """
            SELECT
                e.nome,
                e.ca_base,
                e.limite_destreza,
                e.bonus_ca
            FROM inventario_personagens i
            JOIN equipamentos e
                ON e.id = i.equipamento_id
            WHERE i.personagem_id = %s;
            """,
            (personagem_id,)
        )

        itens = cursor.fetchall()

        armaduras = []
        bonus_escudo = 0

        for item in itens:
            ca_base = item[1]
            limite_destreza = item[2]
            bonus_ca = item[3]

            if bonus_ca:
                bonus_escudo = max(
                    bonus_escudo,
                    bonus_ca
                )

            if ca_base is not None:
                if limite_destreza is None:
                    bonus_des = mod_des

                elif limite_destreza == 0:
                    bonus_des = 0

                else:
                    bonus_des = min(
                        mod_des,
                        limite_destreza
                    )

                armaduras.append(
                    ca_base + bonus_des
                )

        if armaduras:
            ca = max(armaduras)

        else:
            if classe_nome == "Bárbaro":
                ca = max(
                    ca,
                    10 + mod_des + mod_con
                )

            if classe_nome == "Monge":
                ca = max(
                    ca,
                    10 + mod_des + mod_sab
                )

        if classe_nome != "Monge":
            ca += bonus_escudo

        cursor.execute(
            """
            UPDATE personagens
            SET ca = %s
            WHERE id = %s;
            """,
            (
                ca,
                personagem_id
            )
        )

        conexao.commit()

        return ca

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()