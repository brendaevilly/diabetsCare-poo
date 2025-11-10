# Estrutura do Projeto DiabetsCare

## Organização Modular

O projeto está organizado seguindo uma arquitetura clara que separa completamente o **backend** (lógica de negócio e persistência) do **frontend** (interface gráfica).

## Estrutura de Diretórios

```
diabetsCare-poo/
├── backend/                      # 🎯 BACKEND - Lógica de negócio e dados
│   ├── services/                 # Camada de serviços (regras de negócio)
│   │   ├── __init__.py
│   │   └── DiabetsCareService.py # Serviço principal
│   └── repositories/             # Camada de repositórios (persistência)
│       └── __init__.py
│
├── frontend/                     # 🎨 FRONTEND - Interface gráfica (Tkinter)
│   ├── controllers/              # Controllers da GUI
│   │   ├── __init__.py
│   │   └── app.py                # Controller principal
│   ├── views/                    # Telas (Views)
│   │   └── screens/              # Todas as telas do app
│   │       ├── feed_screen.py
│   │       ├── post_screen.py
│   │       ├── glycemia_screen.py
│   │       ├── user_data_screen.py
│   │       ├── comment_screen.py
│   │       ├── login_screen.py
│   │       ├── dashboard_screen.py
│   │       └── signup_screen/     # Pasta com assets do signup
│   ├── utils/                    # Utilitários do frontend
│   │   ├── __init__.py
│   │   └── threading_helper.py  # Helper para operações assíncronas
│   └── assets/                   # Recursos visuais
│       └── imagem.png
│
├── data/                         # 📁 Dados persistidos (JSON, CSV, INI)
│   └── .gitkeep
│
├── main.py                       # 🚀 Ponto de entrada do aplicativo
├── requirements.txt              # Dependências do projeto
└── README.md                     # Documentação principal
```

## Separação de Responsabilidades

### Backend (`backend/`)
- **Services**: Contém toda a lógica de negócio
  - Validações
  - Regras de aplicação
  - Orquestração de operações
- **Repositories**: Responsável pela persistência de dados
  - Abstração de acesso a dados
  - Preparado para FileRepository (JSON/CSV) ou DatabaseRepository (futuro)

### Frontend (`frontend/`)
- **Controllers**: Controla o fluxo da aplicação GUI
  - Gerencia navegação entre telas
  - Conecta views com services
- **Views**: Interface do usuário (Tkinter)
  - **screens/**: Todas as telas do app (Feed, Post, Glicemia, Login, Dashboard, etc.)
- **Utils**: Utilitários e helpers
  - **threading_helper.py**: Lógica de threading separada das views
- **Assets**: Recursos visuais (imagens, ícones)

### Data (`data/`)
- Armazena arquivos de dados persistidos
- JSON para posts
- CSV para registros de glicemia
- INI para configurações

## Princípios da Arquitetura

### 1. Separação Backend/Frontend
- ✅ Backend não conhece Tkinter
- ✅ Frontend não conhece detalhes de persistência
- ✅ Comunicação via camada de serviços

### 2. Modularidade
- Cada módulo tem responsabilidade única
- Fácil manutenção e testes
- Baixo acoplamento

### 3. Escalabilidade
- Fácil adicionar novas telas em `frontend/views/`
- Fácil adicionar novos serviços em `backend/services/`
- Preparado para migração de repositório (memória → arquivo → banco)

## Como Executar

```bash
python main.py
```

## Imports

### No Backend
```python
# Exemplo: services podem importar repositories
from backend.repositories.file_repository import FileRepository
```

### No Frontend
```python
# Exemplo: controllers importam services e views
from backend.services.DiabetsCareService import Servico_Diabets_Care
from frontend.views.screens.feed_screen import FeedScreen
```

## Benefícios desta Estrutura

1. **Organização Clara**: Fácil encontrar qualquer arquivo
2. **Manutenibilidade**: Mudanças isoladas por camada
3. **Testabilidade**: Backend pode ser testado sem GUI
4. **Escalabilidade**: Fácil adicionar novas funcionalidades
5. **Colaboração**: Múltiplos devs podem trabalhar sem conflitos
6. **Preparação para Futuro**: Estrutura pronta para banco de dados

## Próximos Passos

- [ ] Implementar FileRepository em `backend/repositories/`
- [ ] Adicionar testes unitários
- [ ] Implementar modelos de dados em `backend/models/` (se necessário)
- [ ] Adicionar logging estruturado
- [ ] Configuração centralizada

---

**Última atualização**: Novembro 2025  
**Arquitetura**: MVC com separação Backend/Frontend

