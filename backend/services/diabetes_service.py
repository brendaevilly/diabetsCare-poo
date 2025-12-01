import requests

class DiabetsCareService:
    def __init__(self,  base_url = "http://127.0.0.1:5000"):
        self.base_url = base_url
        self.token = None  
    
    # autenticacao

    def register_user(self, username, password, tipo="Comum"):
        payload = {
            "username": username,
            "password": password,
            "tipo": tipo
        }

        response = requests.post(f"{self.base_url}/auth/signup_screen", json=payload)
        return response.json()
    
    def login(self, username, password):
        payload = { "username": username, "password": password }
        r = requests.post(f"{self.base_url}/auth/login_screen", json=payload)

        if r.status_code == 200:
            data = r.json()
            self.token = data["token"]
            return data
        else:
            return {"error": "Credenciais inválidas"}
        
    def get_current_user(self):
        if not self.token:
            return None
        headers = {"Authorization": f"Bearer {self.token}"}
        r = requests.get(f"{self.base_url}/auth/me", headers=headers)
        return r.json()

#posts

    def add_post(self, conteudo):
        if not self.token:
            return {"error": "Usuário não autenticado"}

        headers = {"Authorization": f"Bearer {self.token}"}
        payload = {"conteudo": conteudo}

        r = requests.post(f"{self.base_url}/posts", json=payload, headers=headers)
        return r.json()

    def get_all_posts(self):
        r = requests.get(f"{self.base_url}/posts")
        return r.json()
    
#glicemia

    def save_glycemia_record(self, dados):
        if not self.token:
            return {"error": "Usuário não autenticado"}

        headers = {"Authorization": f"Bearer {self.token}"}
        r = requests.post(f"{self.base_url}/glicemia", json=dados, headers=headers)
        return r.json()
    
    def get_glycemia_history(self):
        if not self.token:
            return {"error": "Usuário não autenticado"}

        headers = {"Authorization": f"Bearer {self.token}"}
        r = requests.get(f"{self.base_url}/glicemia", headers=headers)
        return r.json()
    

