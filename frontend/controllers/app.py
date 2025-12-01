"""
Controller principal do aplicativo DiabetsCare.
Gerencia a navegação entre telas e coordena a comunicação entre GUI e Backend.
"""
import tkinter as tk
import sys
import os

# Adiciona o diretório raiz ao path para imports
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, root_dir)

# Imports do frontend (views)
from frontend.views.screens.login_screen import LoginScreen
from frontend.views.screens.signup_screen import SignupScreen
from frontend.views.screens.post_screen import PostScreen
from frontend.views.screens.feed_screen import FeedScreen
from frontend.views.screens.glycemia_screen import GlycemiaScreen
from frontend.views.screens.dashboard_screen import DashboardScreen
from frontend.views.screens.user_data_screen import UserDataScreen

# Imports do backend (services e repositories)
from backend.services.diabetes_service import DiabetsCareService


class App(tk.Tk):
    """
    Classe principal do aplicativo.
    Gerencia a janela principal, navegação entre telas e inicialização do backend.
    """
    
    def __init__(self):
        super().__init__()
        self.title("DiabetsCare")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")
        self.configure(bg="#F0F2F5")  # Cor de fundo geral da aplicação

        # Container para os frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Inicialização do Backend (Arquitetura em Camadas)
        # 1. Cria o Repositório (persistência em arquivos)
        
        # 2. Cria o Serviço (lógica de negócio)
        self.service = DiabetsCareService()
        
        # Alias para compatibilidade com código existente
        self.DiabetsCareService = self.service

        # Adiciona as telas
        for F in (LoginScreen, SignupScreen, FeedScreen, PostScreen, GlycemiaScreen, 
                  DashboardScreen, UserDataScreen):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Começa na tela de login
        self.show_frame("LoginScreen") 

    def show_frame(self, page_name):
        """
        Mostra um frame para a página dada.
        Atualiza o feed se necessário usando threading para não bloquear a GUI.
        
        Args:
            page_name: Nome da tela a ser exibida
        """
        frame = self.frames[page_name]
        
        if page_name == "FeedScreen":
            # A atualização do feed será feita com threading na própria tela
            # para não bloquear a GUI durante a leitura de dados
            frame.update_feed()  
        
        frame.tkraise()

    def adicionar_post(self, conteudo):
        """
        Adiciona um novo post através do serviço.
        A operação de salvamento deve ser feita com threading na tela PostScreen.
        
        Args:
            conteudo: Conteúdo do post (string)
        """
        try:
            self.service.add_post(conteudo)  
        except Exception as e:
            print(f"Erro ao adicionar post: {e}")
            raise


if __name__ == "__main__":
    app = App()
    app.mainloop()
