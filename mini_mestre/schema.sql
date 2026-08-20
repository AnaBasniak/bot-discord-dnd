-- =========================================================
-- MINI MESTRE - BANCO DE DADOS
-- D&D 5e 2014
-- =========================================================


-- =========================================================
-- JOGADORES
-- =========================================================

CREATE TABLE jogadores (
    discord_id BIGINT PRIMARY KEY,
    nome_discord TEXT NOT NULL,
    eh_mestre BOOLEAN NOT NULL DEFAULT FALSE,
    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


-- =========================================================
-- PERSONAGENS
-- =========================================================

CREATE TABLE personagens (
    id SERIAL PRIMARY KEY,

    jogador_id BIGINT NOT NULL,

    nome TEXT NOT NULL,
    nivel INTEGER NOT NULL DEFAULT 1,

    raca TEXT,
    subraca TEXT,

    classe TEXT,
    subclasse TEXT,

    antecedente TEXT,

    pv_atual INTEGER NOT NULL DEFAULT 0,
    pv_maximo INTEGER NOT NULL DEFAULT 0,

    ca INTEGER NOT NULL DEFAULT 10,
    iniciativa INTEGER NOT NULL DEFAULT 0,

    deslocamento INTEGER NOT NULL DEFAULT 30,

    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_personagem_jogador
        FOREIGN KEY (jogador_id)
        REFERENCES jogadores(discord_id)
        ON DELETE CASCADE
);


-- =========================================================
-- ATRIBUTOS DO PERSONAGEM
-- =========================================================

CREATE TABLE atributos (
    personagem_id INTEGER PRIMARY KEY,

    forca INTEGER NOT NULL DEFAULT 10,
    destreza INTEGER NOT NULL DEFAULT 10,
    constituicao INTEGER NOT NULL DEFAULT 10,
    inteligencia INTEGER NOT NULL DEFAULT 10,
    sabedoria INTEGER NOT NULL DEFAULT 10,
    carisma INTEGER NOT NULL DEFAULT 10,

    CONSTRAINT fk_atributos_personagem
        FOREIGN KEY (personagem_id)
        REFERENCES personagens(id)
        ON DELETE CASCADE
);


-- =========================================================
-- PERÍCIAS DO PERSONAGEM
-- =========================================================

CREATE TABLE pericias (
    personagem_id INTEGER PRIMARY KEY,

    acrobacia BOOLEAN NOT NULL DEFAULT FALSE,
    arcanismo BOOLEAN NOT NULL DEFAULT FALSE,
    atletismo BOOLEAN NOT NULL DEFAULT FALSE,
    atuacao BOOLEAN NOT NULL DEFAULT FALSE,
    enganacao BOOLEAN NOT NULL DEFAULT FALSE,
    furtividade BOOLEAN NOT NULL DEFAULT FALSE,
    historia BOOLEAN NOT NULL DEFAULT FALSE,
    intimidacao BOOLEAN NOT NULL DEFAULT FALSE,
    intuicao BOOLEAN NOT NULL DEFAULT FALSE,
    investigacao BOOLEAN NOT NULL DEFAULT FALSE,
    adestrar_animais BOOLEAN NOT NULL DEFAULT FALSE,
    medicina BOOLEAN NOT NULL DEFAULT FALSE,
    natureza BOOLEAN NOT NULL DEFAULT FALSE,
    percepcao BOOLEAN NOT NULL DEFAULT FALSE,
    persuasao BOOLEAN NOT NULL DEFAULT FALSE,
    prestidigitacao BOOLEAN NOT NULL DEFAULT FALSE,
    religiao BOOLEAN NOT NULL DEFAULT FALSE,
    sobrevivencia BOOLEAN NOT NULL DEFAULT FALSE,

    CONSTRAINT fk_pericias_personagem
        FOREIGN KEY (personagem_id)
        REFERENCES personagens(id)
        ON DELETE CASCADE
);


-- =========================================================
-- SALVAGUARDAS DO PERSONAGEM
-- =========================================================

CREATE TABLE salvaguardas (
    personagem_id INTEGER PRIMARY KEY,

    forca BOOLEAN NOT NULL DEFAULT FALSE,
    destreza BOOLEAN NOT NULL DEFAULT FALSE,
    constituicao BOOLEAN NOT NULL DEFAULT FALSE,
    inteligencia BOOLEAN NOT NULL DEFAULT FALSE,
    sabedoria BOOLEAN NOT NULL DEFAULT FALSE,
    carisma BOOLEAN NOT NULL DEFAULT FALSE,

    CONSTRAINT fk_salvaguardas_personagem
        FOREIGN KEY (personagem_id)
        REFERENCES personagens(id)
        ON DELETE CASCADE
);


-- =========================================================
-- PROFICIÊNCIAS DO PERSONAGEM
-- =========================================================

CREATE TABLE proficiencias (
    id SERIAL PRIMARY KEY,

    personagem_id INTEGER NOT NULL,

    tipo TEXT NOT NULL,
    nome TEXT NOT NULL,

    CONSTRAINT fk_proficiencia_personagem
        FOREIGN KEY (personagem_id)
        REFERENCES personagens(id)
        ON DELETE CASCADE,

    CONSTRAINT uq_proficiencia_personagem
        UNIQUE (personagem_id, tipo, nome)
);


-- =========================================================
-- RAÇAS
-- =========================================================

CREATE TABLE racas (
    id SERIAL PRIMARY KEY,

    nome TEXT NOT NULL UNIQUE,
    descricao TEXT,

    deslocamento INTEGER NOT NULL DEFAULT 30
);


-- =========================================================
-- SUB-RAÇAS
-- =========================================================

CREATE TABLE subracas (
    id SERIAL PRIMARY KEY,

    raca_id INTEGER NOT NULL,

    nome TEXT NOT NULL,
    descricao TEXT,

    CONSTRAINT fk_subraca_raca
        FOREIGN KEY (raca_id)
        REFERENCES racas(id)
        ON DELETE CASCADE,

    CONSTRAINT uq_subraca_nome
        UNIQUE (raca_id, nome)
);


-- =========================================================
-- BÔNUS RACIAIS DE ATRIBUTOS
-- =========================================================

CREATE TABLE bonus_atributos_raciais (
    id SERIAL PRIMARY KEY,

    raca_id INTEGER,
    subraca_id INTEGER,

    atributo TEXT NOT NULL,
    bonus INTEGER NOT NULL,

    CONSTRAINT fk_bonus_raca
        FOREIGN KEY (raca_id)
        REFERENCES racas(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_bonus_subraca
        FOREIGN KEY (subraca_id)
        REFERENCES subracas(id)
        ON DELETE CASCADE,

    CONSTRAINT chk_bonus_origem
        CHECK (
            raca_id IS NOT NULL
            OR subraca_id IS NOT NULL
        )
);


-- =========================================================
-- CARACTERÍSTICAS RACIAIS
-- =========================================================

CREATE TABLE caracteristicas_raciais (
    id SERIAL PRIMARY KEY,

    raca_id INTEGER,
    subraca_id INTEGER,

    nome TEXT NOT NULL,
    descricao TEXT,

    CONSTRAINT fk_caracteristica_raca
        FOREIGN KEY (raca_id)
        REFERENCES racas(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_caracteristica_subraca
        FOREIGN KEY (subraca_id)
        REFERENCES subracas(id)
        ON DELETE CASCADE,

    CONSTRAINT chk_caracteristica_origem
        CHECK (
            raca_id IS NOT NULL
            OR subraca_id IS NOT NULL
        )
);


-- =========================================================
-- ESCOLHAS RACIAIS
-- =========================================================

CREATE TABLE escolhas_raciais (
    id SERIAL PRIMARY KEY,

    raca_id INTEGER,
    subraca_id INTEGER,

    tipo TEXT NOT NULL,
    titulo TEXT NOT NULL,
    quantidade INTEGER NOT NULL DEFAULT 1,

    CONSTRAINT fk_escolha_raca
        FOREIGN KEY (raca_id)
        REFERENCES racas(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_escolha_subraca
        FOREIGN KEY (subraca_id)
        REFERENCES subracas(id)
        ON DELETE CASCADE,

    CONSTRAINT chk_escolha_origem
        CHECK (
            raca_id IS NOT NULL
            OR subraca_id IS NOT NULL
        )
);


-- =========================================================
-- CLASSES
-- =========================================================

CREATE TABLE classes (
    id SERIAL PRIMARY KEY,

    nome TEXT NOT NULL UNIQUE,
    descricao TEXT,

    dado_vida INTEGER NOT NULL,

    nivel_maximo INTEGER NOT NULL DEFAULT 20,

    quantidade_pericias INTEGER NOT NULL DEFAULT 2
);


-- =========================================================
-- SUBCLASSES
-- =========================================================

CREATE TABLE subclasses (
    id SERIAL PRIMARY KEY,

    classe_id INTEGER NOT NULL,

    nome TEXT NOT NULL,
    descricao TEXT,

    nivel_escolha INTEGER,

    CONSTRAINT fk_subclasse_classe
        FOREIGN KEY (classe_id)
        REFERENCES classes(id)
        ON DELETE CASCADE,

    CONSTRAINT uq_subclasse_nome
        UNIQUE (classe_id, nome)
);


-- =========================================================
-- SALVAGUARDAS DAS CLASSES
-- =========================================================

CREATE TABLE salvaguardas_classes (
    id SERIAL PRIMARY KEY,

    classe_id INTEGER NOT NULL,
    atributo TEXT NOT NULL,

    CONSTRAINT fk_salvaguarda_classe
        FOREIGN KEY (classe_id)
        REFERENCES classes(id)
        ON DELETE CASCADE,

    CONSTRAINT uq_salvaguarda_classe
        UNIQUE (classe_id, atributo)
);


-- =========================================================
-- PERÍCIAS DISPONÍVEIS PARA AS CLASSES
-- =========================================================

CREATE TABLE pericias_classes (
    id SERIAL PRIMARY KEY,

    classe_id INTEGER NOT NULL,
    pericia TEXT NOT NULL,

    CONSTRAINT fk_pericia_classe
        FOREIGN KEY (classe_id)
        REFERENCES classes(id)
        ON DELETE CASCADE,

    CONSTRAINT uq_pericia_classe
        UNIQUE (classe_id, pericia)
);


-- =========================================================
-- PROFICIÊNCIAS DAS CLASSES
-- =========================================================

CREATE TABLE proficiencias_classes (
    id SERIAL PRIMARY KEY,

    classe_id INTEGER NOT NULL,

    tipo TEXT NOT NULL,
    nome TEXT NOT NULL,

    CONSTRAINT fk_proficiencia_classe
        FOREIGN KEY (classe_id)
        REFERENCES classes(id)
        ON DELETE CASCADE,

    CONSTRAINT uq_proficiencia_classe
        UNIQUE (classe_id, tipo, nome)
);


-- =========================================================
-- CARACTERÍSTICAS DAS CLASSES
-- =========================================================

CREATE TABLE caracteristicas_classes (
    id SERIAL PRIMARY KEY,

    classe_id INTEGER NOT NULL,

    nivel INTEGER NOT NULL,

    nome TEXT NOT NULL,
    descricao TEXT,

    CONSTRAINT fk_caracteristica_classe
        FOREIGN KEY (classe_id)
        REFERENCES classes(id)
        ON DELETE CASCADE,

    CONSTRAINT uq_caracteristica_classe
        UNIQUE (classe_id, nivel, nome)
);


-- =========================================================
-- CARACTERÍSTICAS DAS SUBCLASSES
-- =========================================================

CREATE TABLE caracteristicas_subclasses (
    id SERIAL PRIMARY KEY,

    subclasse_id INTEGER NOT NULL,

    nivel INTEGER NOT NULL,

    nome TEXT NOT NULL,
    descricao TEXT,

    CONSTRAINT fk_caracteristica_subclasse
        FOREIGN KEY (subclasse_id)
        REFERENCES subclasses(id)
        ON DELETE CASCADE,

    CONSTRAINT uq_caracteristica_subclasse
        UNIQUE (subclasse_id, nivel, nome)
);


-- =========================================================
-- ANTECEDENTES
-- =========================================================

CREATE TABLE antecedentes (
    id SERIAL PRIMARY KEY,

    nome TEXT NOT NULL UNIQUE,
    descricao TEXT
);


-- =========================================================
-- PERÍCIAS DOS ANTECEDENTES
-- =========================================================

CREATE TABLE pericias_antecedentes (
    id SERIAL PRIMARY KEY,

    antecedente_id INTEGER NOT NULL,

    pericia TEXT NOT NULL,

    CONSTRAINT fk_pericia_antecedente
        FOREIGN KEY (antecedente_id)
        REFERENCES antecedentes(id)
        ON DELETE CASCADE,

    CONSTRAINT uq_pericia_antecedente
        UNIQUE (antecedente_id, pericia)
);


-- =========================================================
-- PROFICIÊNCIAS DOS ANTECEDENTES
-- =========================================================

CREATE TABLE proficiencias_antecedentes (
    id SERIAL PRIMARY KEY,

    antecedente_id INTEGER NOT NULL,

    tipo TEXT NOT NULL,
    nome TEXT NOT NULL,

    CONSTRAINT fk_proficiencia_antecedente
        FOREIGN KEY (antecedente_id)
        REFERENCES antecedentes(id)
        ON DELETE CASCADE,

    CONSTRAINT uq_proficiencia_antecedente
        UNIQUE (antecedente_id, tipo, nome)
);


-- =========================================================
-- IDIOMAS DOS ANTECEDENTES
-- =========================================================

CREATE TABLE idiomas_antecedentes (
    id SERIAL PRIMARY KEY,

    antecedente_id INTEGER NOT NULL,

    quantidade INTEGER NOT NULL DEFAULT 0,

    CONSTRAINT fk_idioma_antecedente
        FOREIGN KEY (antecedente_id)
        REFERENCES antecedentes(id)
        ON DELETE CASCADE
);


-- =========================================================
-- CARACTERÍSTICAS DOS ANTECEDENTES
-- =========================================================

CREATE TABLE caracteristicas_antecedentes (
    id SERIAL PRIMARY KEY,

    antecedente_id INTEGER NOT NULL,

    nome TEXT NOT NULL,
    descricao TEXT,

    CONSTRAINT fk_caracteristica_antecedente
        FOREIGN KEY (antecedente_id)
        REFERENCES antecedentes(id)
        ON DELETE CASCADE,

    CONSTRAINT uq_caracteristica_antecedente
        UNIQUE (antecedente_id, nome)
);


-- =========================================================
-- EQUIPAMENTOS
-- =========================================================

CREATE TABLE equipamentos (
    id SERIAL PRIMARY KEY,

    nome TEXT NOT NULL UNIQUE,

    tipo TEXT NOT NULL,

    descricao TEXT,

    ca_base INTEGER,

    limite_destreza INTEGER,

    bonus_ca INTEGER NOT NULL DEFAULT 0
);


-- =========================================================
-- ESCOLHAS DE EQUIPAMENTO DAS CLASSES
-- =========================================================

CREATE TABLE escolhas_equipamentos_classes (
    id SERIAL PRIMARY KEY,

    classe_id INTEGER NOT NULL,

    grupo INTEGER NOT NULL,

    quantidade INTEGER NOT NULL DEFAULT 1,

    titulo TEXT NOT NULL,

    CONSTRAINT fk_escolha_equipamento_classe
        FOREIGN KEY (classe_id)
        REFERENCES classes(id)
        ON DELETE CASCADE
);


-- =========================================================
-- OPÇÕES DAS ESCOLHAS DE EQUIPAMENTO
-- =========================================================

CREATE TABLE opcoes_equipamentos_classes (
    id SERIAL PRIMARY KEY,

    escolha_id INTEGER NOT NULL,

    opcao INTEGER NOT NULL,

    equipamento_id INTEGER,

    categoria TEXT,

    quantidade INTEGER NOT NULL DEFAULT 1,

    CONSTRAINT fk_opcao_escolha
        FOREIGN KEY (escolha_id)
        REFERENCES escolhas_equipamentos_classes(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_opcao_equipamento
        FOREIGN KEY (equipamento_id)
        REFERENCES equipamentos(id)
        ON DELETE CASCADE,

    CONSTRAINT chk_opcao_equipamento
        CHECK (
            equipamento_id IS NOT NULL
            OR categoria IS NOT NULL
        )
);


-- =========================================================
-- INVENTÁRIO DOS PERSONAGENS
-- =========================================================

CREATE TABLE inventario_personagens (
    id SERIAL PRIMARY KEY,

    personagem_id INTEGER NOT NULL,

    equipamento_id INTEGER,

    nome TEXT NOT NULL,

    quantidade INTEGER NOT NULL DEFAULT 1,

    equipado BOOLEAN NOT NULL DEFAULT FALSE,

    CONSTRAINT fk_inventario_personagem
        FOREIGN KEY (personagem_id)
        REFERENCES personagens(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_inventario_equipamento
        FOREIGN KEY (equipamento_id)
        REFERENCES equipamentos(id)
        ON DELETE SET NULL
);


-- =========================================================
-- MAGIAS
-- =========================================================

CREATE TABLE magias (
    id SERIAL PRIMARY KEY,

    nome TEXT NOT NULL UNIQUE,

    nivel INTEGER NOT NULL DEFAULT 0,

    escola TEXT,

    tempo_conjuracao TEXT,

    alcance TEXT,

    componentes TEXT,

    duracao TEXT,

    descricao TEXT,

    ritual BOOLEAN NOT NULL DEFAULT FALSE,

    concentracao BOOLEAN NOT NULL DEFAULT FALSE
);


-- =========================================================
-- MAGIAS DISPONÍVEIS PARA CADA CLASSE
-- =========================================================

CREATE TABLE magias_classes (
    id SERIAL PRIMARY KEY,

    magia_id INTEGER NOT NULL,

    classe_id INTEGER NOT NULL,

    CONSTRAINT fk_magia_classe_magia
        FOREIGN KEY (magia_id)
        REFERENCES magias(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_magia_classe_classe
        FOREIGN KEY (classe_id)
        REFERENCES classes(id)
        ON DELETE CASCADE,

    CONSTRAINT uq_magia_classe
        UNIQUE (magia_id, classe_id)
);


-- =========================================================
-- MAGIAS DO PERSONAGEM
-- =========================================================

CREATE TABLE magias_personagens (
    id SERIAL PRIMARY KEY,

    personagem_id INTEGER NOT NULL,

    magia_id INTEGER NOT NULL,

    preparada BOOLEAN NOT NULL DEFAULT FALSE,

    CONSTRAINT fk_magia_personagem
        FOREIGN KEY (personagem_id)
        REFERENCES personagens(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_magia_personagem_magia
        FOREIGN KEY (magia_id)
        REFERENCES magias(id)
        ON DELETE CASCADE,

    CONSTRAINT uq_magia_personagem
        UNIQUE (personagem_id, magia_id)
);


-- =========================================================
-- SLOTS DE MAGIA DO PERSONAGEM
-- =========================================================

CREATE TABLE slots_magia_personagens (
    id SERIAL PRIMARY KEY,

    personagem_id INTEGER NOT NULL,

    nivel_slot INTEGER NOT NULL,

    total INTEGER NOT NULL DEFAULT 0,

    usados INTEGER NOT NULL DEFAULT 0,

    CONSTRAINT fk_slot_personagem
        FOREIGN KEY (personagem_id)
        REFERENCES personagens(id)
        ON DELETE CASCADE,

    CONSTRAINT uq_slot_personagem
        UNIQUE (personagem_id, nivel_slot),

    CONSTRAINT chk_nivel_slot
        CHECK (
            nivel_slot BETWEEN 1 AND 9
        ),

    CONSTRAINT chk_slots_validos
        CHECK (
            total >= 0
            AND usados >= 0
            AND usados <= total
        )
);


-- =========================================================
-- BAÚ COMUNITÁRIO
-- =========================================================

CREATE TABLE bau_comunitario (
    id SERIAL PRIMARY KEY,

    equipamento_id INTEGER,

    nome TEXT NOT NULL,

    quantidade INTEGER NOT NULL DEFAULT 1,

    CONSTRAINT fk_bau_equipamento
        FOREIGN KEY (equipamento_id)
        REFERENCES equipamentos(id)
        ON DELETE SET NULL
);


-- =========================================================
-- NPCS
-- =========================================================

CREATE TABLE npcs (
    id SERIAL PRIMARY KEY,

    nome TEXT NOT NULL,

    descricao TEXT,

    observacoes TEXT,

    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


-- =========================================================
-- IMAGENS DOS NPCS
-- =========================================================

CREATE TABLE imagens_npc (
    id SERIAL PRIMARY KEY,

    npc_id INTEGER NOT NULL,

    url TEXT NOT NULL,

    descricao TEXT,

    CONSTRAINT fk_imagem_npc
        FOREIGN KEY (npc_id)
        REFERENCES npcs(id)
        ON DELETE CASCADE
);


-- =========================================================
-- COMBATES
-- =========================================================

CREATE TABLE combates (
    id SERIAL PRIMARY KEY,

    ativo BOOLEAN NOT NULL DEFAULT TRUE,

    rodada INTEGER NOT NULL DEFAULT 1,

    turno_atual INTEGER NOT NULL DEFAULT 0,

    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    encerrado_em TIMESTAMP
);


-- =========================================================
-- PARTICIPANTES DO COMBATE
-- =========================================================

CREATE TABLE participantes_combate (
    id SERIAL PRIMARY KEY,

    combate_id INTEGER NOT NULL,

    personagem_id INTEGER,

    npc_id INTEGER,

    nome TEXT NOT NULL,

    iniciativa INTEGER NOT NULL DEFAULT 0,

    pv_atual INTEGER,

    ordem INTEGER NOT NULL DEFAULT 0,

    CONSTRAINT fk_participante_combate
        FOREIGN KEY (combate_id)
        REFERENCES combates(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_participante_personagem
        FOREIGN KEY (personagem_id)
        REFERENCES personagens(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_participante_npc
        FOREIGN KEY (npc_id)
        REFERENCES npcs(id)
        ON DELETE CASCADE,

    CONSTRAINT chk_origem_participante
        CHECK (
            personagem_id IS NOT NULL
            OR npc_id IS NOT NULL
        )
);


-- =========================================================
-- RESUMOS DE SESSÃO
-- =========================================================

CREATE TABLE sessoes (
    id SERIAL PRIMARY KEY,

    titulo TEXT,

    numero INTEGER,

    resumo TEXT,

    data_sessao DATE,

    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);