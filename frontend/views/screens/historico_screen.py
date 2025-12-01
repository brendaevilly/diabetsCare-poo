import tkinter as tk
from tkinter import ttk, messagebox

class HistoricoScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#E0F2F7")

        tk.Label(self, text=" Histórico Completo", bg="#E0F2F7",
                 font=("Arial", 20, "bold")).pack(pady=20)

        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill="both", padx=40, pady=10)

        self.posts_tab = tk.Frame(notebook, bg="white")
        notebook.add(self.posts_tab, text="Posts")

        self.glicemias_tab = tk.Frame(notebook, bg="white")
        notebook.add(self.glicemias_tab, text="Glicemias")

        tk.Button(self, text="Voltar", bg="#EA4335", fg="white",
                  font=("Arial", 12, "bold"), relief="flat", padx=20, pady=10,
                  command=lambda: controller.show_frame("UserDataScreen")).pack(pady=20)

    def atualizar_dados(self):
        # Limpa conteúdo anterior
        for w in self.posts_tab.winfo_children():
            w.destroy()
        for w in self.glicemias_tab.winfo_children():
            w.destroy()

        try:
            # get current user details (requires that user is logged in and token set)
            user = None
            try:
                user = self.controller.service.get_current_user()
            except Exception:
                user = None

            user_id = None
            username = None
            if isinstance(user, dict):
                user_id = user.get('id')
                username = user.get('username')

            # Prefer server endpoint to list posts by user if available, else get all and filter
            posts = []
            try:
                if user_id is not None and hasattr(self.controller.service, 'listarPostsPorUsuario'):
                    posts = self.controller.service.listarPostsPorUsuario(user_id)
                else:
                    all_posts = self.controller.service.get_all_posts()
                    # filter by username if available
                    if username:
                        posts = [p for p in all_posts if p.get('user') == username]
                    else:
                        posts = all_posts
            except Exception:
                posts = []

            # glicemia: try to fetch history for current user
            try:
                glicemias = self.controller.service.get_glycemia_history()
            except Exception:
                glicemias = []
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar histórico: {e}")
            return

            # --- Exibir Posts ---
        if posts:
            for post in reversed(posts):
                # posts returned from API use 'timestamp' and 'content'
                data = post.get("timestamp") or post.get("date") or "Data não registrada"
                texto = f"• [{data}] {post.get('content') or post.get('conteudo', 'Sem conteúdo')}"
                tk.Label(
                        self.posts_tab,
                        text=texto,
                        bg="white",
                        fg="#202124",
                        font=("Arial", 12),
                        anchor="w",
                        justify="left",
                        wraplength=700
                ).pack(anchor="w", pady=5)
        else:
            tk.Label(
                self.posts_tab,
                text="Nenhum post encontrado.",
                bg="white",
                fg="gray"
            ).pack(pady=10)

        # --- Glicemias ---
        if glicemias:
            for g in reversed(glicemias):
                data = g.get('data') or g.get('timestamp') or '—'
                jejum = g.get('jejum')
                pos = g.get('pos_prandial')
                dormir = g.get('dormir')
                observacoes = g.get('observacoes', '—')

                parts = []
                if jejum is not None:
                    parts.append(f"Jejum: {jejum}")
                if pos is not None:
                    parts.append(f"Pós-prandial: {pos}")
                if dormir is not None:
                    parts.append(f"Antes de dormir: {dormir}")

                texto = f"{data} | " + ", ".join(parts) + f"\nObservações: {observacoes}"

                tk.Label(
                    self.glicemias_tab,
                    text=texto, bg="white", fg="#202124",
                    font=("Arial", 12),
                    anchor="w", justify="left",
                    wraplength=700
                ).pack(anchor="w", pady=10)
        else:
            tk.Label(
                self.glicemias_tab,
                text="Nenhum registro de glicemia encontrado.",
                bg="white", fg="gray"
            ).pack(pady=10)

