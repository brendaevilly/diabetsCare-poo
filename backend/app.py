"""
Aplicação Flask principal do DiabetsCare.
Este arquivo será expandido pelo Dev 2 com a implementação completa da API REST.
"""
from flask import Flask, jsonify

app = Flask(__name__)

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

