from flask import Flask, render_template, request, jsonify
from controllers.controlador import Controlador

app = Flask(__name__)
controlador_app = Controlador()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enqueue', methods=['POST'])
def enqueue():
    data = request.json
    nombre = data.get('nombre')
    if nombre:
        controlador_app._modelo.enqueue(nombre)
        return jsonify({'message': f'Paciente {nombre} agregado a la cola.'}), 200
    return jsonify({'error': 'Nombre no proporcionado.'}), 400

@app.route('/dequeue', methods=['POST'])
def dequeue():
    paciente_atendido = controlador_app._modelo.dequeue()
    if paciente_atendido:
        return jsonify({'message': f'Paciente {paciente_atendido} atendido.'}), 200
    return jsonify({'error': 'No hay pacientes en la cola.'}), 400

@app.route('/cola', methods=['GET'])
def cola():
    cola_actual = controlador_app._modelo.obtener_cola_completa()
    return jsonify(cola_actual), 200

if __name__ == '__main__':
    app.run(debug=True)