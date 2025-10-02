import tkinter as tk
from tkinter import ttk

class FeedScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#F0F2F5") # Cor de fundo para o feed

        # Frame para os botões de navegação no topo
        nav_frame = tk.Frame(self, bg="#F0F2F5")
        nav_frame.pack(pady=10, fill="x")

        post_button = tk.Button(nav_frame, text="Criar Post", command=lambda: controller.show_frame("PostScreen"),
                                bg="#4285F4", fg="white", font=("Arial", 10, "bold"), relief="flat", padx=10, pady=5)
        post_button.pack(side="left", padx=10)

        glycemia_button = tk.Button(nav_frame, text="Registrar Glicemia", command=lambda: controller.show_frame("GlycemiaScreen"),
                                    bg="#34A853", fg="white", font=("Arial", 10, "bold"), relief="flat", padx=10, pady=5)
        glycemia_button.pack(side="left", padx=10)

        # Canvas e Scrollbar para a lista de posts
        self.canvas = tk.Canvas(self, bg="#F0F2F5", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#F0F2F5")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw", width=self.winfo_width())
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True, padx=(20,0))
        self.scrollbar.pack(side="right", fill="y", padx=(0,20))

        # Bind para ajustar a largura do canvas quando a janela for redimensionada
        self.bind("<Configure>", self._on_frame_configure)

    def _on_frame_configure(self, event):
        # Ajusta a largura da janela interna do canvas para preencher o espaço disponível
        self.canvas.itemconfig(self.canvas.winfo_children()[0], width=event.width - self.scrollbar.winfo_width() - 40)

    def update_feed(self, posts=None):
        if posts is None:
            posts = self.controller.posts

        # Limpa o feed antigo
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Adiciona os posts ao feed
        for post in posts:
            # Simula um card com bordas arredondadas e sombra
            post_card = tk.Frame(self.scrollable_frame, bg="white", bd=0, relief="flat", 
                                 highlightbackground="#CCCCCC", highlightthickness=1)
            post_card.pack(fill="x", pady=10, padx=20, ipadx=10, ipady=10)

            user_label = tk.Label(post_card, text=post["user"], font=("Arial", 14, "bold"), bg="white", fg="#1a73e8")
            user_label.pack(anchor="w", pady=(0, 5))

            content_label = tk.Label(post_card, text=post["content"], font=("Arial", 12), bg="white", 
                                    wraplength=self.winfo_width() - 100, justify="left", anchor="w")
            content_label.pack(fill="x", expand=True)

