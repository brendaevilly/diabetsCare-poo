"""
Aplicação Flask principal do DiabetsCare.
Este arquivo será expandido pelo Dev 2 com a implementação completa da API REST.
"""
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from config import db, init_db, JWT_SECRET

from controllers.auth_controller import auth_controller
from controllers.post_controller import post_controller
from controllers.glicemia_controller import glicemia_controller

app = Flask(__name__)


# Configuração do JWT
app.config["JWT_SECRET_KEY"] = JWT_SECRET
jwt = JWTManager(app)

# Inicializar o banco de dados
init_db(app)

# Registrar blueprints (controllers)
app.register_blueprint(auth_controller, url_prefix="/auth")
app.register_blueprint(post_controller, url_prefix="/posts")
app.register_blueprint(glicemia_controller, url_prefix="/glicemia")
for rule in app.url_map.iter_rules():
    print(rule)


@app.route('/')
def health_check():
    """Endpoint de verificação de saúde da API"""
    return jsonify({
        'status': 'ok',
        'mensagem': 'API DiabetsCare está rodando',
        'versao': '1.0.0'
    })

@app.route('/api/health', methods=['GET'])
def api_health():
    """Endpoint de saúde da API"""
    return jsonify({
        'status': 'healthy',
        'servico': 'DiabetsCare Backend'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)