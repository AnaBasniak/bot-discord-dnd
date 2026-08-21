from mini_mestre.database import conectar


# =========================================================
# BUSCAR PERSONAGEM
# =========================================================

def buscar_personagem(
    discord_id,
    nome_personagem
):
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
                subclasse
            FROM personagens
            WHERE jogador_id = %s
              AND LOWER(nome) = LOWER(%s);
            """,
            (
                discord_id,
                nome_personagem,
            )
        )

        resultado = cursor.fetchone()

        if resultado is None:
            return None

        return {
            "id": resultado[0],
            "nome": resultado[1],
            "nivel": resultado[2],
            "raca": resultado[3],
            "subraca": resultado[4],
            "classe": resultado[5],
            "subclasse": resultado[6],
        }

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# LISTAR MAGIAS DISPONÍVEIS PARA A CLASSE
# =========================================================

def listar_magias_classe(
    nome_classe,
    nivel_magia=None
):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        parametros = [nome_classe]

        sql = """
            SELECT
                m.id,
                m.nome,
                m.nivel,
                m.escola,
                m.ritual,
                m.concentracao
            FROM magias m
            JOIN magias_classes mc
                ON mc.magia_id = m.id
            JOIN classes c
                ON c.id = mc.classe_id
            WHERE LOWER(c.nome) = LOWER(%s)
        """

        if nivel_magia is not None:
            sql += """
                AND m.nivel = %s
            """

            parametros.append(
                nivel_magia
            )

        sql += """
            ORDER BY
                m.nivel,
                m.nome;
        """

        cursor.execute(
            sql,
            tuple(parametros)
        )

        resultados = cursor.fetchall()

        return [
            {
                "id": linha[0],
                "nome": linha[1],
                "nivel": linha[2],
                "escola": linha[3],
                "ritual": linha[4],
                "concentracao": linha[5],
            }
            for linha in resultados
        ]

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# BUSCAR MAGIA PELO NOME
# =========================================================

def buscar_magia(
    nome_magia
):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT
                id,
                nome,
                nivel,
                escola,
                tempo_conjuracao,
                alcance,
                componentes,
                duracao,
                descricao,
                ritual,
                concentracao
            FROM magias
            WHERE LOWER(nome) = LOWER(%s);
            """,
            (nome_magia,)
        )

        resultado = cursor.fetchone()

        if resultado is None:
            return None

        return {
            "id": resultado[0],
            "nome": resultado[1],
            "nivel": resultado[2],
            "escola": resultado[3],
            "tempo_conjuracao": resultado[4],
            "alcance": resultado[5],
            "componentes": resultado[6],
            "duracao": resultado[7],
            "descricao": resultado[8],
            "ritual": resultado[9],
            "concentracao": resultado[10],
        }

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# VERIFICAR SE MAGIA PERTENCE À CLASSE
# =========================================================

def magia_pertence_classe(
    magia_id,
    nome_classe
):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT EXISTS (
                SELECT 1
                FROM magias_classes mc
                JOIN classes c
                    ON c.id = mc.classe_id
                WHERE mc.magia_id = %s
                  AND LOWER(c.nome) = LOWER(%s)
            );
            """,
            (
                magia_id,
                nome_classe,
            )
        )

        return cursor.fetchone()[0]

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# ADICIONAR MAGIA AO PERSONAGEM
# =========================================================

def adicionar_magia_personagem(
    personagem_id,
    magia_id,
    preparada=False,
    origem="classe"
):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
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
                %s,
                %s
            )

            ON CONFLICT (
                personagem_id,
                magia_id,
                origem
            )
            DO UPDATE SET
                conhecida = TRUE,
                preparada = EXCLUDED.preparada;
            """,
            (
                personagem_id,
                magia_id,
                preparada,
                origem,
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
# REMOVER MAGIA DO PERSONAGEM
# =========================================================

def remover_magia_personagem(
    personagem_id,
    magia_id,
    origem="classe"
):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            DELETE FROM magias_personagens
            WHERE personagem_id = %s
              AND magia_id = %s
              AND origem = %s;
            """,
            (
                personagem_id,
                magia_id,
                origem,
            )
        )

        removida = (
            cursor.rowcount > 0
        )

        conexao.commit()

        return removida

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# LISTAR MAGIAS DO PERSONAGEM
# =========================================================

def listar_magias_personagem(
    personagem_id
):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT
                m.id,
                m.nome,
                m.nivel,
                m.escola,
                mp.conhecida,
                mp.preparada,
                mp.origem,
                m.ritual,
                m.concentracao
            FROM magias_personagens mp
            JOIN magias m
                ON m.id = mp.magia_id
            WHERE mp.personagem_id = %s
            ORDER BY
                m.nivel,
                m.nome;
            """,
            (personagem_id,)
        )

        resultados = cursor.fetchall()

        return [
            {
                "id": linha[0],
                "nome": linha[1],
                "nivel": linha[2],
                "escola": linha[3],
                "conhecida": linha[4],
                "preparada": linha[5],
                "origem": linha[6],
                "ritual": linha[7],
                "concentracao": linha[8],
            }
            for linha in resultados
        ]

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# PREPARAR MAGIA
# =========================================================

def preparar_magia(
    personagem_id,
    magia_id
):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            UPDATE magias_personagens
            SET preparada = TRUE
            WHERE personagem_id = %s
              AND magia_id = %s
              AND origem = 'classe';
            """,
            (
                personagem_id,
                magia_id,
            )
        )

        alterada = (
            cursor.rowcount > 0
        )

        conexao.commit()

        return alterada

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# DESPREPARAR MAGIA
# =========================================================

def despreparar_magia(
    personagem_id,
    magia_id
):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            UPDATE magias_personagens
            SET preparada = FALSE
            WHERE personagem_id = %s
              AND magia_id = %s
              AND origem = 'classe';
            """,
            (
                personagem_id,
                magia_id,
            )
        )

        alterada = (
            cursor.rowcount > 0
        )

        conexao.commit()

        return alterada

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# LISTAR SLOTS DO PERSONAGEM
# =========================================================

def listar_slots(
    personagem_id
):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT
                nivel_slot,
                total,
                usados
            FROM slots_magia_personagens
            WHERE personagem_id = %s
            ORDER BY nivel_slot;
            """,
            (personagem_id,)
        )

        resultados = cursor.fetchall()

        return [
            {
                "nivel": linha[0],
                "total": linha[1],
                "usados": linha[2],
                "disponiveis": (
                    linha[1] - linha[2]
                ),
            }
            for linha in resultados
        ]

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# GASTAR SLOT
# =========================================================

def gastar_slot(
    personagem_id,
    nivel_slot
):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            UPDATE slots_magia_personagens
            SET usados = usados + 1
            WHERE personagem_id = %s
              AND nivel_slot = %s
              AND usados < total
            RETURNING
                total,
                usados;
            """,
            (
                personagem_id,
                nivel_slot,
            )
        )

        resultado = cursor.fetchone()

        if resultado is None:
            conexao.rollback()
            return None

        conexao.commit()

        return {
            "total": resultado[0],
            "usados": resultado[1],
            "disponiveis": (
                resultado[0]
                - resultado[1]
            ),
        }

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# RECUPERAR TODOS OS SLOTS
# =========================================================

def recuperar_slots(
    personagem_id
):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            UPDATE slots_magia_personagens
            SET usados = 0
            WHERE personagem_id = %s;
            """,
            (personagem_id,)
        )

        conexao.commit()

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# LISTAR MAGIAS RACIAIS
# =========================================================

def listar_magias_raciais(
    personagem_id
):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT
                m.nome,
                m.nivel,
                mr.origem,
                mr.habilidade_conjuracao,
                mr.nivel_desbloqueio,
                mr.usa_slot,
                mr.usos_maximos,
                mr.usos_gastos,
                mr.descanso_recuperacao,
                mr.nivel_conjuracao
            FROM magias_raciais_personagens mr
            JOIN magias m
                ON m.id = mr.magia_id
            WHERE mr.personagem_id = %s
            ORDER BY
                mr.nivel_desbloqueio,
                m.nome;
            """,
            (personagem_id,)
        )

        resultados = cursor.fetchall()

        return [
            {
                "nome": linha[0],
                "nivel": linha[1],
                "origem": linha[2],
                "habilidade": linha[3],
                "nivel_desbloqueio": linha[4],
                "usa_slot": linha[5],
                "usos_maximos": linha[6],
                "usos_gastos": linha[7],
                "descanso": linha[8],
                "nivel_conjuracao": linha[9],
            }
            for linha in resultados
        ]

    finally:
        cursor.close()
        conexao.close()