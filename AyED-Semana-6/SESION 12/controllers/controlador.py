from models.pilas import Pila

from views import view_consola


p=Pila()

def iniciar_aplicacion():
    """Inicia la aplicación principal y maneja el menú."""
    while True:
        opcion = view_consola.mostrar_menu_principal()

        if opcion == 1:
            p.estaVacia()
            print("Comprueba si esta vacia: ", p.estaVacia())
        elif opcion == 2:
            item = input("Ingrese el ítem a agregar: ")
            p.incluir(item)
            print(f"Ítem '{item}' agregado.")
        elif opcion == 3:
            if not p.estaVacia():
                item_extraido = p.extraer()
                print(f"Ítem '{item_extraido}' eliminado.")
            else:
                print("La pila está vacía. No se puede eliminar ningún ítem.")
        elif opcion == 4:
            if not p.estaVacia():
                print(f"Ítem en el tope: {p.inspeccionar()}")
            else:
                print("La pila está vacía. No hay ítem en el tope.")
        elif opcion == 5:
            print(f"Tamaño de la pila: {p.tamano()}")
            
        elif opcion == 0:
            print("Saliendo")
            break