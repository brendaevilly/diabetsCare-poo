import tkinter as tk
from tkinter import ttk
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

        self.left_frame = tk.Frame(self.root, bg="white", width=screen_width // 2, height=screen_height)
        self.left_frame.pack(side="left", fill="both", expand=True)

        self.right_frame = tk.Frame(self.root, bg="#1A73E8", width=screen_width // 2, height=screen_height)   
        self.right_frame.pack(side="right", fill="both", expand=True)

        self._criar_painel_esquerdo()
        self._criar_painel_direito()

    def _criar_painel_esquerdo(self):
        login_label = tk.Label(self.left_frame, text="Login", font=("Arial", 36, "bold"), fg="#1A73E8", bg="white")   
        login_label.place(relx=0.5, rely=0.2, anchor="center")

        subtitle_label = tk.Label(self.left_frame, text="Adicione os detalhes da sua conta", font=("Arial", 14), fg="gray", bg="white")
        subtitle_label.place(relx=0.5, rely=0.28, anchor="center")

        username_label = tk.Label(self.left_frame, text="Nome de usuário", font=("Arial", 12), fg="gray", bg="white")
        username_label.place(relx=0.5, rely=0.38, anchor="s")
        self.username_entry = tk.Entry(self.left_frame, width=40, font=("Arial", 14), bd=0, relief="flat", highlightbackground="#E0E0E0", highlightthickness=1)
        self.username_entry.place(relx=0.5, rely=0.42, anchor="center", height=45)

        password_label = tk.Label(self.left_frame, text="Senha", font=("Arial", 12), fg="gray", bg="white")
        password_label.place(relx=0.5, rely=0.52, anchor="s")
        self.password_entry = tk.Entry(self.left_frame, width=40, font=("Arial", 14), show="*", bd=0, relief="flat", highlightbackground="#E0E0E0", highlightthickness=1)
        self.password_entry.place(relx=0.5, rely=0.56, anchor="center", height=45)

        login_button = tk.Button(self.left_frame, text="Login", font=("Arial", 16, "bold"), bg="#1A73E8", fg="white", bd=0, relief="flat", command=self._fazer_login) # Cor e função alteradas
        login_button.place(relx=0.5, rely=0.68, anchor="center", width=150, height=50)

        no_account_label = tk.Label(self.left_frame, text="Não tem uma conta?", font=("Arial", 12), fg="gray", bg="white")
        no_account_label.place(relx=0.5, rely=0.85, anchor="e")

        register_button = tk.Button(self.left_frame, text="Cadastre-se", font=("Arial", 14, "bold"), bg="#1A73E8", fg="white", bd=0, relief="flat", command=self._cadastrar) # Cor e função alteradas
        register_button.place(relx=0.5, rely=0.85, anchor="w", width=180, height=50)

    def _criar_painel_direito(self):
        welcome_label = tk.Label(self.right_frame, text="Bem-Vindo ao", font=("Arial", 24), fg="white", bg="#1A73E8")   
        welcome_label.place(relx=0.5, rely=0.2, anchor="center")

        diabetes_label = tk.Label(self.right_frame, text="DiabetesCare", font=("Arial", 40, "bold"), fg="white", bg="#1A73E8")   
        diabetes_label.place(relx=0.5, rely=0.28, anchor="center")

        right_subtitle_label = tk.Label(self.right_frame, text="Faça login para acessar sua conta ou cadastre-se", font=("Arial", 14), fg="white", bg="#1A73E8")   
        right_subtitle_label.place(relx=0.5, rely=0.35, anchor="center")

        image_path = os.path.join(os.path.dirname(__file__), "imagem.png")
        try:
            original_image = Image.open(image_path)
            resized_image = original_image.resize((300, 300), Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(resized_image)
            image_label = tk.Label(self.right_frame, image=self.photo, bg="#1A73E8")   
            image_label.place(relx=0.5, rely=0.65, anchor="center")
        except FileNotFoundError:
            print(f"Erro: imagem.png não encontrada em {image_path}.")
            image_placeholder = tk.Label(self.right_frame, text="[Ícone de Prancheta]", font=("Arial", 20), fg="white", bg="#1A73E8")   
            image_placeholder.place(relx=0.5, rely=0.65, anchor="center")
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")
            image_placeholder = tk.Label(self.right_frame, text="[Ícone de Prancheta]", font=("Arial", 20), fg="white", bg="#1A73E8")   
            image_placeholder.place(relx=0.5, rely=0.65, anchor="center")

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
