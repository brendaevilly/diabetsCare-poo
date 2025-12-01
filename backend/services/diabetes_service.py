import requests

class DiabetsCareService:
    def __init__(self,  base_url = "http://127.0.0.1:5000"):
        self.base_url = base_url
        self.token = None  
    
    # autenticacao

    def register_user(self, username, password, tipo):
        payload = {
            "username": username,
            "password": password,
            "tipo": tipo
        }

        response = requests.post(f"{self.base_url}/auth/register", json=payload)
        if response.status_code != 201:
            try:
                err = response.json().get('error')
            except Exception:
                err = response.text
            raise Exception(err or 'Erro ao registrar usuário')
        return response.json()
    
    def login(self, username, password):
        payload = {"username": username, "password": password}
        r = requests.post(f"{self.base_url}/auth/login", json=payload)
        
        if r.status_code != 200:
            try:
                msg = r.json().get('error')
            except Exception:
                msg = r.text
            raise Exception(msg or 'Credenciais inválidas')
        
        data = r.json()
        self.token = data.get("access_token") or data.get("token")  #
        
        try:
            user = self.get_current_user()
            return user
        except Exception as e:
            print(f"Erro ao validar token: {e}")
            raise Exception("Token inválido")
        
    def get_current_user(self):
        if not self.token:
            return None
        headers = {"Authorization": f"Bearer {self.token}"}
        r = requests.get(f"{self.base_url}/auth/me", headers=headers)
        return r.json()

#posts

    def add_post(self, conteudo):
        if not self.token:
            raise Exception("Usuário não autenticado")
        
        conteudo_str = str(conteudo) if conteudo is not None else ""
        
        if not conteudo_str or not conteudo_str.strip():
            raise Exception("O conteúdo do post não pode estar vazio")

        headers = {"Authorization": f"Bearer {self.token}"}
        payload = {"conteudo": conteudo.strip()}

        r = requests.post(f"{self.base_url}/posts", json=payload, headers=headers)
        if not r.ok:
            print("Status:", r.status_code)
            print("Response:", r.text)
            raise Exception("Erro ao criar post/glicemia")

        return r.json()

    def adicionarPost(self, conteudo):
        return self.add_post(conteudo)


    def get_all_posts(self):
        r = requests.get(f"{self.base_url}/posts")
        return r.json()
    
    def listarPostsPorUsuario(self, user_id):
        r = requests.get(f"{self.base_url}/posts/user/{user_id}")
        return r.json()
    
#glicemia

    def save_glycemia_record(self, dados):
        if not self.token:
            raise Exception("Usuário não autenticado")

        headers = {"Authorization": f"Bearer {self.token}"}
        r = requests.post(f"{self.base_url}/glicemia", json=dados, headers=headers)
        if not r.ok:
            try:
                msg = r.json().get('error')
            except Exception:
                msg = r.text
            raise Exception(msg or 'Erro ao salvar registro de glicemia')
        return r.json()

    # alias used by frontend: adicionarGlicemia
    def adicionarGlicemia(self, dados):
        return self.save_glycemia_record(dados)
    
    def get_glycemia_history(self):
        if not self.token:
            raise Exception("Usuário não autenticado")

        headers = {"Authorization": f"Bearer {self.token}"}
        r = requests.get(f"{self.base_url}/glicemia", headers=headers)
        if not r.ok:
            try:
                msg = r.json().get('error')
            except Exception:
                msg = r.text
            raise Exception(msg or 'Erro ao obter histórico de glicemia')
        return r.json()
    

