import tkinter as tk
from post_screen import PostScreen
from feed_screen import FeedScreen
from glycemia_screen import GlycemiaScreen
from DiabetsCareService import Servico_Diabets_Care

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicativo de Posts e Glicemia")
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

      
        self.DiabetsCareService = Servico_Diabets_Care

        # Adiciona as telas
        for F in (FeedScreen, PostScreen, GlycemiaScreen):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("FeedScreen") 

    def show_frame(self, page_name):
        """Mostra um frame para a página dada"""
        frame = self.frames[page_name]
        if page_name == "FeedScreen":
            frame.update_feed()  
        frame.tkraise()

    def adicionar_post(self, conteudo):
        try:
            self.DiabetsCareService.adicionarPost(conteudo)  
        except Exception as e:
            print(f"Erro ao adicionar post: {e}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
