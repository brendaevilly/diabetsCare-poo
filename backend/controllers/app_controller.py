from backend.services.diabetes_service import Servico_Diabets_Care, RepositorioPost, RepositorioGlicemia

class App:
    def __init__(self):
        # Instancia os repositórios e o serviço principal
        self.repo_post = RepositorioPost()
        self.repo_glicemia = RepositorioGlicemia()
        self.service = Servico_Diabets_Care(self.repo_post, self.repo_glicemia)

    def show_frame(self, frame_name):
        """Exemplo de método que mostra uma tela ou chama algo no frontend."""
        print(f"Exibindo tela: {frame_name}")

    def add_post(self, conteudo):
        """Adiciona um novo post através do serviço."""
        self.service.adicionarPost(conteudo)

    def add_glicemia(self, dados_glicemia):
        """Adiciona um novo registro de glicemia através do serviço."""
        self.service.adicionarGlicemia(dados_glicemia)
