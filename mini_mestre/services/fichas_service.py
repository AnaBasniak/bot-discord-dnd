from mini_mestre.database import conectar
from mini_mestre.data.magias_raciais import MAGIAS_RACIAIS


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
    "lidar_animais",
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

        # Anão da Colina:
        # Tenacidade Anã concede +1 PV por nível.
        if subraca == "Anão da Colina":
            pv_maximo += 1

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
# MAGIAS - INTEGRAÇÃO COM PERSONAGEM
# =========================================================

def listar_truques_mago():
    """
    Retorna os truques (nível 0) disponíveis para Mago.
    Usado pela escolha racial do Alto Elfo.
    """
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT
                m.id,
                m.nome,
                m.escola
            FROM magias m
            JOIN magias_classes mc
                ON mc.magia_id = m.id
            JOIN classes c
                ON c.id = mc.classe_id
            WHERE c.nome = 'Mago'
              AND m.nivel = 0
            ORDER BY m.nome;
            """
        )

        return [
            {
                "id": linha[0],
                "nome": linha[1],
                "escola": linha[2],
            }
            for linha in cursor.fetchall()
        ]

    finally:
        cursor.close()
        conexao.close()


def _buscar_magia_id_cursor(
    cursor,
    nome_magia
):
    cursor.execute(
        """
        SELECT id
        FROM magias
        WHERE LOWER(nome) = LOWER(%s);
        """,
        (nome_magia,)
    )

    resultado = cursor.fetchone()

    if resultado is None:
        raise ValueError(
            f"Magia não encontrada no banco: {nome_magia}"
        )

    return resultado[0]


def _registrar_magia_racial_cursor(
    cursor,
    personagem_id,
    nome_magia,
    origem,
    habilidade_conjuracao,
    nivel_desbloqueio,
    usa_slot=False,
    usos_maximos=None,
    descanso_recuperacao=None,
    nivel_conjuracao=None,
):
    magia_id = _buscar_magia_id_cursor(
        cursor,
        nome_magia
    )

    origem_banco = (
        f"raca:{origem}"
    )

    # Guarda a magia também na lista geral do personagem.
    cursor.execute(
        """
        INSERT INTO magias_personagens (
            personagem_id,
            magia_id,
            conhecida,
            preparada,
            origem
        )
        VALUES (
            %s,
            %s,
            TRUE,
            FALSE,
            %s
        )
        ON CONFLICT (
            personagem_id,
            magia_id,
            origem
        )
        DO UPDATE SET
            conhecida = TRUE;
        """,
        (
            personagem_id,
            magia_id,
            origem_banco,
        )
    )

    # Guarda as regras próprias do traço racial.
    cursor.execute(
        """
        INSERT INTO magias_raciais_personagens (
            personagem_id,
            magia_id,
            origem,
            habilidade_conjuracao,
            nivel_desbloqueio,
            usa_slot,
            usos_maximos,
            usos_gastos,
            descanso_recuperacao,
            nivel_conjuracao
        )
        VALUES (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            0,
            %s,
            %s
        )
        ON CONFLICT (
            personagem_id,
            magia_id,
            origem
        )
        DO UPDATE SET
            habilidade_conjuracao =
                EXCLUDED.habilidade_conjuracao,
            nivel_desbloqueio =
                EXCLUDED.nivel_desbloqueio,
            usa_slot =
                EXCLUDED.usa_slot,
            usos_maximos =
                EXCLUDED.usos_maximos,
            descanso_recuperacao =
                EXCLUDED.descanso_recuperacao,
            nivel_conjuracao =
                EXCLUDED.nivel_conjuracao;
        """,
        (
            personagem_id,
            magia_id,
            origem,
            habilidade_conjuracao,
            nivel_desbloqueio,
            usa_slot,
            usos_maximos,
            descanso_recuperacao,
            nivel_conjuracao,
        )
    )


def sincronizar_slots_personagem(
    personagem_id,
    classe_nome,
    nivel_personagem
):
    """
    Copia para o personagem os espaços previstos em
    slots_magia_classes para a classe e o nível informados.

    Também funciona para Bruxo, pois a progressão de Pacto
    está cadastrada nessa tabela com o nível único do espaço.
    A recuperação curta/longa será tratada pelo Elfo Doméstico.
    """
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT id
            FROM classes
            WHERE nome = %s;
            """,
            (classe_nome,)
        )

        resultado = cursor.fetchone()

        if resultado is None:
            raise ValueError(
                f"Classe não encontrada: {classe_nome}"
            )

        classe_id = resultado[0]

        cursor.execute(
            """
            SELECT
                nivel_magia,
                quantidade
            FROM slots_magia_classes
            WHERE classe_id = %s
              AND nivel_classe = %s
            ORDER BY nivel_magia;
            """,
            (
                classe_id,
                nivel_personagem,
            )
        )

        progressao = cursor.fetchall()

        # Remove níveis que deixaram de existir na progressão
        # atual e recria/atualiza os que são válidos.
        cursor.execute(
            """
            DELETE FROM slots_magia_personagens
            WHERE personagem_id = %s;
            """,
            (personagem_id,)
        )

        for nivel_magia, quantidade in progressao:
            cursor.execute(
                """
                INSERT INTO slots_magia_personagens (
                    personagem_id,
                    nivel_slot,
                    total,
                    usados
                )
                VALUES (
                    %s,
                    %s,
                    %s,
                    0
                );
                """,
                (
                    personagem_id,
                    nivel_magia,
                    quantidade,
                )
            )

        conexao.commit()

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


def registrar_magias_raciais_personagem(
    personagem_id,
    raca_nome,
    subraca_nome,
    nivel_personagem=1,
    truque_alto_elfo=None,
):
    """
    Registra as magias raciais já desbloqueadas no nível atual.

    Casos fixos:
    - Drow
    - Tiefling
    - Gnomo da Floresta

    Caso de escolha:
    - Alto Elfo
    """
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        # Primeiro verifica a sub-raça, depois a raça.
        chave = None

        if (
            subraca_nome
            and subraca_nome in MAGIAS_RACIAIS
        ):
            chave = subraca_nome

        elif raca_nome in MAGIAS_RACIAIS:
            chave = raca_nome

        if chave is not None:
            for regra in MAGIAS_RACIAIS[chave]:

                if (
                    regra["nivel_personagem"]
                    > nivel_personagem
                ):
                    continue

                _registrar_magia_racial_cursor(
                    cursor=cursor,
                    personagem_id=personagem_id,
                    nome_magia=regra["nome"],
                    origem=chave,
                    habilidade_conjuracao=
                        regra["habilidade"],
                    nivel_desbloqueio=
                        regra["nivel_personagem"],
                    usa_slot=
                        regra.get(
                            "usa_slot",
                            False
                        ),
                    usos_maximos=
                        regra.get("usos"),
                    descanso_recuperacao=
                        regra.get("descanso"),
                    nivel_conjuracao=
                        regra.get(
                            "nivel_conjuracao"
                        ),
                )

        # Alto Elfo escolhe um truque da lista de Mago.
        if subraca_nome == "Alto Elfo":

            if not truque_alto_elfo:
                raise ValueError(
                    "O Alto Elfo precisa escolher "
                    "um truque da lista de Mago."
                )

            cursor.execute(
                """
                SELECT
                    m.id
                FROM magias m
                JOIN magias_classes mc
                    ON mc.magia_id = m.id
                JOIN classes c
                    ON c.id = mc.classe_id
                WHERE LOWER(m.nome) = LOWER(%s)
                  AND m.nivel = 0
                  AND c.nome = 'Mago';
                """,
                (truque_alto_elfo,)
            )

            if cursor.fetchone() is None:
                raise ValueError(
                    "O truque escolhido pelo Alto Elfo "
                    "não pertence à lista de Mago."
                )

            _registrar_magia_racial_cursor(
                cursor=cursor,
                personagem_id=personagem_id,
                nome_magia=truque_alto_elfo,
                origem="Alto Elfo",
                habilidade_conjuracao="inteligencia",
                nivel_desbloqueio=1,
                usa_slot=False,
                usos_maximos=None,
                descanso_recuperacao=None,
                nivel_conjuracao=0,
            )

        conexao.commit()

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


def inicializar_sistema_magico_personagem(
    personagem_id,
    classe_nome,
    raca_nome,
    subraca_nome,
    nivel_personagem=1,
    truque_alto_elfo=None,
):
    """
    Inicializa a parte mágica da ficha sem escolher
    magias de classe.

    As magias de classe serão gerenciadas pelo
    Elfo Doméstico.
    """
    sincronizar_slots_personagem(
        personagem_id,
        classe_nome,
        nivel_personagem
    )

    registrar_magias_raciais_personagem(
        personagem_id=personagem_id,
        raca_nome=raca_nome,
        subraca_nome=subraca_nome,
        nivel_personagem=nivel_personagem,
        truque_alto_elfo=truque_alto_elfo,
    )

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

            equipamento_id = item.get(
                "equipamento_id"
            )

            equipado = False

            # Armaduras e escudos iniciais
            # já começam equipados.
            if equipamento_id is not None:

                cursor.execute(
                    """
                    SELECT tipo
                    FROM equipamentos
                    WHERE id = %s;
                    """,
                    (equipamento_id,)
                )

                resultado = cursor.fetchone()

                if resultado:
                    tipo = resultado[0]

                    if tipo in (
                        "armadura",
                        "escudo",
                    ):
                        equipado = True

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
                    %s
                );
                """,
                (
                    personagem_id,
                    equipamento_id,
                    item["nome"],
                    item.get(
                        "quantidade",
                        1
                    ),
                    equipado,
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
                e.tipo,
                e.ca_base,
                e.limite_destreza,
                e.bonus_ca
            FROM inventario_personagens i
            JOIN equipamentos e
                ON e.id = i.equipamento_id
            WHERE i.personagem_id = %s
              AND i.equipado = TRUE;
            """,
            (personagem_id,)
        )

        itens = cursor.fetchall()

        armaduras = []
        bonus_escudo = 0

        for item in itens:

            tipo = item[1]
            ca_base = item[2]
            limite_destreza = item[3]
            bonus_ca = item[4]

            if tipo == "escudo":
                bonus_escudo = max(
                    bonus_escudo,
                    bonus_ca
                )

            if tipo == "armadura":

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

            ca = max(
                armaduras
            )

        else:

            if classe_nome == "Bárbaro":
                ca = max(
                    ca,
                    10
                    + mod_des
                    + mod_con
                )

            if classe_nome == "Monge":
                ca = max(
                    ca,
                    10
                    + mod_des
                    + mod_sab
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

        # =========================================================
# CONSULTAR PERSONAGENS
# =========================================================

def listar_personagens_jogador(discord_id):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT
                id,
                nome,
                nivel,
                raca,
                subraca,
                classe,
                subclasse,
                antecedente,
                pv_atual,
                pv_maximo,
                ca,
                iniciativa,
                deslocamento
            FROM personagens
            WHERE jogador_id = %s
            ORDER BY nome;
            """,
            (discord_id,)
        )

        resultados = cursor.fetchall()

        return [
            {
                "id": linha[0],
                "nome": linha[1],
                "nivel": linha[2],
                "raca": linha[3],
                "subraca": linha[4],
                "classe": linha[5],
                "subclasse": linha[6],
                "antecedente": linha[7],
                "pv_atual": linha[8],
                "pv_maximo": linha[9],
                "ca": linha[10],
                "iniciativa": linha[11],
                "deslocamento": linha[12],
            }
            for linha in resultados
        ]

    finally:
        cursor.close()
        conexao.close()


def buscar_personagem(personagem_id):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT
                id,
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
                ca,
                iniciativa,
                deslocamento
            FROM personagens
            WHERE id = %s;
            """,
            (personagem_id,)
        )

        linha = cursor.fetchone()

        if linha is None:
            return None

        return {
            "id": linha[0],
            "jogador_id": linha[1],
            "nome": linha[2],
            "nivel": linha[3],
            "raca": linha[4],
            "subraca": linha[5],
            "classe": linha[6],
            "subclasse": linha[7],
            "antecedente": linha[8],
            "pv_atual": linha[9],
            "pv_maximo": linha[10],
            "ca": linha[11],
            "iniciativa": linha[12],
            "deslocamento": linha[13],
        }

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# ATRIBUTOS
# =========================================================

def buscar_atributos_personagem(personagem_id):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT
                forca,
                destreza,
                constituicao,
                inteligencia,
                sabedoria,
                carisma
            FROM atributos
            WHERE personagem_id = %s;
            """,
            (personagem_id,)
        )

        linha = cursor.fetchone()

        if linha is None:
            return None

        return {
            "forca": linha[0],
            "destreza": linha[1],
            "constituicao": linha[2],
            "inteligencia": linha[3],
            "sabedoria": linha[4],
            "carisma": linha[5],
        }

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# PERÍCIAS
# =========================================================

def buscar_pericias_personagem(personagem_id):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT
                acrobacia,
                arcanismo,
                atletismo,
                atuacao,
                enganacao,
                furtividade,
                historia,
                intimidacao,
                intuicao,
                investigacao,
                lidar_animais,
                medicina,
                natureza,
                percepcao,
                persuasao,
                prestidigitacao,
                religiao,
                sobrevivencia
            FROM pericias
            WHERE personagem_id = %s;
            """,
            (personagem_id,)
        )

        linha = cursor.fetchone()

        if linha is None:
            return []

        nomes = [
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
            "lidar_animais",
            "medicina",
            "natureza",
            "percepcao",
            "persuasao",
            "prestidigitacao",
            "religiao",
            "sobrevivencia",
        ]

        return [
            nomes[indice]
            for indice, possui in enumerate(linha)
            if possui
        ]

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# SALVAGUARDAS
# =========================================================

def buscar_salvaguardas_personagem(personagem_id):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT
                forca,
                destreza,
                constituicao,
                inteligencia,
                sabedoria,
                carisma
            FROM salvaguardas
            WHERE personagem_id = %s;
            """,
            (personagem_id,)
        )

        linha = cursor.fetchone()

        if linha is None:
            return []

        nomes = [
            "forca",
            "destreza",
            "constituicao",
            "inteligencia",
            "sabedoria",
            "carisma",
        ]

        return [
            nomes[indice]
            for indice, possui in enumerate(linha)
            if possui
        ]

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# PROFICIÊNCIAS
# =========================================================

def buscar_proficiencias_personagem(personagem_id):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT tipo, nome
            FROM proficiencias
            WHERE personagem_id = %s
            ORDER BY tipo, nome;
            """,
            (personagem_id,)
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
# MAGIAS - INTEGRAÇÃO COM PERSONAGEM
# =========================================================

def listar_truques_mago():
    """
    Retorna os truques (nível 0) disponíveis para Mago.
    Usado pela escolha racial do Alto Elfo.
    """
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT
                m.id,
                m.nome,
                m.escola
            FROM magias m
            JOIN magias_classes mc
                ON mc.magia_id = m.id
            JOIN classes c
                ON c.id = mc.classe_id
            WHERE c.nome = 'Mago'
              AND m.nivel = 0
            ORDER BY m.nome;
            """
        )

        return [
            {
                "id": linha[0],
                "nome": linha[1],
                "escola": linha[2],
            }
            for linha in cursor.fetchall()
        ]

    finally:
        cursor.close()
        conexao.close()


def _buscar_magia_id_cursor(
    cursor,
    nome_magia
):
    cursor.execute(
        """
        SELECT id
        FROM magias
        WHERE LOWER(nome) = LOWER(%s);
        """,
        (nome_magia,)
    )

    resultado = cursor.fetchone()

    if resultado is None:
        raise ValueError(
            f"Magia não encontrada no banco: {nome_magia}"
        )

    return resultado[0]


def _registrar_magia_racial_cursor(
    cursor,
    personagem_id,
    nome_magia,
    origem,
    habilidade_conjuracao,
    nivel_desbloqueio,
    usa_slot=False,
    usos_maximos=None,
    descanso_recuperacao=None,
    nivel_conjuracao=None,
):
    magia_id = _buscar_magia_id_cursor(
        cursor,
        nome_magia
    )

    origem_banco = (
        f"raca:{origem}"
    )

    # Guarda a magia também na lista geral do personagem.
    cursor.execute(
        """
        INSERT INTO magias_personagens (
            personagem_id,
            magia_id,
            conhecida,
            preparada,
            origem
        )
        VALUES (
            %s,
            %s,
            TRUE,
            FALSE,
            %s
        )
        ON CONFLICT (
            personagem_id,
            magia_id,
            origem
        )
        DO UPDATE SET
            conhecida = TRUE;
        """,
        (
            personagem_id,
            magia_id,
            origem_banco,
        )
    )

    # Guarda as regras próprias do traço racial.
    cursor.execute(
        """
        INSERT INTO magias_raciais_personagens (
            personagem_id,
            magia_id,
            origem,
            habilidade_conjuracao,
            nivel_desbloqueio,
            usa_slot,
            usos_maximos,
            usos_gastos,
            descanso_recuperacao,
            nivel_conjuracao
        )
        VALUES (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            0,
            %s,
            %s
        )
        ON CONFLICT (
            personagem_id,
            magia_id,
            origem
        )
        DO UPDATE SET
            habilidade_conjuracao =
                EXCLUDED.habilidade_conjuracao,
            nivel_desbloqueio =
                EXCLUDED.nivel_desbloqueio,
            usa_slot =
                EXCLUDED.usa_slot,
            usos_maximos =
                EXCLUDED.usos_maximos,
            descanso_recuperacao =
                EXCLUDED.descanso_recuperacao,
            nivel_conjuracao =
                EXCLUDED.nivel_conjuracao;
        """,
        (
            personagem_id,
            magia_id,
            origem,
            habilidade_conjuracao,
            nivel_desbloqueio,
            usa_slot,
            usos_maximos,
            descanso_recuperacao,
            nivel_conjuracao,
        )
    )


def sincronizar_slots_personagem(
    personagem_id,
    classe_nome,
    nivel_personagem
):
    """
    Copia para o personagem os espaços previstos em
    slots_magia_classes para a classe e o nível informados.

    Também funciona para Bruxo, pois a progressão de Pacto
    está cadastrada nessa tabela com o nível único do espaço.
    A recuperação curta/longa será tratada pelo Elfo Doméstico.
    """
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT id
            FROM classes
            WHERE nome = %s;
            """,
            (classe_nome,)
        )

        resultado = cursor.fetchone()

        if resultado is None:
            raise ValueError(
                f"Classe não encontrada: {classe_nome}"
            )

        classe_id = resultado[0]

        cursor.execute(
            """
            SELECT
                nivel_magia,
                quantidade
            FROM slots_magia_classes
            WHERE classe_id = %s
              AND nivel_classe = %s
            ORDER BY nivel_magia;
            """,
            (
                classe_id,
                nivel_personagem,
            )
        )

        progressao = cursor.fetchall()

        # Remove níveis que deixaram de existir na progressão
        # atual e recria/atualiza os que são válidos.
        cursor.execute(
            """
            DELETE FROM slots_magia_personagens
            WHERE personagem_id = %s;
            """,
            (personagem_id,)
        )

        for nivel_magia, quantidade in progressao:
            cursor.execute(
                """
                INSERT INTO slots_magia_personagens (
                    personagem_id,
                    nivel_slot,
                    total,
                    usados
                )
                VALUES (
                    %s,
                    %s,
                    %s,
                    0
                );
                """,
                (
                    personagem_id,
                    nivel_magia,
                    quantidade,
                )
            )

        conexao.commit()

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


def registrar_magias_raciais_personagem(
    personagem_id,
    raca_nome,
    subraca_nome,
    nivel_personagem=1,
    truque_alto_elfo=None,
):
    """
    Registra as magias raciais já desbloqueadas no nível atual.

    Casos fixos:
    - Drow
    - Tiefling
    - Gnomo da Floresta

    Caso de escolha:
    - Alto Elfo
    """
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        # Primeiro verifica a sub-raça, depois a raça.
        chave = None

        if (
            subraca_nome
            and subraca_nome in MAGIAS_RACIAIS
        ):
            chave = subraca_nome

        elif raca_nome in MAGIAS_RACIAIS:
            chave = raca_nome

        if chave is not None:
            for regra in MAGIAS_RACIAIS[chave]:

                if (
                    regra["nivel_personagem"]
                    > nivel_personagem
                ):
                    continue

                _registrar_magia_racial_cursor(
                    cursor=cursor,
                    personagem_id=personagem_id,
                    nome_magia=regra["nome"],
                    origem=chave,
                    habilidade_conjuracao=
                        regra["habilidade"],
                    nivel_desbloqueio=
                        regra["nivel_personagem"],
                    usa_slot=
                        regra.get(
                            "usa_slot",
                            False
                        ),
                    usos_maximos=
                        regra.get("usos"),
                    descanso_recuperacao=
                        regra.get("descanso"),
                    nivel_conjuracao=
                        regra.get(
                            "nivel_conjuracao"
                        ),
                )

        # Alto Elfo escolhe um truque da lista de Mago.
        if subraca_nome == "Alto Elfo":

            if not truque_alto_elfo:
                raise ValueError(
                    "O Alto Elfo precisa escolher "
                    "um truque da lista de Mago."
                )

            cursor.execute(
                """
                SELECT
                    m.id
                FROM magias m
                JOIN magias_classes mc
                    ON mc.magia_id = m.id
                JOIN classes c
                    ON c.id = mc.classe_id
                WHERE LOWER(m.nome) = LOWER(%s)
                  AND m.nivel = 0
                  AND c.nome = 'Mago';
                """,
                (truque_alto_elfo,)
            )

            if cursor.fetchone() is None:
                raise ValueError(
                    "O truque escolhido pelo Alto Elfo "
                    "não pertence à lista de Mago."
                )

            _registrar_magia_racial_cursor(
                cursor=cursor,
                personagem_id=personagem_id,
                nome_magia=truque_alto_elfo,
                origem="Alto Elfo",
                habilidade_conjuracao="inteligencia",
                nivel_desbloqueio=1,
                usa_slot=False,
                usos_maximos=None,
                descanso_recuperacao=None,
                nivel_conjuracao=0,
            )

        conexao.commit()

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


def inicializar_sistema_magico_personagem(
    personagem_id,
    classe_nome,
    raca_nome,
    subraca_nome,
    nivel_personagem=1,
    truque_alto_elfo=None,
):
    """
    Inicializa a parte mágica da ficha sem escolher
    magias de classe.

    As magias de classe serão gerenciadas pelo
    Elfo Doméstico.
    """
    sincronizar_slots_personagem(
        personagem_id,
        classe_nome,
        nivel_personagem
    )

    registrar_magias_raciais_personagem(
        personagem_id=personagem_id,
        raca_nome=raca_nome,
        subraca_nome=subraca_nome,
        nivel_personagem=nivel_personagem,
        truque_alto_elfo=truque_alto_elfo,
    )

# =========================================================
# INVENTÁRIO
# =========================================================

def buscar_inventario_personagem(personagem_id):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT
                nome,
                quantidade,
                equipado
            FROM inventario_personagens
            WHERE personagem_id = %s
            ORDER BY nome;
            """,
            (personagem_id,)
        )

        return [
            {
                "nome": linha[0],
                "quantidade": linha[1],
                "equipado": linha[2],
            }
            for linha in cursor.fetchall()
        ]

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# MESTRE
# =========================================================

def jogador_eh_mestre(discord_id):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT eh_mestre
            FROM jogadores
            WHERE discord_id = %s;
            """,
            (discord_id,)
        )

        resultado = cursor.fetchone()

        if resultado is None:
            return False

        return bool(resultado[0])

    finally:
        cursor.close()
        conexao.close()


def pode_acessar_personagem(discord_id, personagem_id):
    personagem = buscar_personagem(
        personagem_id
    )

    if personagem is None:
        return False

    if personagem["jogador_id"] == discord_id:
        return True

    return jogador_eh_mestre(
        discord_id
    )
    # =========================================================
# ALTERAR PV
# =========================================================

def alterar_pv(
    personagem_id,
    valor
):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT
                pv_atual,
                pv_maximo
            FROM personagens
            WHERE id = %s;
            """,
            (personagem_id,)
        )

        resultado = cursor.fetchone()

        if resultado is None:
            raise ValueError(
                "Personagem não encontrado."
            )

        pv_atual = resultado[0]
        pv_maximo = resultado[1]

        novo_pv = pv_atual + valor

        if novo_pv < 0:
            novo_pv = 0

        if novo_pv > pv_maximo:
            novo_pv = pv_maximo

        cursor.execute(
            """
            UPDATE personagens
            SET pv_atual = %s
            WHERE id = %s;
            """,
            (
                novo_pv,
                personagem_id
            )
        )

        conexao.commit()

        return {
            "antes": pv_atual,
            "depois": novo_pv,
            "maximo": pv_maximo,
        }

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()

        # =========================================================
# GERENCIAMENTO DE INVENTÁRIO
# =========================================================

def adicionar_item_inventario(
    personagem_id,
    nome,
    quantidade=1
):
    if quantidade <= 0:
        raise ValueError(
            "A quantidade deve ser maior que zero."
        )

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        # Procura equipamento oficial.
        cursor.execute(
            """
            SELECT id
            FROM equipamentos
            WHERE LOWER(nome) = LOWER(%s);
            """,
            (nome,)
        )

        resultado = cursor.fetchone()

        equipamento_id = (
            resultado[0]
            if resultado
            else None
        )

        # Se já existe no inventário,
        # soma a quantidade.
        cursor.execute(
            """
            SELECT id, quantidade
            FROM inventario_personagens
            WHERE personagem_id = %s
              AND LOWER(nome) = LOWER(%s)
            LIMIT 1;
            """,
            (
                personagem_id,
                nome
            )
        )

        existente = cursor.fetchone()

        if existente:

            item_id = existente[0]

            cursor.execute(
                """
                UPDATE inventario_personagens
                SET quantidade =
                    quantidade + %s
                WHERE id = %s;
                """,
                (
                    quantidade,
                    item_id
                )
            )

        else:

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
                    equipamento_id,
                    nome,
                    quantidade
                )
            )

        conexao.commit()

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


def remover_item_inventario(
    personagem_id,
    nome,
    quantidade=1
):
    if quantidade <= 0:
        raise ValueError(
            "A quantidade deve ser maior que zero."
        )

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT
                id,
                quantidade,
                equipado
            FROM inventario_personagens
            WHERE personagem_id = %s
              AND LOWER(nome) = LOWER(%s)
            LIMIT 1;
            """,
            (
                personagem_id,
                nome
            )
        )

        resultado = cursor.fetchone()

        if resultado is None:
            raise ValueError(
                "Esse item não está no inventário."
            )

        item_id = resultado[0]
        quantidade_atual = resultado[1]

        if quantidade >= quantidade_atual:

            cursor.execute(
                """
                DELETE FROM inventario_personagens
                WHERE id = %s;
                """,
                (item_id,)
            )

        else:

            cursor.execute(
                """
                UPDATE inventario_personagens
                SET quantidade =
                    quantidade - %s
                WHERE id = %s;
                """,
                (
                    quantidade,
                    item_id
                )
            )

        conexao.commit()

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


def alterar_equipado(
    personagem_id,
    nome,
    equipado
):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT
                i.id,
                e.tipo
            FROM inventario_personagens i
            LEFT JOIN equipamentos e
                ON e.id = i.equipamento_id
            WHERE i.personagem_id = %s
              AND LOWER(i.nome) = LOWER(%s)
            LIMIT 1;
            """,
            (
                personagem_id,
                nome
            )
        )

        resultado = cursor.fetchone()

        if resultado is None:
            raise ValueError(
                "Item não encontrado no inventário."
            )

        item_id = resultado[0]
        tipo = resultado[1]

        if tipo not in (
            "armadura",
            "escudo",
            "arma",
            "foco",
        ):
            raise ValueError(
                "Esse item não pode ser equipado."
            )

        # Só uma armadura por vez.
        if equipado and tipo == "armadura":

            cursor.execute(
                """
                UPDATE inventario_personagens
                SET equipado = FALSE
                WHERE personagem_id = %s
                  AND equipamento_id IN (
                      SELECT id
                      FROM equipamentos
                      WHERE tipo = 'armadura'
                  );
                """,
                (personagem_id,)
            )

        cursor.execute(
            """
            UPDATE inventario_personagens
            SET equipado = %s
            WHERE id = %s;
            """,
            (
                equipado,
                item_id
            )
        )

        conexao.commit()

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


def recalcular_ca_personagem(
    personagem_id
):
    personagem = buscar_personagem(
        personagem_id
    )

    if personagem is None:
        raise ValueError(
            "Personagem não encontrado."
        )

    atributos = buscar_atributos_personagem(
        personagem_id
    )

    return calcular_ca_personagem(
        personagem_id,
        personagem["classe"],
        atributos
    )
    # =========================================================
# BAÚ COMUNITÁRIO
# =========================================================

def listar_bau():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT
                id,
                equipamento_id,
                nome,
                quantidade
            FROM bau_comunitario
            ORDER BY nome;
            """
        )

        return [
            {
                "id": linha[0],
                "equipamento_id": linha[1],
                "nome": linha[2],
                "quantidade": linha[3],
            }
            for linha in cursor.fetchall()
        ]

    finally:
        cursor.close()
        conexao.close()


def adicionar_item_bau(
    nome,
    quantidade=1,
    equipamento_id=None
):
    if quantidade <= 0:
        raise ValueError(
            "A quantidade deve ser maior que zero."
        )

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        # Se não recebemos o ID, tenta encontrar
        # o item na tabela oficial de equipamentos.
        if equipamento_id is None:

            cursor.execute(
                """
                SELECT id
                FROM equipamentos
                WHERE LOWER(nome) = LOWER(%s);
                """,
                (nome,)
            )

            resultado = cursor.fetchone()

            if resultado:
                equipamento_id = resultado[0]

        cursor.execute(
            """
            SELECT id
            FROM bau_comunitario
            WHERE LOWER(nome) = LOWER(%s)
            LIMIT 1;
            """,
            (nome,)
        )

        existente = cursor.fetchone()

        if existente:

            cursor.execute(
                """
                UPDATE bau_comunitario
                SET quantidade =
                    quantidade + %s
                WHERE id = %s;
                """,
                (
                    quantidade,
                    existente[0]
                )
            )

        else:

            cursor.execute(
                """
                INSERT INTO bau_comunitario (
                    equipamento_id,
                    nome,
                    quantidade
                )
                VALUES (%s, %s, %s);
                """,
                (
                    equipamento_id,
                    nome,
                    quantidade
                )
            )

        conexao.commit()

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


def remover_item_bau(
    nome,
    quantidade=1
):
    if quantidade <= 0:
        raise ValueError(
            "A quantidade deve ser maior que zero."
        )

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT
                id,
                equipamento_id,
                nome,
                quantidade
            FROM bau_comunitario
            WHERE LOWER(nome) = LOWER(%s)
            LIMIT 1;
            """,
            (nome,)
        )

        resultado = cursor.fetchone()

        if resultado is None:
            raise ValueError(
                "Esse item não está no baú."
            )

        item_id = resultado[0]
        equipamento_id = resultado[1]
        nome_real = resultado[2]
        quantidade_atual = resultado[3]

        if quantidade > quantidade_atual:

            raise ValueError(
                (
                    "O baú possui apenas "
                    f"{quantidade_atual} unidade(s) "
                    f"de {nome_real}."
                )
            )

        if quantidade == quantidade_atual:

            cursor.execute(
                """
                DELETE FROM bau_comunitario
                WHERE id = %s;
                """,
                (item_id,)
            )

        else:

            cursor.execute(
                """
                UPDATE bau_comunitario
                SET quantidade =
                    quantidade - %s
                WHERE id = %s;
                """,
                (
                    quantidade,
                    item_id
                )
            )

        conexao.commit()

        return {
            "equipamento_id": equipamento_id,
            "nome": nome_real,
            "quantidade": quantidade,
        }

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# TRANSFERIR INVENTÁRIO → BAÚ
# =========================================================

def transferir_inventario_para_bau(
    personagem_id,
    nome,
    quantidade=1
):
    if quantidade <= 0:
        raise ValueError(
            "A quantidade deve ser maior que zero."
        )

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT
                id,
                equipamento_id,
                nome,
                quantidade,
                equipado
            FROM inventario_personagens
            WHERE personagem_id = %s
              AND LOWER(nome) = LOWER(%s)
            LIMIT 1;
            """,
            (
                personagem_id,
                nome
            )
        )

        resultado = cursor.fetchone()

        if resultado is None:
            raise ValueError(
                "Esse item não está no inventário."
            )

        item_id = resultado[0]
        equipamento_id = resultado[1]
        nome_real = resultado[2]
        quantidade_atual = resultado[3]
        equipado = resultado[4]

        if quantidade > quantidade_atual:

            raise ValueError(
                (
                    "O personagem possui apenas "
                    f"{quantidade_atual} unidade(s) "
                    f"de {nome_real}."
                )
            )

        # Se só existe uma unidade e ela está equipada,
        # desequipa antes da transferência.
        if (
            equipado
            and quantidade == quantidade_atual
        ):

            cursor.execute(
                """
                UPDATE inventario_personagens
                SET equipado = FALSE
                WHERE id = %s;
                """,
                (item_id,)
            )

        if quantidade == quantidade_atual:

            cursor.execute(
                """
                DELETE FROM inventario_personagens
                WHERE id = %s;
                """,
                (item_id,)
            )

        else:

            cursor.execute(
                """
                UPDATE inventario_personagens
                SET quantidade =
                    quantidade - %s
                WHERE id = %s;
                """,
                (
                    quantidade,
                    item_id
                )
            )

        # Procura se já existe no baú.
        cursor.execute(
            """
            SELECT id
            FROM bau_comunitario
            WHERE LOWER(nome) = LOWER(%s)
            LIMIT 1;
            """,
            (nome_real,)
        )

        item_bau = cursor.fetchone()

        if item_bau:

            cursor.execute(
                """
                UPDATE bau_comunitario
                SET quantidade =
                    quantidade + %s
                WHERE id = %s;
                """,
                (
                    quantidade,
                    item_bau[0]
                )
            )

        else:

            cursor.execute(
                """
                INSERT INTO bau_comunitario (
                    equipamento_id,
                    nome,
                    quantidade
                )
                VALUES (%s, %s, %s);
                """,
                (
                    equipamento_id,
                    nome_real,
                    quantidade
                )
            )

        conexao.commit()

        return {
            "nome": nome_real,
            "quantidade": quantidade,
        }

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# TRANSFERIR BAÚ → INVENTÁRIO
# =========================================================

def transferir_bau_para_inventario(
    personagem_id,
    nome,
    quantidade=1
):
    if quantidade <= 0:
        raise ValueError(
            "A quantidade deve ser maior que zero."
        )

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT
                id,
                equipamento_id,
                nome,
                quantidade
            FROM bau_comunitario
            WHERE LOWER(nome) = LOWER(%s)
            LIMIT 1;
            """,
            (nome,)
        )

        resultado = cursor.fetchone()

        if resultado is None:
            raise ValueError(
                "Esse item não está no baú."
            )

        item_bau_id = resultado[0]
        equipamento_id = resultado[1]
        nome_real = resultado[2]
        quantidade_bau = resultado[3]

        if quantidade > quantidade_bau:

            raise ValueError(
                (
                    "O baú possui apenas "
                    f"{quantidade_bau} unidade(s) "
                    f"de {nome_real}."
                )
            )

        if quantidade == quantidade_bau:

            cursor.execute(
                """
                DELETE FROM bau_comunitario
                WHERE id = %s;
                """,
                (item_bau_id,)
            )

        else:

            cursor.execute(
                """
                UPDATE bau_comunitario
                SET quantidade =
                    quantidade - %s
                WHERE id = %s;
                """,
                (
                    quantidade,
                    item_bau_id
                )
            )

        cursor.execute(
            """
            SELECT id
            FROM inventario_personagens
            WHERE personagem_id = %s
              AND LOWER(nome) = LOWER(%s)
            LIMIT 1;
            """,
            (
                personagem_id,
                nome_real
            )
        )

        item_inventario = cursor.fetchone()

        if item_inventario:

            cursor.execute(
                """
                UPDATE inventario_personagens
                SET quantidade =
                    quantidade + %s
                WHERE id = %s;
                """,
                (
                    quantidade,
                    item_inventario[0]
                )
            )

        else:

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
                    equipamento_id,
                    nome_real,
                    quantidade
                )
            )

        conexao.commit()

        return {
            "nome": nome_real,
            "quantidade": quantidade,
        }

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()