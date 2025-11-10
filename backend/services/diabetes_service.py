"""
Camada de Serviço para o DiabetsCare.
Gerencia regras de negócio e coordena operações entre a GUI e o Repositório.
"""
from backend.repositories.file_repository import FileRepository
from typing import List, Dict, Optional


class DiabetsCareService:
    """
    Serviço principal do DiabetsCare.
    Gerencia posts, registros de glicemia e autenticação de usuários.
    """
    
    def __init__(self, repository: FileRepository = None):
        """
        Inicializa o serviço com um repositório.
        
        Args:
            repository: Instância do FileRepository. Se None, cria uma nova.
        """
        if repository is None:
            repository = FileRepository()
        self.repository = repository
        self.current_user: Optional[Dict] = None
    
    # ========== MÉTODOS DE AUTENTICAÇÃO ==========
    
    def register_user(self, username: str, password: str, tipo: str = "Comum") -> Dict:
        """
        Registra um novo usuário.
        
        Args:
            username: Nome de usuário
            password: Senha
            tipo: Tipo de usuário ("Comum" ou "Profissional")
            
        Returns:
            Dicionário com dados do usuário criado (sem senha)
            
        Raises:
            ValueError: Se o usuário já existir ou dados inválidos
        """
        if not username or not username.strip():
            raise ValueError("Nome de usuário não pode estar vazio")
        
        if not password or not password.strip():
            raise ValueError("Senha não pode estar vazia")
        
        if tipo not in ["Comum", "Profissional"]:
            raise ValueError("Tipo de usuário deve ser 'Comum' ou 'Profissional'")
        
        user_data = {
            "username": username.strip(),
            "password": password.strip(),
            "tipo": tipo
        }
        
        return self.repository.add_user(user_data)
    
    def login(self, username: str, password: str) -> Dict:
        """
        Autentica um usuário.
        
        Args:
            username: Nome de usuário
            password: Senha
            
        Returns:
            Dicionário com dados do usuário (sem senha)
            
        Raises:
            ValueError: Se as credenciais forem inválidas
        """
        if not username or not password:
            raise ValueError("Nome de usuário e senha são obrigatórios")
        
        user = self.repository.verify_user(username.strip(), password.strip())
        
        if not user:
            raise ValueError("Nome de usuário ou senha incorretos")
        
        self.current_user = user
        return user
    
    def logout(self):
        """Faz logout do usuário atual"""
        self.current_user = None
    
    def get_current_user(self) -> Optional[Dict]:
        """
        Retorna o usuário atualmente autenticado.
        
        Returns:
            Dicionário com dados do usuário ou None
        """
        return self.current_user
    
    # ========== MÉTODOS PARA POSTS ==========
    
    def add_post(self, conteudo: str) -> Dict:
        """
        Adiciona um novo post.
        
        Args:
            conteudo: Conteúdo do post (string)
            
        Returns:
            Dicionário com o post criado
            
        Raises:
            ValueError: Se o conteúdo for vazio
        """
        if not conteudo or not conteudo.strip():
            raise ValueError("O conteúdo do post não pode ser vazio")
        
        # Obtém o usuário atual ou usa um padrão
        user = self.current_user
        username = user.get('username', 'Usuário Padrão') if user else 'Usuário Padrão'
        
        post_data = {
            "user": username,
            "content": conteudo.strip()
        }
        
        return self.repository.add_post(post_data)
    
    def get_all_posts(self) -> List[Dict]:
        """
        Retorna todos os posts.
        
        Returns:
            Lista de posts (dicionários)
        """
        return self.repository.load_posts()
    
    # ========== MÉTODOS PARA GLICEMIA ==========
    
    def save_glycemia_record(self, dados: Dict) -> Dict:
        """
        Salva um novo registro de glicemia.
        
        Args:
            dados: Dicionário com dados de glicemia (jejum, pos_prandial, dormir, observacoes)
            
        Returns:
            Dicionário com o registro criado
            
        Raises:
            ValueError: Se os dados forem inválidos
        """
        if not dados:
            raise ValueError("Os dados de glicemia não podem estar vazios")
        
        # Valida campos obrigatórios
        required_fields = ['jejum', 'pos_prandial', 'dormir']
        for field in required_fields:
            if field not in dados:
                raise ValueError(f"Campo '{field}' é obrigatório")
        
        return self.repository.append_glycemia_record(dados)
    
    def get_glycemia_history(self) -> List[Dict]:
        """
        Retorna o histórico de registros de glicemia.
        
        Returns:
            Lista de registros (dicionários)
        """
        return self.repository.load_glycemia_records()
    
    # ========== MÉTODOS DE COMPATIBILIDADE (para código existente) ==========
    
    def adicionarPost(self, conteudo):
        """
        Método de compatibilidade com código existente.
        Aceita string ou dicionário.
        """
        if isinstance(conteudo, str):
            return self.add_post(conteudo)
        elif isinstance(conteudo, dict):
            # Se for dicionário, tenta extrair conteúdo ou usar como post completo
            if 'content' in conteudo:
                return self.add_post(conteudo['content'])
            else:
                # Adiciona como post completo
                return self.repository.add_post(conteudo)
        else:
            raise ValueError("Conteúdo inválido: deve ser string ou dicionário")
    
    def getPost(self):
        """Método de compatibilidade com código existente"""
        return self.get_all_posts()
    
    def adicionarGlicemia(self, dados_glicemia: Dict):
        """Método de compatibilidade com código existente"""
        return self.save_glycemia_record(dados_glicemia)
    
    def getHistoricoPost(self):
        """Método de compatibilidade com código existente"""
        return self.get_all_posts()


# ========== CLASSES DE COMPATIBILIDADE (para código existente) ==========

class Servico_Diabets_Care:
    """
    Classe de compatibilidade com código existente.
    Mantém a interface antiga enquanto usa a nova implementação.
    """
    
    def __init__(self, repositorio_post=None, repositorio_glicemia=None):
        # Ignora os repositórios antigos e usa o novo FileRepository
        self.service = DiabetsCareService()
    
    def adicionarPost(self, conteudo):
        return self.service.adicionarPost(conteudo)
    
    def getPost(self):
        return self.service.getPost()
    
    def adicionarGlicemia(self, dados_glicemia):
        return self.service.adicionarGlicemia(dados_glicemia)
    
    def getHistoricoPost(self):
        return self.service.getHistoricoPost()


class RepositorioPost:
    """
    Classe de compatibilidade (deprecated).
    Mantida apenas para compatibilidade com código existente.
    """
    def __init__(self):
        pass
    
    def adiciona(self, post):
        pass
    
    def getPost(self):
        return []


class RepositorioGlicemia:
    """
    Classe de compatibilidade (deprecated).
    Mantida apenas para compatibilidade com código existente.
    """
    def __init__(self):
        pass
    
    def adicionarGlicemia(self, dados_glicemia):
        pass
    
    def getHistoricoGlicemia(self):
        return []
