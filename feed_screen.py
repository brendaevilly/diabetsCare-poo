import tkinter as tk
from tkinter import ttk

class FeedScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="white")

        # Frame para os botões de navegação
        nav_frame = tk.Frame(self, bg="white")
        nav_frame.pack(pady=10)

        post_button = tk.Button(nav_frame, text="Criar Post", command=lambda: controller.show_frame("PostScreen"))
        post_button.pack(side="left", padx=5)

        glycemia_button = tk.Button(nav_frame, text="Registrar Glicemia", command=lambda: controller.show_frame("GlycemiaScreen"))
        glycemia_button.pack(side="left", padx=5)

        # Canvas e Scrollbar para a lista de posts
        self.canvas = tk.Canvas(self, bg="white", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="white")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True, padx=(10,0))
        self.scrollbar.pack(side="right", fill="y", padx=(0,10))

    def update_feed(self, posts=None):
        if posts is None:
            posts = self.controller.posts

        # Limpa o feed antigo
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Adiciona os posts ao feed
        for post in posts:
            post_card = tk.Frame(self.scrollable_frame, bg="white", bd=1, relief="solid", highlightbackground="#CCCCCC", highlightthickness=1)
            post_card.pack(fill="x", pady=5, padx=10, ipadx=5, ipady=5)

            user_label = tk.Label(post_card, text=post["user"], font=("Arial", 12, "bold"), bg="white", fg="#1a73e8")
            user_label.pack(anchor="w")

            content_frame = tk.Frame(post_card, bg="white") # Frame para o conteúdo
            content_frame.pack(fill="x", expand=True, pady=(5,0))

            content_label = tk.Label(content_frame, text=post["content"], font=("Arial", 11), bg="white", wraplength=self.winfo_width() - 60, justify="left")
            content_label.pack(anchor="w")