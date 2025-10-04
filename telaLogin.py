import tkinter as tk
from PIL import Image, ImageTk
import os

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DiabetesCare Login")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")
        self.root.resizable(False, False)

        # Configurar grid principal
        self.root.grid_columnconfigure(0, weight=1, uniform="col")
        self.root.grid_columnconfigure(1, weight=1, uniform="col")
        self.root.grid_rowconfigure(0, weight=1)

        # Frames principais
        self.left_frame = tk.Frame(self.root, bg="white")
        self.left_frame.grid(row=0, column=0, sticky="nsew")

        self.right_frame = tk.Frame(self.root, bg="#1E90FF")
        self.right_frame.grid(row=0, column=1, sticky="nsew")

        self._criar_painel_esquerdo()
        self._criar_painel_direito()

    def _criar_painel_esquerdo(self):
        # Container centralizado
        container_left = tk.Frame(self.left_frame, bg="white")
        container_left.place(relx=0.5, rely=0.5, anchor="center")

        # Título
        tk.Label(container_left, text="Login", font=("Arial", 36, "bold"),
                 fg="#1E90FF", bg="white").pack(pady=(0, 10))

        tk.Label(container_left, text="Adicione os detalhes da sua conta",
                 font=("Arial", 14), fg="gray", bg="white").pack(pady=(0, 20))

        # Usuário
        tk.Label(container_left, text="Nome de usuário", font=("Arial", 12),
                 fg="gray", bg="white").pack(anchor="w")
        self.username_entry = tk.Entry(container_left, width=40, font=("Arial", 14),
                                       bd=0, relief="flat", highlightbackground="#E0E0E0", highlightthickness=1)
        self.username_entry.pack(pady=(0, 15), ipady=8)

        # Senha
        tk.Label(container_left, text="Senha", font=("Arial", 12),
                 fg="gray", bg="white").pack(anchor="w")
        self.password_entry = tk.Entry(container_left, width=40, font=("Arial", 14), show="*",
                                       bd=0, relief="flat", highlightbackground="#E0E0E0", highlightthickness=1)
        self.password_entry.pack(pady=(0, 20), ipady=8)

        # Botão Login
        tk.Button(container_left, text="Login", font=("Arial", 16, "bold"),
                  bg="#1E90FF", fg="white", bd=0, relief="flat",
                  command=self._fazer_login).pack(pady=15, ipadx=20, ipady=10)

        # Cadastre-se
        frame_register = tk.Frame(container_left, bg="white")
        frame_register.pack(pady=10)

        tk.Label(frame_register, text="Não tem uma conta?", font=("Arial", 12),
                 fg="gray", bg="white").grid(row=0, column=0, padx=5)
        tk.Button(frame_register, text="Cadastre-se", font=("Arial", 12, "bold"),
                  bg="#1E90FF", fg="white", bd=0, relief="flat",
                  command=self._cadastrar).grid(row=0, column=1, padx=5)

    def _criar_painel_direito(self):
        # Container centralizado
        container_right = tk.Frame(self.right_frame, bg="#1E90FF")
        container_right.place(relx=0.5, rely=0.5, anchor="center")

        # Títulos
        tk.Label(container_right, text="Bem-Vindo ao", font=("Arial", 24),
                 fg="white", bg="#1E90FF").pack()
        tk.Label(container_right, text="DiabetesCare", font=("Arial", 40, "bold"),
                 fg="white", bg="#1E90FF").pack()
        tk.Label(container_right, text="Faça login para acessar sua conta ou cadastre-se",
                 font=("Arial", 14), fg="white", bg="#1E90FF").pack(pady=10)

        # Imagem
        image_path = os.path.join(os.path.dirname(__file__), "imagem.png")
        try:
            original_image = Image.open(image_path)
            resized_image = original_image.resize((300, 300), Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(resized_image)
            tk.Label(container_right, image=self.photo, bg="#1E90FF").pack(pady=20)
        except Exception:
            tk.Label(container_right, text="[Ícone de Prancheta]", font=("Arial", 20),
                     fg="white", bg="#1E90FF").pack(pady=20)

    def _fazer_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        print(f"Login com Usuário: {username}, Senha: {password}")

    def _cadastrar(self):
        print("Redirecionar para tela de cadastro")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
