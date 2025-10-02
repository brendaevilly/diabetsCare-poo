import tkinter as tk
from tkinter import ttk

class PostScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        # Simula um gradiente com uma cor de fundo clara
        self.configure(bg="#E0F2F7") 

        # Frame principal para centralizar o conteúdo e aplicar o fundo azul claro
        main_frame = tk.Frame(self, bg="#E0F2F7")
        main_frame.pack(expand=True, fill="both")

        # Card de postagem com fundo branco e bordas arredondadas (simuladas com highlight)
        # Tkinter não suporta bordas arredondadas nativamente, então usaremos um truque visual
        post_card = tk.Frame(main_frame, bg="white", bd=0, relief="flat", 
                             highlightbackground="#CCCCCC", highlightthickness=1)
        post_card.pack(padx=50, pady=50, ipadx=20, ipady=20)

        # Campo de texto para a postagem
        self.post_text = tk.Text(post_card, height=10, width=60, font=("Arial", 14), 
                                 relief="flat", bd=0, wrap="word", padx=10, pady=10)
        self.post_text.insert("1.0", "No que está pensando?")
        self.post_text.config(fg="grey")
        self.post_text.bind("<FocusIn>", self._clear_placeholder)
        self.post_text.bind("<FocusOut>", self._add_placeholder)
        self.post_text.pack(padx=10, pady=10)

        # Linha divisória
        separator = ttk.Separator(post_card, orient="horizontal")
        separator.pack(fill="x", padx=10, pady=10)

        # Frame para os botões
        button_frame = tk.Frame(post_card, bg="white")
        button_frame.pack(pady=10)

        # Botão Cancelar
        cancel_button = tk.Button(button_frame, text="Cancelar", command=self._cancel_post, 
                                 bg="#EA4335", fg="white", font=("Arial", 12, "bold"), 
                                 relief="flat", padx=25, pady=12, bd=0)
        cancel_button.pack(side="left", padx=10)

        # Botão Postar
        post_button = tk.Button(button_frame, text="Postar", command=self._submit_post, 
                               bg="#34A853", fg="white", font=("Arial", 12, "bold"), 
                               relief="flat", padx=25, pady=12, bd=0)
        post_button.pack(side="left", padx=10)

    def _clear_placeholder(self, event):
        if self.post_text.get("1.0", "end-1c").strip() == "No que está pensando?".strip():
            self.post_text.delete("1.0", "end")
            self.post_text.config(fg="black")

    def _add_placeholder(self, event):
        if not self.post_text.get("1.0", "end-1c").strip():
            self.post_text.insert("1.0", "No que está pensando?")
            self.post_text.config(fg="grey")

    def _submit_post(self):
        content = self.post_text.get("1.0", "end-1c").strip()
        if content and content != "No que está pensando?".strip():
            self.controller.add_post(content)
            self.post_text.delete("1.0", "end")
            self.post_text.insert("1.0", "No que está pensando?")
            self.post_text.config(fg="grey")
            self.controller.show_frame("FeedScreen")
        else:
            print("Post vazio!") # Pode ser substituído por um messagebox

    def _cancel_post(self):
        self.post_text.delete("1.0", "end")
        self.post_text.insert("1.0", "No que está pensando?")
        self.post_text.config(fg="grey")
        self.controller.show_frame("FeedScreen")

