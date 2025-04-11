from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
import os  # <-- IMPORTANTE!

app = Flask(__name__)
CORS(app)

# Configurações do banco (substitua pelos seus dados REAIS!)
config = {
    'host': 'br268.hostgator.com.br',        # Exemplo: 'srv123.hstgr.io'
    'user': 'welber77_welber',     # Exemplo: 'welber_user'
    'password': '1Ddeprs1#%',   # Exemplo: 'senha123'
    'database': 'welber77_root'    # Exemplo: 'welber_db'
}

@app.route('/')
def testar_conexao():
    try:
        conexao = mysql.connector.connect(**config)
        if conexao.is_connected():
            return jsonify({'mensagem': 'Conexão com MySQL bem-sucedida!'}), 200
    except Error as erro:
        return jsonify({'erro': f'Falha na conexão: {erro}'}), 500
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Pega porta definida pelo Render
    app.run(host="0.0.0.0", port=port)


