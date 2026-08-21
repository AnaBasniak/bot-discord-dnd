from mini_mestre.database import conectar


# =========================================================
# BUSCAR PERSONAGEM
# =========================================================

def buscar_personagem_conjuracao(personagem_id):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT
                id,
                nome,
                nivel,
                classe
            FROM personagens
            WHERE id = %s;
            """,
            (personagem_id,)
        )

        resultado = cursor.fetchone()

        if resultado is None:
            return None

        return {
            "id": resultado[0],
            "nome": resultado[1],
            "nivel": resultado[2],
            "classe": resultado[3],
        }

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# BUSCAR MAGIA DO PERSONAGEM
# =========================================================

def buscar_magia_personagem(
    personagem_id,
    nome_magia
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
                mp.origem
            FROM magias_personagens mp
            JOIN magias m
                ON m.id = mp.magia_id
            WHERE mp.personagem_id = %s
              AND LOWER(m.nome) = LOWER(%s)
            ORDER BY
                CASE
                    WHEN mp.origem LIKE 'raca:%%'
                    THEN 0
                    ELSE 1
                END;
            """,
            (
                personagem_id,
                nome_magia,
            )
        )

        resultados = cursor.fetchall()

        if not resultados:
            return None

        return [
            {
                "id": linha[0],
                "nome": linha[1],
                "nivel": linha[2],
                "escola": linha[3],
                "conhecida": linha[4],
                "preparada": linha[5],
                "origem": linha[6],
            }
            for linha in resultados
        ]

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# BUSCAR REGRA RACIAL
# =========================================================

def buscar_regra_magia_racial(
    personagem_id,
    magia_id
):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            SELECT
                origem,
                habilidade_conjuracao,
                usa_slot,
                usos_maximos,
                usos_gastos,
                descanso_recuperacao,
                nivel_conjuracao
            FROM magias_raciais_personagens
            WHERE personagem_id = %s
              AND magia_id = %s;
            """,
            (
                personagem_id,
                magia_id,
            )
        )

        resultado = cursor.fetchone()

        if resultado is None:
            return None

        return {
            "origem": resultado[0],
            "habilidade_conjuracao": resultado[1],
            "usa_slot": resultado[2],
            "usos_maximos": resultado[3],
            "usos_gastos": resultado[4],
            "descanso_recuperacao": resultado[5],
            "nivel_conjuracao": resultado[6],
        }

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# LISTAR SLOTS DISPONÍVEIS
# =========================================================

def listar_slots_disponiveis(personagem_id):
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

        return [
            {
                "nivel": linha[0],
                "total": linha[1],
                "usados": linha[2],
                "disponiveis": linha[1] - linha[2],
            }
            for linha in cursor.fetchall()
        ]

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# ESCOLHER SLOT
# =========================================================

def escolher_slot(
    personagem_id,
    nivel_minimo
):
    slots = listar_slots_disponiveis(
        personagem_id
    )

    for slot in slots:

        if slot["nivel"] < nivel_minimo:
            continue

        if slot["disponiveis"] <= 0:
            continue

        return slot["nivel"]

    return None


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
            "nivel": nivel_slot,
            "total": resultado[0],
            "usados": resultado[1],
            "restantes":
                resultado[0] - resultado[1],
        }

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# GASTAR USO RACIAL
# =========================================================

def gastar_uso_racial(
    personagem_id,
    magia_id
):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            UPDATE magias_raciais_personagens
            SET usos_gastos = usos_gastos + 1
            WHERE personagem_id = %s
              AND magia_id = %s
              AND usos_maximos IS NOT NULL
              AND usos_gastos < usos_maximos
            RETURNING
                usos_maximos,
                usos_gastos;
            """,
            (
                personagem_id,
                magia_id,
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
            "restantes":
                resultado[0] - resultado[1],
        }

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


# =========================================================
# CONJURAR MAGIA RACIAL
# =========================================================

def _conjurar_magia_racial(
    personagem_id,
    magia,
    regra_racial
):

    if (
        not regra_racial["usa_slot"]
        and
        regra_racial["usos_maximos"] is None
    ):

        return {
            "sucesso": True,
            "tipo": "racial_livre",
            "magia": magia["nome"],
            "nivel_magia": magia["nivel"],
            "origem": regra_racial["origem"],
            "mensagem":
                "Magia racial conjurada sem gastar slot.",
        }

    if (
        not regra_racial["usa_slot"]
        and
        regra_racial["usos_maximos"] is not None
    ):

        resultado = gastar_uso_racial(
            personagem_id,
            magia["id"]
        )

        if resultado is None:

            return {
                "sucesso": False,
                "erro":
                    "Você já gastou todos os usos "
                    "raciais dessa magia.",
            }

        return {
            "sucesso": True,
            "tipo": "racial",
            "magia": magia["nome"],
            "nivel_magia": magia["nivel"],
            "origem": regra_racial["origem"],
            "usos_restantes":
                resultado["restantes"],
            "mensagem":
                "Magia racial conjurada.",
        }

    nivel_minimo = (
        regra_racial["nivel_conjuracao"]
        if regra_racial["nivel_conjuracao"] is not None
        else magia["nivel"]
    )

    nivel_slot = escolher_slot(
        personagem_id,
        nivel_minimo
    )

    if nivel_slot is None:

        return {
            "sucesso": False,
            "erro":
                "Você não possui um espaço de magia "
                "disponível para conjurar essa magia.",
        }

    resultado = gastar_slot(
        personagem_id,
        nivel_slot
    )

    if resultado is None:

        return {
            "sucesso": False,
            "erro":
                "Não foi possível gastar o espaço "
                "de magia.",
        }

    return {
        "sucesso": True,
        "tipo": "racial_slot",
        "magia": magia["nome"],
        "nivel_magia": magia["nivel"],
        "nivel_slot": nivel_slot,
        "slots_restantes":
            resultado["restantes"],
        "origem": regra_racial["origem"],
        "mensagem":
            "Magia racial conjurada usando "
            "um espaço de magia.",
    }


# =========================================================
# CONJURAR
# =========================================================

def conjurar_magia(
    personagem_id,
    nome_magia
):

    personagem = buscar_personagem_conjuracao(
        personagem_id
    )

    if personagem is None:

        return {
            "sucesso": False,
            "erro": "Personagem não encontrado.",
        }

    magias = buscar_magia_personagem(
        personagem_id,
        nome_magia
    )

    if not magias:

        return {
            "sucesso": False,
            "erro":
                "Essa magia não pertence ao personagem.",
        }

    # =====================================================
    # ORIGEM RACIAL TEM PRIORIDADE
    # =====================================================

    for magia in magias:

        if (
            magia["origem"]
            and
            magia["origem"].startswith("raca:")
        ):

            regra_racial = (
                buscar_regra_magia_racial(
                    personagem_id,
                    magia["id"]
                )
            )

            if regra_racial is not None:

                return _conjurar_magia_racial(
                    personagem_id,
                    magia,
                    regra_racial
                )

    # =====================================================
    # MAGIA DE CLASSE
    # =====================================================

    magia = magias[0]

    if magia["nivel"] == 0:

        return {
            "sucesso": True,
            "tipo": "truque",
            "magia": magia["nome"],
            "nivel_magia": 0,
            "mensagem":
                "Truque conjurado sem gastar slot.",
        }

    # =====================================================
    # VERIFICAR PREPARAÇÃO / CONHECIMENTO
    # =====================================================

    classes_preparam = {
        "Clérigo",
        "Druida",
        "Mago",
        "Paladino",
    }

    if personagem["classe"] in classes_preparam:

        if not magia["preparada"]:

            return {
                "sucesso": False,
                "erro":
                    "Essa magia não está preparada.",
            }

    else:

        if not magia["conhecida"]:

            return {
                "sucesso": False,
                "erro":
                    "Essa magia não está conhecida.",
            }

    # =====================================================
    # BRUXO
    # =====================================================

    if personagem["classe"] == "Bruxo":

        slots = listar_slots_disponiveis(
            personagem_id
        )

        slot_pacto = None

        for slot in slots:

            if slot["disponiveis"] <= 0:
                continue

            if slot["nivel"] < magia["nivel"]:
                continue

            slot_pacto = slot["nivel"]
            break

        if slot_pacto is None:

            return {
                "sucesso": False,
                "erro":
                    "Você não possui espaço de "
                    "Magia de Pacto disponível.",
            }

        resultado = gastar_slot(
            personagem_id,
            slot_pacto
        )

        if resultado is None:

            return {
                "sucesso": False,
                "erro":
                    "Não foi possível gastar o "
                    "espaço de Magia de Pacto.",
            }

        return {
            "sucesso": True,
            "tipo": "pacto",
            "magia": magia["nome"],
            "nivel_magia": magia["nivel"],
            "nivel_slot": slot_pacto,
            "slots_restantes":
                resultado["restantes"],
            "mensagem":
                "Magia conjurada usando "
                "Magia de Pacto.",
        }

    # =====================================================
    # DEMAIS CLASSES
    # =====================================================

    nivel_slot = escolher_slot(
        personagem_id,
        magia["nivel"]
    )

    if nivel_slot is None:

        return {
            "sucesso": False,
            "erro":
                "Você não possui um espaço de magia "
                "disponível para conjurar essa magia.",
        }

    resultado = gastar_slot(
        personagem_id,
        nivel_slot
    )

    if resultado is None:

        return {
            "sucesso": False,
            "erro":
                "Não foi possível gastar o espaço "
                "de magia.",
        }

    return {
        "sucesso": True,
        "tipo": "slot",
        "magia": magia["nome"],
        "nivel_magia": magia["nivel"],
        "nivel_slot": nivel_slot,
        "slots_restantes":
            resultado["restantes"],
        "mensagem":
            "Magia conjurada com sucesso.",
    }


# =========================================================
# RECUPERAR SLOTS
# =========================================================

def recuperar_slots(personagem_id):

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
# RECUPERAR USOS RACIAIS
# =========================================================

def recuperar_usos_raciais(
    personagem_id,
    tipo_descanso
):

    conexao = conectar()
    cursor = conexao.cursor()

    try:

        if tipo_descanso == "curto":

            cursor.execute(
                """
                UPDATE magias_raciais_personagens
                SET usos_gastos = 0
                WHERE personagem_id = %s
                  AND descanso_recuperacao = 'curto';
                """,
                (personagem_id,)
            )

        elif tipo_descanso == "longo":

            cursor.execute(
                """
                UPDATE magias_raciais_personagens
                SET usos_gastos = 0
                WHERE personagem_id = %s
                  AND descanso_recuperacao IN (
                      'curto',
                      'longo'
                  );
                """,
                (personagem_id,)
            )

        else:

            raise ValueError(
                "Tipo de descanso inválido."
            )

        conexao.commit()

    except Exception:

        conexao.rollback()
        raise

    finally:

        cursor.close()
        conexao.close()


# =========================================================
# DESCANSO CURTO
# =========================================================

def descanso_curto(personagem_id):

    personagem = buscar_personagem_conjuracao(
        personagem_id
    )

    if personagem is None:

        return {
            "sucesso": False,
            "erro":
                "Personagem não encontrado.",
        }

    recuperou_slots = False

    if personagem["classe"] == "Bruxo":

        recuperar_slots(
            personagem_id
        )

        recuperou_slots = True

    recuperar_usos_raciais(
        personagem_id,
        "curto"
    )

    return {
        "sucesso": True,
        "classe":
            personagem["classe"],
        "recuperou_slots":
            recuperou_slots,
        "mensagem":
            "Descanso curto concluído.",
    }


# =========================================================
# DESCANSO LONGO
# =========================================================

def descanso_longo(personagem_id):

    personagem = buscar_personagem_conjuracao(
        personagem_id
    )

    if personagem is None:

        return {
            "sucesso": False,
            "erro":
                "Personagem não encontrado.",
        }

    recuperar_slots(
        personagem_id
    )

    recuperar_usos_raciais(
        personagem_id,
        "longo"
    )

    return {
        "sucesso": True,
        "classe":
            personagem["classe"],
        "recuperou_slots":
            True,
        "mensagem":
            "Descanso longo concluído.",
    }