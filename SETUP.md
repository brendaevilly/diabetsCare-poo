# Guia de Setup e Execução - DiabetsCare-POO

Este documento descreve o processo de configuração e execução do projeto DiabetsCare usando Docker e PostgreSQL.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- [Docker](https://www.docker.com/get-started) (versão 20.10 ou superior)
- [Docker Compose](https://docs.docker.com/compose/install/) (versão 2.0 ou superior)

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
diabetsCare-poo/
├── backend/              # Servidor Flask e lógica de negócio
│   ├── controllers/      # Controladores da API
│   ├── models/           # Modelos de dados (SQLAlchemy)
│   ├── repositories/     # Camada de acesso a dados
│   ├── services/         # Lógica de negócio
│   ├── Dockerfile        # Configuração do contêiner do backend
│   ├── init.sql          # Script de inicialização do banco
│   └── requirements.txt  # Dependências Python do backend
├── frontend/             # Aplicação desktop Tkinter
├── data/                 # Dados locais (será migrado para PostgreSQL)
└── docker-compose.yml    # Orquestração dos serviços
```

## Serviços Docker

O `docker-compose.yml` configura três serviços principais:

1. **PostgreSQL**: Banco de dados relacional
   - Porta: `5432`
   - Usuário: `diabetscare_user`
   - Senha: `diabetscare_pass`
   - Banco: `diabetscare_db`

2. **Backend (Flask)**: API REST para comunicação com o frontend
   - Porta: `5000`
   - URL base: `http://localhost:5000`

## Como Executar

### 1. Iniciar os Serviços

No diretório raiz do projeto, execute:

```bash
docker-compose up -d
```

Este comando irá:
- Baixar as imagens necessárias (PostgreSQL, Python)
- Criar e iniciar os contêineres
- Executar o script `init.sql` para criar as tabelas no banco de dados
- Iniciar o servidor Flask

### 2. Verificar o Status dos Serviços

Para verificar se os serviços estão rodando:

```bash
docker-compose ps
```

### 3. Visualizar os Logs

Para acompanhar os logs do backend:

```bash
docker-compose logs -f backend
```

Para acompanhar os logs do PostgreSQL:

```bash
docker-compose logs -f postgres
```

### 4. Parar os Serviços

Para parar os serviços:

```bash
docker-compose down
```

Para parar e remover os volumes (apaga os dados do banco):

```bash
docker-compose down -v
```

## Estrutura do Banco de Dados

O banco de dados PostgreSQL contém as seguintes tabelas:

### `usuarios`
- `id`: Identificador único (SERIAL)
- `username`: Nome de usuário (único)
- `password`: Senha (hash)
- `tipo`: Tipo de usuário ('Comum' ou 'Profissional')
- `created_at`: Data de criação

### `glicemia`
- `id`: Identificador único (SERIAL)
- `usuario_id`: Referência ao usuário (FOREIGN KEY)
- `data`: Data do registro
- `jejum`: Valor de glicemia em jejum (mg/dL)
- `pos_prandial`: Valor pós-prandial (mg/dL)
- `dormir`: Valor antes de dormir (mg/dL)
- `observacoes`: Observações do usuário
- `created_at`: Data de criação

### `posts`
- `id`: Identificador único (SERIAL)
- `usuario_id`: Referência ao usuário (FOREIGN KEY)
- `conteudo`: Conteúdo do post
- `timestamp`: Data e hora de criação

## Conectando ao Banco de Dados

Para conectar ao banco de dados usando um cliente PostgreSQL:

```bash
docker-compose exec postgres psql -U diabetscare_user -d diabetscare_db
```

Ou usando uma ferramenta externa como pgAdmin ou DBeaver:
- Host: `localhost`
- Porta: `5432`
- Usuário: `diabetscare_user`
- Senha: `diabetscare_pass`
- Banco: `diabetscare_db`

## Desenvolvimento

### Modo de Desenvolvimento

O backend está configurado para modo de desenvolvimento com hot-reload. Alterações no código serão refletidas automaticamente.

### Adicionar Novas Dependências

1. Adicione a dependência em `backend/requirements.txt`
2. Reconstrua o contêiner:

```bash
docker-compose build backend
docker-compose up -d backend
```

### Executar Migrações ou Scripts SQL

Para executar scripts SQL adicionais, você pode:

1. Adicionar ao diretório `backend/` e montar como volume
2. Ou executar diretamente:

```bash
docker-compose exec postgres psql -U diabetscare_user -d diabetscare_db -f /caminho/para/script.sql
```

## Troubleshooting

### Porta já em uso

Se a porta 5000 ou 5432 já estiver em uso, você pode alterar no `docker-compose.yml`:

```yaml
ports:
  - "5001:5000"  # Mude a porta externa
```

### Erro de conexão com o banco

Certifique-se de que o serviço PostgreSQL está saudável antes do backend iniciar. O `docker-compose.yml` já configura essa dependência.

### Limpar e recriar tudo

Se precisar começar do zero:

```bash
docker-compose down -v
docker-compose build --no-cache
docker-compose up -d
```

## Status da Implementação

### Concluído (Dev 1)
- Estrutura de diretórios configurada
- Docker Compose configurado
- PostgreSQL configurado com script de inicialização
- Dockerfile do backend criado
- Arquivo `app.py` básico criado (endpoints de saúde)

### Em Andamento
- **Estágio 2**: Implementação da DAL e API REST (Dev 2 e Dev 3)
  - Dev 2: Modelos e API para Usuário e Glicemia
  - Dev 3: Modelos e API para Alimentação e Relatórios

### Próximos Passos
- **Estágio 3**: Adaptação do frontend para usar a API (Dev 4)
- **Estágio 4**: Testes de integração e revisão final

## Suporte

Para problemas ou dúvidas, consulte a documentação do projeto ou entre em contato com a equipe de desenvolvimento.

