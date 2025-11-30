-- Script de inicialização do banco de dados PostgreSQL para DiabetsCare
-- Este script é executado automaticamente quando o contêiner PostgreSQL é criado pela primeira vez

-- Criação da tabela de usuários
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    tipo VARCHAR(50) NOT NULL DEFAULT 'Comum',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criação da tabela de glicemia
CREATE TABLE IF NOT EXISTS glicemia (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER REFERENCES usuarios(id) ON DELETE CASCADE,
    data DATE NOT NULL,
    jejum INTEGER,
    pos_prandial INTEGER,
    dormir INTEGER,
    observacoes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criação da tabela de posts
CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER REFERENCES usuarios(id) ON DELETE CASCADE,
    conteudo TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices para melhorar performance de consultas
CREATE INDEX IF NOT EXISTS idx_glicemia_usuario_data ON glicemia(usuario_id, data);
CREATE INDEX IF NOT EXISTS idx_posts_usuario_timestamp ON posts(usuario_id, timestamp);

-- Comentários nas tabelas
COMMENT ON TABLE usuarios IS 'Armazena informações dos usuários do sistema';
COMMENT ON TABLE glicemia IS 'Registros de medições de glicemia dos usuários';
COMMENT ON TABLE posts IS 'Posts compartilhados pelos usuários na plataforma';

