from cola import Cola

class Banco:
    def __init__(self):
        self.cola.clientes = Cola()
        self.ultimo.cliente = None

    def llegar_cliente(self, cliente):
        self.cola.clientes.encolar(cliente)
        
    def atender_cliente(self):
        self.ultimo.cliente = self.cola.clientes.desencolar()
        return self.ultimo.cliente
    
    def obtener_cliente_en_espera(self):
        return self.cola.clientes.mostrar()
    
    def obtener_ultimo_cliente_atendido(self):
        return self.ultimo.cliente