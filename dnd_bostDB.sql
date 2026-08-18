CREATE TABLE jogadores (
    discord_id BIGINT PRIMARY KEY,
    nome_discord TEXT NOT NULL,
    eh_mestre BOOLEAN NOT NULL DEFAULT FALSE,
    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE personagens (
    id SERIAL PRIMARY KEY,

    jogador_id BIGINT NOT NULL,

    nome TEXT NOT NULL,

    nivel INTEGER NOT NULL DEFAULT 1,

    raca TEXT,
    subraca TEXT,
    classe TEXT,
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
    lidar_animais BOOLEAN NOT NULL DEFAULT FALSE,
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

CREATE TABLE proficiencias (
    id SERIAL PRIMARY KEY,

    personagem_id INTEGER NOT NULL,

    tipo TEXT NOT NULL,
    nome TEXT NOT NULL,

    CONSTRAINT fk_proficiencia_personagem
        FOREIGN KEY (personagem_id)
        REFERENCES personagens(id)
        ON DELETE CASCADE
);
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

CREATE TABLE racas (
    id SERIAL PRIMARY KEY,

    nome TEXT NOT NULL UNIQUE,

    descricao TEXT,

    deslocamento INTEGER NOT NULL DEFAULT 30
);

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
CREATE TABLE classes (
    id SERIAL PRIMARY KEY,

    nome TEXT NOT NULL UNIQUE,

    descricao TEXT,

    dado_vida INTEGER NOT NULL,

    nivel_maximo INTEGER NOT NULL DEFAULT 20
);
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