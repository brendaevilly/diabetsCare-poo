import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk  # pip install pillow

root = tk.Tk()
root.title("DiabetesCare")
root.state("zoomed")
root.configure(bg="white")

# =============== FRAME ESQUERDA (FORMULÁRIO) ==================
frame_left = tk.Frame(root, bg="white", width=500, height=600)
frame_left.pack(side="left", fill="both", padx = 320, pady= 150)

# Título
titulo = tk.Label(frame_left, text="Cadastre-se", font=("Arial", 28, "bold"), fg="#1E90FF", bg="white")
titulo.pack(pady=(60, 5))

subtitulo = tk.Label(frame_left, text="Adicione os detalhes da sua conta", font=("Arial", 10), bg="white", fg="gray")
subtitulo.pack(pady=(0, 20))

# Campos
usuario = tk.Entry(frame_left, font=("Arial", 12), width=30, bd=0, bg="#E6F0FF", relief="flat")
usuario.insert(0, "Nome Usuário")
usuario.pack(pady=10, ipady=8)

senha = tk.Entry(frame_left, font=("Arial", 12), width=30, bd=0, bg="#E6F0FF", relief="flat", show="*")
senha.insert(0, "Senha")
senha.pack(pady=10, ipady=8)

# Opções
tipo_var = tk.StringVar(value="Comum")

frame_tipo = tk.Frame(frame_left, bg="white")
frame_tipo.pack(pady=10)

tk.Radiobutton(frame_tipo, text="Comum", variable=tipo_var, value="Comum", bg="white", font=("Arial", 10)).grid(row=0, column=0, padx=30)
tk.Radiobutton(frame_tipo, text="Profissional", variable=tipo_var, value="Profissional", bg="white", font=("Arial", 10)).grid(row=0, column=1, padx=30)

# Botão cadastro
btn_cadastrar = tk.Button(frame_left, text="Cadastre-se", bg="#1E90FF", fg="white", font=("Arial", 12, "bold"),
                          relief="flat", width=20, height=2, cursor="hand2")
btn_cadastrar.pack(pady=20)

# Login
frame_login = tk.Frame(frame_left, bg="white")
frame_login.pack(pady=20)

tk.Label(frame_login, text="Já possui uma conta?", font=("Arial", 10), bg="white", fg="gray").grid(row=0, column=0)
tk.Button(frame_login, text="Login", bg="#1E90FF", fg="white", font=("Arial", 10, "bold"),
          relief="flat", cursor="hand2").grid(row=0, column=1, padx=5)


# =============== FRAME DIREITA (TELA AZUL) ==================
frame_right = tk.Frame(root, bg="#4A90E2", width=500, height=600)
frame_right.pack(side="right", fill="both")

# Carregar imagens decorativas
bg1 = ImageTk.PhotoImage(Image.open("Vector1.png").resize((250,250)))
bg2 = ImageTk.PhotoImage(Image.open("Vector2.png").resize((200,200)))
bg3 = ImageTk.PhotoImage(Image.open("Vector3.png").resize((180,180)))
icon = ImageTk.PhotoImage(Image.open("report (1) 2.png").resize((220,220)))

# Colocar vetores no fundo
lbl_bg1 = tk.Label(frame_right, image=bg1, bg="#4A90E2", border=0)
lbl_bg1.place(x=300, y=10)

lbl_bg2 = tk.Label(frame_right, image=bg2, bg="#4A90E2", border=0)
lbl_bg2.place(x=-50, y=90)

lbl_bg3 = tk.Label(frame_right, image=bg3, bg="#4A90E2", border=0)
lbl_bg3.place(x=150, y=350)


# Texto de boas-vindas
title_font = font.Font(family="Arial", size=22, weight="bold")
subtitle_font = font.Font(family="Arial", size=18, weight="bold")

tk.Label(frame_right, text="Bem-Vindo ao", bg="#4A90E2",  fg="white", font=title_font).place(x=50, y=180)
tk.Label(frame_right, text="DiabetesCare", bg="#4A90E2", fg="white", font=subtitle_font).place(x=50, y=220)
tk.Label(frame_right, text="Faça o login para acessar sua conta ou cadastre-se",
         bg="#4A90E2", fg="white", font=("Arial", 10)).place(x=50, y=260)

# Ícone central
lbl_icon = tk.Label(frame_right, image=icon, bg="#4A90E2", border=0)
lbl_icon.place(x=140, y=320)


root.mainloop()
