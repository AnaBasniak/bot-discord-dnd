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