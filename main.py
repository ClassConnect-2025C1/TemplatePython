from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def root():
    return "Servidor funcionando en Python"

@app.route('/healthcheck')
def healthcheck():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = 8080
    print(f"Servidor escuchando en el puerto {port}")
    try:
        app.run(host='0.0.0.0', port=port)
    except Exception as e:
        print(f"Error al iniciar el servidor: {e}")
