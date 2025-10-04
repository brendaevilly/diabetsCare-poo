# 📋 Documentação Completa do Código - DiabetesCare

## 🏗️ Visão Geral do Sistema

O DiabetesCare é um sistema de monitoramento de glicemia desenvolvido em Python usando a biblioteca Tkinter para interface gráfica. O sistema permite que usuários registrem seus níveis de glicemia em diferentes momentos do dia.

---

## 📁 Estrutura de Arquivos

```
diabetsCare-poo/
├── telas/
│   └── tela_glicemia.py      # Tela principal de registro de glicemia
├── rodar_feed.py             # Script para executar tela de feed
├── requirements.txt          # Dependências do projeto
└── README.md                 # Documentação do projeto
```

---

## 📄 Arquivo: `telas/tela_glicemia.py`

### Importações (Linhas 1-2)
```python
import tkinter as tk
from tkinter import ttk
```
- **Linha 1**: Importa a biblioteca principal Tkinter para criar interfaces gráficas
- **Linha 2**: Importa o módulo ttk (themed widgets) que fornece widgets com visual mais moderno

### Função Principal (Linhas 4-5)
```python
def create_app():
    root = tk.Tk()
```
- **Linha 4**: Define a função principal que criará toda a aplicação
- **Linha 5**: Cria a janela principal (root window) da aplicação Tkinter

### Configuração da Janela (Linhas 6-8)
```python
    root.title("Registro de Glicemia")
    root.geometry("2000x1500") # Abre a janela em tela cheia
    root.configure(bg="#FFFFFF")
```
- **Linha 6**: Define o título da janela como "Registro de Glicemia"
- **Linha 7**: Define o tamanho da janela para 2000x1500 pixels (comentário indica tela cheia)
- **Linha 8**: Configura a cor de fundo da janela principal como branco (#FFFFFF)

### Criação do Cabeçalho (Linhas 10-12)
```python
    # --- Header --- #
    header_frame = tk.Frame(root, bg="#FFFFFF")
    header_frame.pack(pady=(40, 20), padx=50, anchor="w")
```
- **Linha 10**: Comentário indicando a seção do cabeçalho
- **Linha 11**: Cria um frame (container) para o cabeçalho com fundo branco
- **Linha 12**: Posiciona o frame com padding vertical (40 pixels acima, 20 abaixo), 50 pixels nas laterais, alinhado à esquerda

### Título Principal (Linhas 14-15)
```python
    title_label = tk.Label(header_frame, text="Registre sua glicemia", font=("Roboto", 60, "bold"), fg="#1a73e8", bg="#FFFFFF")
    title_label.pack(anchor="w")
```
- **Linha 14**: Cria o título principal com:
  - Texto: "Registre sua glicemia"
  - Fonte: Roboto, tamanho 60, negrito
  - Cor do texto: azul Google (#1a73e8)
  - Fundo: branco
- **Linha 15**: Posiciona o título alinhado à esquerda

### Subtítulo (Linhas 17-18)
```python
    subtitle_label = tk.Label(header_frame, text="Insira seus dados de hoje", font=("Roboto", 20), fg="#1a73e8", bg="#FFFFFF")
    subtitle_label.pack(anchor="w")
```
- **Linha 17**: Cria o subtítulo com fonte Roboto tamanho 20, mesma cor azul
- **Linha 18**: Posiciona o subtítulo alinhado à esquerda

### Container dos Sliders (Linhas 20-22)
```python
    # --- Sliders Frame --- #
    sliders_frame = tk.Frame(root, bg="#FFFFFF")
    sliders_frame.pack(fill="x", padx=50, pady=10)
```
- **Linha 20**: Comentário da seção de sliders
- **Linha 21**: Cria frame para conter todos os sliders
- **Linha 22**: Posiciona o frame preenchendo toda a largura (fill="x"), com padding

### Função para Criar Slider (Linha 24)
```python
    def create_slider_row(parent, label_text, initial_value, min_val, max_val, color_tag_text, color_tag_bg):
```
- **Linha 24**: Define função interna para criar uma linha de slider com parâmetros:
  - `parent`: container pai onde será criado
  - `label_text`: texto do rótulo
  - `initial_value`: valor inicial do slider
  - `min_val`, `max_val`: valores mínimo e máximo
  - `color_tag_text`, `color_tag_bg`: texto e cor da tag de status

### Frame da Linha do Slider (Linhas 25-26)
```python
        row_frame = tk.Frame(parent, bg="#FFFFFF")
        row_frame.pack(fill="x", pady=15)
```
- **Linha 25**: Cria frame para uma linha individual de slider
- **Linha 26**: Posiciona preenchendo a largura com espaçamento vertical de 15 pixels

### Label do Slider (Linhas 28-29)
```python
        label = tk.Label(row_frame, text=label_text, font=("Arial", 14), fg="#1a73e8", bg="#FFFFFF")
        label.pack(side="left", anchor="w")
```
- **Linha 28**: Cria rótulo com o texto descritivo (ex: "Glicemia em jejum")
- **Linha 29**: Posiciona à esquerda da linha

### Container do Slider (Linhas 31-32)
```python
        slider_container_frame = tk.Frame(row_frame, bg="#FFFFFF")
        slider_container_frame.pack(side="left", fill="x", expand=True, padx=20)
```
- **Linha 31**: Cria container específico para o slider e valor
- **Linha 32**: Posiciona expandindo para ocupar espaço disponível

### Label do Valor (Linhas 34-35)
```python
        value_label = tk.Label(slider_container_frame, text=str(initial_value), font=("Arial", 12), fg="#5f6368", bg="#FFFFFF")
        value_label.pack(anchor="center")
```
- **Linha 34**: Cria label para mostrar o valor numérico atual do slider
- **Linha 35**: Centraliza o label no container

### Estilo do Slider (Linhas 37-40)
```python
        # Custom style for the slider
        style = ttk.Style()
        style.configure("TScale", background="#FFFFFF", troughcolor="#d3d3d3", sliderthickness=20)
        style.map("TScale", background=[("active", "#FFFFFF")])
```
- **Linha 37**: Comentário sobre estilo customizado
- **Linha 38**: Cria objeto de estilo para widgets ttk
- **Linha 39**: Configura aparência do slider (fundo branco, trilha cinza, espessura 20)
- **Linha 40**: Define cor de fundo quando ativo

### Criação do Slider (Linhas 42-44)
```python
        slider = ttk.Scale(slider_container_frame, from_=min_val, to=max_val, orient="horizontal", length=400, style="TScale")
        slider.set(initial_value)
        slider.pack(fill="x", expand=True)
```
- **Linha 42**: Cria o slider horizontal com valores mínimo/máximo, comprimento 400px
- **Linha 43**: Define o valor inicial
- **Linha 44**: Posiciona preenchendo a largura disponível

### Função de Atualização (Linhas 46-49)
```python
        def update_value(event):
            value_label.config(text=str(int(slider.get())))
        slider.bind("<B1-Motion>", update_value)
        slider.bind("<ButtonRelease-1>", update_value)
```
- **Linha 46**: Define função para atualizar o valor mostrado
- **Linha 47**: Atualiza o texto do label com o valor atual do slider
- **Linha 48**: Liga a função ao evento de arrastar o slider
- **Linha 49**: Liga a função ao evento de soltar o botão do mouse

### Tag de Status (Linhas 51-52)
```python
        color_tag = tk.Label(row_frame, text=color_tag_text, bg=color_tag_bg, fg="white", font=("Arial", 10, "bold"), padx=20, pady=5, relief="flat", borderwidth=0)
        color_tag.pack(side="right", padx=20)
```
- **Linha 51**: Cria tag colorida com status (Baixa/Normal/Alta) com:
  - Texto em branco, fonte Arial 10 negrito
  - Padding interno, borda plana
- **Linha 52**: Posiciona à direita da linha

### Retorno da Função (Linha 54)
```python
        return slider, value_label
```
- **Linha 54**: Retorna referências ao slider e label para uso posterior

### Criação dos Sliders (Linhas 56-59)
```python
    # --- Sliders --- #
    create_slider_row(sliders_frame, "Glicemia em jejum (mg/dL)", 65, 40, 200, "Baixa", "#fbbc04")
    create_slider_row(sliders_frame, "Glicemia pós-prandial (após refeição)", 90, 40, 200, "Normal", "#34a853")
    create_slider_row(sliders_frame, "Glicemia antes de dormir", 145, 40, 200, "Alta", "#ea4335")
```
- **Linha 56**: Comentário da seção
- **Linha 57**: Cria slider para glicemia em jejum (valor inicial 65, tag "Baixa" amarela)
- **Linha 58**: Cria slider pós-prandial (valor inicial 90, tag "Normal" verde)
- **Linha 59**: Cria slider antes de dormir (valor inicial 145, tag "Alta" vermelha)

### Área de Texto (Linhas 61-63)
```python
    # --- Text Area --- #
    text_frame = tk.Frame(root, bg="#FFFFFF")
    text_frame.pack(fill="x", padx=50, pady=20, anchor="w")
```
- **Linha 61**: Comentário da seção de texto
- **Linha 62**: Cria frame para a área de texto
- **Linha 63**: Posiciona com padding e alinhamento à esquerda

### Label da Pergunta (Linhas 65-66)
```python
    how_are_you_label = tk.Label(text_frame, text="Como você está?", font=("Arial", 14), fg="#1a73e8", bg="#FFFFFF")
    how_are_you_label.pack(anchor="w", pady=(0, 10))
```
- **Linha 65**: Cria label com a pergunta "Como você está?"
- **Linha 66**: Posiciona à esquerda com espaço abaixo

### Campo de Texto (Linhas 68-70)
```python
    text_area = tk.Text(text_frame, height=5, font=("Arial", 12), bg="#f0f0f0", relief="solid", bd=0, highlightthickness=1, highlightbackground="#e0e0e0", wrap="word", padx=10, pady=10)
    text_area.insert(tk.END, "Escreva aqui...")
    text_area.pack(fill="x", expand=True)
```
- **Linha 68**: Cria área de texto multi-linha com:
  - 5 linhas de altura, fonte Arial 12
  - Fundo cinza claro, borda sólida
  - Quebra de linha por palavra, padding interno
- **Linha 69**: Insere texto placeholder
- **Linha 70**: Posiciona preenchendo a largura

### Botão Salvar (Linhas 72-74)
```python
    # --- Save Button --- #
    save_button = tk.Button(root, text="Salvar", font=("Arial", 14, "bold"), bg="#1a73e8", fg="white", padx=40, pady=15, relief="flat", bd=0, highlightthickness=0)
    save_button.pack(pady=30)
```
- **Linha 72**: Comentário da seção do botão
- **Linha 73**: Cria botão azul com:
  - Texto "Salvar" em branco, fonte Arial 14 negrito
  - Fundo azul Google, borda plana
  - Padding interno para tamanho adequado
- **Linha 74**: Posiciona com espaço vertical

### Formas Abstratas (Linhas 76-80)
```python
    # --- Abstract Shapes --- #
    canvas = tk.Canvas(root, width=300, height=200, bg="#FFFFFF", highlightthickness=0)
    canvas.place(relx=1.0, rely=0, anchor="ne")
    canvas.create_oval(100, -100, 400, 200, fill="#1a73e8", outline="")
    canvas.create_oval(180, -50, 450, 150, fill="#1967d2", outline="")
```
- **Linha 76**: Comentário das formas decorativas
- **Linha 77**: Cria canvas (área de desenho) 300x200 pixels
- **Linha 78**: Posiciona no canto superior direito da janela
- **Linha 79**: Desenha círculo azul decorativo (parcialmente fora da tela)
- **Linha 80**: Desenha segundo círculo azul mais escuro sobreposto

### Execução do Loop Principal (Linha 82)
```python
    root.mainloop()
```
- **Linha 82**: Inicia o loop principal do Tkinter (mantém a janela aberta e responsiva)

### Execução Condicional (Linhas 84-85)
```python
if __name__ == "__main__":
    create_app()
```
- **Linha 84**: Verifica se o arquivo está sendo executado diretamente (não importado)
- **Linha 85**: Chama a função para criar e executar a aplicação

---

## 📄 Arquivo: `rodar_feed.py`

Este arquivo contém um script simplificado para executar apenas a tela de feed:

### Estrutura Básica
```python
#!/usr/bin/env python3
"""
Script para rodar apenas a tela de feed
"""

import tkinter as tk
from telas.tela_feed import TelaFeed

class SistemaFeed:
    # ... código da classe
```

- Define uma classe `SistemaFeed` que cria uma janela para mostrar apenas o feed
- Inclui métodos necessários para compatibilidade com a classe base
- Permite executar a tela de feed independentemente

---

## 📄 Arquivo: `requirements.txt`

```
numpy>=1.26
matplotlib>=3.8
```

- **Linha 1**: Especifica versão mínima do NumPy para operações numéricas
- **Linha 2**: Especifica versão mínima do Matplotlib para gráficos (uso futuro)

---

## 🎯 Conceitos Técnicos Utilizados

### 1. **Tkinter Widgets**
- `tk.Tk()`: Janela principal
- `tk.Frame()`: Container para organizar widgets
- `tk.Label()`: Texto estático
- `tk.Button()`: Botão clicável
- `tk.Text()`: Área de texto multi-linha
- `ttk.Scale()`: Slider com visual moderno
- `tk.Canvas()`: Área para desenhos

### 2. **Layout Management**
- `pack()`: Empacotamento sequencial
- `place()`: Posicionamento absoluto
- Parâmetros: `fill`, `expand`, `anchor`, `pady`, `padx`

### 3. **Eventos**
- `bind()`: Liga eventos a funções
- `<B1-Motion>`: Arrastar com botão esquerdo
- `<ButtonRelease-1>`: Soltar botão esquerdo

### 4. **Estilização**
- Cores hexadecimais (#FFFFFF, #1a73e8)
- Fontes personalizadas (Arial, Roboto)
- Padding e margens para espaçamento

### 5. **Estrutura de Dados**
- Funções aninhadas para organização
- Parâmetros para configuração flexível
- Retorno de múltiplos valores (tuple)

---

## 🔧 Fluxo de Execução

1. **Inicialização**: Criação da janela principal
2. **Layout**: Construção dos elementos visuais
3. **Configuração**: Definição de estilos e valores iniciais
4. **Eventos**: Ligação de interações do usuário
5. **Loop Principal**: Manutenção da interface responsiva

---

## 📚 Possíveis Melhorias

1. **Validação de Dados**: Verificar valores inseridos
2. **Persistência**: Salvar dados em arquivos
3. **Responsividade**: Adaptar a diferentes tamanhos de tela
4. **Acessibilidade**: Adicionar suporte a teclado
5. **Internacionalização**: Suporte a múltiplos idiomas

---

*Este documento serve como guia completo para compreensão e manutenção do código do sistema DiabetesCare.*
