class ServicoDiabetsCare:
    def __init__(self, repositorio_post, repositorio_glicemia):
        self.repositorio_post = repositorio_post
        self.repositorio_glicemia = repositorio_glicemia
    
    def adicionarPost(self, conteudo):
        if not conteudo or len(conteudo.strip()) == 0:
            raise ValueError("O conteúdo do post não pode ser vazio.")
        
        post_data = {"user": "Usuário Padrão", "content": conteudo}
        self.repositorio_post.adiciona(post_data)  

    def getPost(self):
        return self.repositorio_post.getPost()   

    def adicionarGlicemia(self, dados_glicemia):  
        if not isinstance(dados_glicemia.get('value'), (int, float)) or dados_glicemia.get('value') <= 0:
            raise ValueError("O valor da glicemia deve ser um número positivo.")
            
    def getHistoricoPost(self):
        return self.repositorio_post.getPost()


class RepositorioPost:
    def __init__(self):
        self.posts = []

    def adiciona(self, post):
        self.posts.insert(0, post)
    
    def getPost(self):
        return self.posts
    

class RepositorioGlicemia:
    def __init__(self):
        self.historico_glicemia = []

    def adicionarGlicemia(self, dados_glicemia):
        self.historico_glicemia.append(dados_glicemia)

    def getHistoricoGlicemia(self):
        return self.historico_glicemia
    

repositorio_post = RepositorioPost()
repositorio_glicemia = RepositorioGlicemia()

Servico_Diabets_Care = ServicoDiabetsCare(repositorio_post, repositorio_glicemia)
