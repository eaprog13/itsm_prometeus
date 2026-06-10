CREATE TABLE departamentos (
    departamento_id  SERIAL        PRIMARY KEY,
    nome             VARCHAR(100)  NOT NULL UNIQUE,
    descricao        TEXT
);

CREATE TABLE categorias (
    categoria_id  SERIAL          PRIMARY KEY,
    nome          VARCHAR(100)    NOT NULL UNIQUE,
    descricao     TEXT            NOT NULL,
    criado_em     TIMESTAMP       DEFAULT NOW()
);

CREATE TABLE users (
    user_id          SERIAL        PRIMARY KEY,
    nome             VARCHAR(100)  NOT NULL,
    email            VARCHAR(150)  NOT NULL UNIQUE,
    contacto         VARCHAR(20)   NOT NULL UNIQUE,
    tipo             VARCHAR(50)   NOT NULL,
    departamento_id  INT           REFERENCES departamentos(departamento_id),
    turno            VARCHAR(50)   NOT NULL,
    password         VARCHAR(255)  NOT NULL,
    criado_em        TIMESTAMP     DEFAULT NOW()
);

CREATE TABLE produtos (
    produto_id    SERIAL          PRIMARY KEY,
    nome          VARCHAR(100)    NOT NULL,
    categoria     VARCHAR(100)    NOT NULL,
    marca         VARCHAR(100)    NOT NULL,
    n_serie       VARCHAR(100)    NOT NULL UNIQUE,
    criado_em     TIMESTAMP       DEFAULT NOW()
);

CREATE TABLE tickets (
    ticket_id     SERIAL          PRIMARY KEY,
    user_id       INT             NOT NULL REFERENCES users(user_id),
    tecnico_id    INT             REFERENCES users(user_id),
    produto_id    INT             REFERENCES produtos(produto_id),
    categoria_id  INT             REFERENCES categorias(categoria_id),
    estado        VARCHAR(20)     NOT NULL DEFAULT 'aberto',
    prioridade    VARCHAR(20)     NOT NULL,
    descricao     TEXT            NOT NULL,
    observacao    TEXT,
    criado_em     TIMESTAMP       DEFAULT NOW()
);