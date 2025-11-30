# Backend DiabetsCare

Servidor Flask que fornece a API REST para o aplicativo DiabetsCare.

## Estrutura

```
backend/
├── app.py              # Aplicação Flask principal (a ser expandida pelo Dev 2)
├── controllers/        # Controladores da API REST
├── models/             # Modelos SQLAlchemy (a ser implementado pelo Dev 2 e Dev 3)
├── repositories/       # Camada de acesso a dados (DAL)
├── services/           # Lógica de negócio
├── Dockerfile          # Configuração do contêiner Docker
├── init.sql            # Script de inicialização do banco de dados
└── requirements.txt    # Dependências Python
```

## Configuração

### Variáveis de Ambiente

O backend utiliza as seguintes variáveis de ambiente (configuradas no `docker-compose.yml`):

- `DATABASE_URL`: URL de conexão com o PostgreSQL
- `FLASK_ENV`: Ambiente de execução (development/production)
- `FLASK_DEBUG`: Modo debug (1 para ativado)
- `FLASK_APP`: Nome do arquivo principal da aplicação (app.py)

## Execução Local (sem Docker)

Para executar localmente sem Docker:

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Configure as variáveis de ambiente:
```bash
export DATABASE_URL=postgresql://diabetscare_user:diabetscare_pass@localhost:5432/diabetscare_db
export FLASK_APP=app.py
export FLASK_ENV=development
```

3. Execute o servidor:
```bash
flask run
```

## Execução com Docker

O backend é executado automaticamente através do `docker-compose.yml` na raiz do projeto.

Para reconstruir o contêiner após alterações:
```bash
docker-compose build backend
docker-compose up -d backend
```

## Próximos Passos (Dev 2 e Dev 3)

### Tarefas do Dev 2:
- Implementar modelos SQLAlchemy para Usuário e Glicemia
- Implementar DAL para Usuário e Glicemia
- Criar endpoints de API para autenticação e registro
- Criar endpoints de API para CRUD de glicemia

### Tarefas do Dev 3:
- Implementar DAL para Relatórios
- Criar endpoints de API para relatórios e consultas complexas

## Estrutura do Banco de Dados

Consulte o arquivo `init.sql` para ver a estrutura completa das tabelas:
- `usuarios`: Informações dos usuários
- `glicemia`: Registros de medições de glicemia
- `posts`: Posts compartilhados pelos usuários

## Endpoints Atuais

### GET /
Retorna status da API.

**Resposta:**
```json
{
  "status": "ok",
  "mensagem": "API DiabetsCare está rodando",
  "versao": "1.0.0"
}
```

### GET /api/health
Verificação de saúde da API.

**Resposta:**
```json
{
  "status": "healthy",
  "servico": "DiabetsCare Backend"
}
```

## Notas

- O arquivo `app.py` atual contém apenas endpoints básicos de saúde. A implementação completa da API será feita pelos desenvolvedores Dev 2 e Dev 3.
- A conexão com o banco de dados PostgreSQL será implementada usando SQLAlchemy.
- Todos os endpoints devem seguir o padrão REST e retornar JSON.

