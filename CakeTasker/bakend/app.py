from flask import Flask, jsonify, request
from db_manager import DBManager
import config

app = Flask(__name__)

# Conexión a la base de datos
db_manager = DBManager(config)

# ------------------------------
# 1. CREAR PEDIDO (POST)
# ------------------------------
@app.route('/pedidos', methods=['POST'])
def crear_pedido():
    datos = request.json

    nuevo_id = db_manager.crear(datos)

    return jsonify({
        "mensaje": "Pedido creado correctamente",
        "id": nuevo_id
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
