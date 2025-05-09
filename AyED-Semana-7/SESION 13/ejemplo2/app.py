from Flask import Flask, render_template, request, redirect, url_for
from banco import Banco

app = Flask(__name__)
banco = Banco()

@app.route('/')
def index():
    cliente_actual = banco.obtener_ultimo_cliente_atendido()
    return render_template('index.html', cliente_actual=cliente_actual)

@app.route('/agregar_cliente', methods=['POST'])
def agregar_cliente():
    nombre_cliente = request.form['nombre_cliente']
    banco.llegar_cliente(nombre_cliente)
    return redirect(url_for('index'))

@app.route('/atender_cliente', methods=['POST'])
def atender_cliente():
    try:
        cliente_atendido = banco.atender_cliente()
    except IndexError:
        cliente_atendido = None
    return redirect(url_for('index'))