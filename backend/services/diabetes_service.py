class Servico_Diabets_Care:
    def __init__(self, repositorio_post, repositorio_glicemia):
        self.repositorio_post = repositorio_post
        self.repositorio_glicemia = repositorio_glicemia
    
    def adicionarPost(self, conteudo):
        """
        Agora aceita um dicionário com dados estruturados (por exemplo {'data': '2025-11-09','valor': 110})
        ou uma string. Normaliza para um dicionário antes de salvar.
        """
        # aceita string -> transforma em post simples
        if isinstance(conteudo, str):
            texto = conteudo.strip()
            if not texto:
                raise ValueError("O conteúdo do post não pode ser vazio.")
            post_data = {"user": "Usuário Padrão", "content": texto}
            self.repositorio_post.adiciona(post_data)
            return

        # aceita dicionário -> valida e salva
        if isinstance(conteudo, dict):
            if not conteudo:
                raise ValueError("Os dados do post não podem ser vazios.")

            # Normaliza campos: se vier {'data','valor'} transformamos em um post
            post_data = conteudo.copy()
            # opcional: garanta que haja um campo 'user' e 'type'
            post_data.setdefault("user", "Usuário Padrão")
            post_data.setdefault("type", "registro_glicemia")
            # por exemplo, se veio data+valor, mantém isso:
            self.repositorio_post.adiciona(post_data)
            return

        # tipo inválido
        raise ValueError("Conteúdo inválido: deve ser string ou dicionário.")  

    def getPost(self):
        return self.repositorio_post.getPost()   

    def adicionarGlicemia(self, dados_glicemia):  
        if not dados_glicemia:
            raise ValueError("Os dados de glicemia não podem estar vazios.")
        
        self.repositorio_glicemia.adicionarGlicemia(dados_glicemia)
            
    def getHistoricoPost(self):
        return self.repositorio_post.getPost()


class RepositorioPost:
    def __init__(self):
        self.posts = []

    def adiciona(self, post):
        self.posts.append(post)
    
    def getPost(self):
        return self.posts
    

class RepositorioGlicemia:
    def __init__(self):
        self.historico_glicemia = []

    def adicionarGlicemia(self, dados_glicemia):
        self.historico_glicemia.append(dados_glicemia)

    def getHistoricoGlicemia(self):
        return self.historico_glicemia
    

