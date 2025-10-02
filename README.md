# DiabetesCare - Sistema de Cuidados com Diabetes

Sistema desenvolvido em Python com Tkinter para gerenciamento de dados de glicemia e posts educativos sobre diabetes.

## 🏗️ Estrutura do Projeto

```
diabetsCare-poo/
├── sistema_diabetes.py       # Sistema principal
├── requirements.txt          # Dependências
├── telas/                    # Telas modulares em português
│   ├── __init__.py
│   ├── tela_base.py          # Classe base para todas as telas
│   ├── tela_glicemia.py      # Tela de registro de glicemia
│   ├── tela_posts.py         # Tela de criação de posts
│   └── tela_feed.py          # Tela de feed de posts
└── README.md
```

## 🚀 Como Executar

1. **Instalar dependências:**
```bash
pip install -r requirements.txt
```

2. **Executar o sistema:**
```bash
python3 sistema_diabetes.py
```

## 📱 Funcionalidades Implementadas

### **Tela de Glicemia:**
- ✅ Sliders interativos para 3 tipos de glicemia:
  - Em jejum (50-200 mg/dL)
  - Pós-prandial (50-300 mg/dL) 
  - Antes de dormir (50-250 mg/dL)
- ✅ Indicadores de status (Baixa/Normal/Alta) com cores
- ✅ Campo de bem-estar
- ✅ **Botão salvar funcional**
- ✅ Limpeza automática dos campos após salvar

### **Tela de Posts:**
- ✅ Campo de texto para criação de posts
- ✅ Botão postar funcional
- ✅ Navegação automática para o feed após postar
- ✅ Validação de conteúdo

### **Tela de Feed:**
- ✅ Lista scrollável de posts
- ✅ Posts de exemplo com profissionais da saúde
- ✅ Informações do autor e data
- ✅ Interface responsiva

## 🎨 Design

- **Interface em português** com comentários detalhados
- **Cores consistentes**: Azul principal, verde para normal, amarelo para baixa, vermelho para alta
- **Navegação intuitiva** entre telas
- **Sliders interativos** para entrada de dados
- **Menu principal** com opções claras

## 🔧 Arquitetura

### **Sistema Modular em Português:**
- Cada tela em arquivo separado
- Classe base `TelaBase` com funcionalidades comuns
- Sistema principal `SistemaDiabetes` gerencia navegação
- Código completamente comentado em português

### **Classes Principais:**
- `SistemaDiabetes`: Sistema principal
- `TelaBase`: Classe base para telas
- `TelaGlicemia`: Registro de glicemia
- `TelaPosts`: Criação de posts
- `TelaFeed`: Feed de posts

## 📊 Tecnologias

- **Python 3.x**
- **Tkinter** - Interface gráfica
- **NumPy** - Dados numéricos (para futuras implementações)
- **Matplotlib** - Gráficos (para futuras implementações)

## 🔮 Próximos Passos

- Implementar persistência de dados (JSON/CSV)
- Adicionar threads para operações assíncronas
- Implementar validações de dados
- Adicionar gráficos no dashboard
- Implementar sistema de login/cadastro