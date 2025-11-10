"""
Camada de Repositório para persistência de dados em arquivos.
Implementa persistência em JSON para posts e usuários, e CSV para registros de glicemia.
"""
import json
import csv
import os
from datetime import datetime
from typing import List, Dict, Optional


class FileRepository:
    """
    Repositório para persistência de dados em arquivos.
    Gerencia posts (JSON), usuários (JSON) e registros de glicemia (CSV).
    """
    
    def __init__(self, data_dir: str = "data"):
        """
        Inicializa o repositório com o diretório de dados.
        
        Args:
            data_dir: Diretório onde os arquivos serão salvos
        """
        self.data_dir = data_dir
        self.posts_file = os.path.join(data_dir, "posts.json")
        self.users_file = os.path.join(data_dir, "users.json")
        self.glycemia_file = os.path.join(data_dir, "glicemia.csv")
        
        # Garante que o diretório existe
        os.makedirs(data_dir, exist_ok=True)
        
        # Inicializa arquivos se não existirem
        self._initialize_files()
    
    def _initialize_files(self):
        """Inicializa os arquivos se não existirem"""
        if not os.path.exists(self.posts_file):
            self.save_posts([])
        
        if not os.path.exists(self.users_file):
            self._save_users([])
        
        if not os.path.exists(self.glycemia_file):
            self._initialize_glycemia_csv()
    
    def _initialize_glycemia_csv(self):
        """Inicializa o arquivo CSV de glicemia com cabeçalhos"""
        with open(self.glycemia_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'data', 'jejum', 'pos_prandial', 'dormir', 'observacoes'])
            writer.writeheader()
    
    # ========== MÉTODOS PARA POSTS (JSON) ==========
    
    def load_posts(self) -> List[Dict]:
        """
        Carrega todos os posts do arquivo JSON.
        
        Returns:
            Lista de posts (dicionários)
        """
        if not os.path.exists(self.posts_file):
            return []
        
        try:
            with open(self.posts_file, 'r', encoding='utf-8') as f:
                posts = json.load(f)
                return posts if isinstance(posts, list) else []
        except (json.JSONDecodeError, IOError) as e:
            print(f"Erro ao carregar posts: {e}")
            return []
    
    def save_posts(self, posts: List[Dict]):
        """
        Salva a lista completa de posts no arquivo JSON.
        
        Args:
            posts: Lista de posts (dicionários) para salvar
        """
        try:
            with open(self.posts_file, 'w', encoding='utf-8') as f:
                json.dump(posts, f, indent=4, ensure_ascii=False)
        except IOError as e:
            raise Exception(f"Erro ao salvar posts: {e}")
    
    def get_next_post_id(self, posts: List[Dict]) -> int:
        """
        Gera o próximo ID único para um post.
        
        Args:
            posts: Lista de posts existentes
            
        Returns:
            Próximo ID disponível
        """
        if not posts:
            return 1
        
        ids = [post.get('id', 0) for post in posts if isinstance(post, dict)]
        return max(ids, default=0) + 1
    
    def add_post(self, post: Dict) -> Dict:
        """
        Adiciona um novo post à lista.
        
        Args:
            post: Dicionário com dados do post
            
        Returns:
            Post criado com ID e timestamp
        """
        posts = self.load_posts()
        
        # Adiciona ID e timestamp se não existirem
        if 'id' not in post:
            post['id'] = self.get_next_post_id(posts)
        
        if 'timestamp' not in post:
            post['timestamp'] = datetime.now().isoformat()
        
        posts.append(post)
        self.save_posts(posts)
        return post
    
    # ========== MÉTODOS PARA USUÁRIOS (JSON) ==========
    
    def load_users(self) -> List[Dict]:
        """
        Carrega todos os usuários do arquivo JSON.
        
        Returns:
            Lista de usuários (dicionários)
        """
        if not os.path.exists(self.users_file):
            return []
        
        try:
            with open(self.users_file, 'r', encoding='utf-8') as f:
                users = json.load(f)
                return users if isinstance(users, list) else []
        except (json.JSONDecodeError, IOError) as e:
            print(f"Erro ao carregar usuários: {e}")
            return []
    
    def _save_users(self, users: List[Dict]):
        """
        Salva a lista completa de usuários no arquivo JSON.
        
        Args:
            users: Lista de usuários (dicionários) para salvar
        """
        try:
            with open(self.users_file, 'w', encoding='utf-8') as f:
                json.dump(users, f, indent=4, ensure_ascii=False)
        except IOError as e:
            raise Exception(f"Erro ao salvar usuários: {e}")
    
    def find_user_by_username(self, username: str) -> Optional[Dict]:
        """
        Busca um usuário pelo nome de usuário.
        
        Args:
            username: Nome de usuário para buscar
            
        Returns:
            Dicionário do usuário ou None se não encontrado
        """
        users = self.load_users()
        for user in users:
            if user.get('username') == username:
                return user
        return None
    
    def add_user(self, user: Dict) -> Dict:
        """
        Adiciona um novo usuário.
        
        Args:
            user: Dicionário com dados do usuário (username, password, tipo)
            
        Returns:
            Usuário criado (sem senha)
            
        Raises:
            ValueError: Se o usuário já existir
        """
        users = self.load_users()
        
        # Verifica se o usuário já existe
        if self.find_user_by_username(user.get('username')):
            raise ValueError(f"Usuário '{user.get('username')}' já existe")
        
        # Adiciona data de criação
        user['created_at'] = datetime.now().isoformat()
        
        users.append(user)
        self._save_users(users)
        
        # Retorna usuário sem senha
        user_copy = user.copy()
        user_copy.pop('password', None)
        return user_copy
    
    def verify_user(self, username: str, password: str) -> Optional[Dict]:
        """
        Verifica as credenciais de um usuário.
        
        Args:
            username: Nome de usuário
            password: Senha
            
        Returns:
            Dicionário do usuário (sem senha) se as credenciais estiverem corretas, None caso contrário
        """
        user = self.find_user_by_username(username)
        if user and user.get('password') == password:
            user_copy = user.copy()
            user_copy.pop('password', None)
            return user_copy
        return None
    
    # ========== MÉTODOS PARA GLICEMIA (CSV) ==========
    
    def load_glycemia_records(self) -> List[Dict]:
        """
        Carrega todos os registros de glicemia do arquivo CSV.
        
        Returns:
            Lista de registros (dicionários)
        """
        if not os.path.exists(self.glycemia_file):
            return []
        
        records = []
        try:
            with open(self.glycemia_file, 'r', encoding='utf-8', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Converte valores numéricos
                    if 'id' in row and row['id']:
                        row['id'] = int(row['id'])
                    if 'jejum' in row and row['jejum']:
                        row['jejum'] = int(row['jejum'])
                    if 'pos_prandial' in row and row['pos_prandial']:
                        row['pos_prandial'] = int(row['pos_prandial'])
                    if 'dormir' in row and row['dormir']:
                        row['dormir'] = int(row['dormir'])
                    records.append(row)
        except (IOError, ValueError) as e:
            print(f"Erro ao carregar registros de glicemia: {e}")
            return []
        
        return records
    
    def append_glycemia_record(self, record: Dict) -> Dict:
        """
        Adiciona um novo registro de glicemia ao arquivo CSV.
        
        Args:
            record: Dicionário com dados do registro (jejum, pos_prandial, dormir, observacoes)
            
        Returns:
            Registro criado com ID e data
        """
        # Carrega registros existentes para gerar ID
        existing_records = self.load_glycemia_records()
        
        # Gera ID
        if existing_records:
            ids = [r.get('id', 0) for r in existing_records if isinstance(r.get('id'), int)]
            next_id = max(ids, default=0) + 1
        else:
            next_id = 1
        
        # Adiciona ID e data se não existirem
        record['id'] = next_id
        if 'data' not in record:
            record['data'] = datetime.now().strftime('%Y-%m-%d')
        
        # Garante que todos os campos necessários existam
        record.setdefault('jejum', '')
        record.setdefault('pos_prandial', '')
        record.setdefault('dormir', '')
        record.setdefault('observacoes', '')
        
        # Adiciona ao arquivo CSV usando append
        try:
            with open(self.glycemia_file, 'a', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['id', 'data', 'jejum', 'pos_prandial', 'dormir', 'observacoes'])
                writer.writerow(record)
        except IOError as e:
            raise Exception(f"Erro ao salvar registro de glicemia: {e}")
        
        return record
