from models.pila_sacos import PilaSacos
from views.vista_pila import VistaPila

class ControladorPila:
    def __init__(self):
        self.modelo = PilaSacos()
        self.vista = VistaPila()

    def ejecutar(self):
        while True:
            self.vista.mostrar_menu()
            opcion = self.vista.obtener_opcion()

            if opcion == '1':
                nombre_saco = self.vista.obtener_nombre_saco()
                self.modelo.apilar(nombre_saco)
            elif opcion == '2':
                saco_desapilado = self.modelo.desapilar()
                self.vista.mostrar_saco_desapilado(saco_desapilado)
            elif opcion == '3':
                tope_pila = self.modelo.ver_tope()
                self.vista.mostrar_tope_pila(tope_pila)
            elif opcion == '4':
                self.vista.mostrar_pila(self.modelo.sacos)
            elif opcion == '5':
                break
            else:
                print("Opcion invalida")