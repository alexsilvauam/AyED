from banco import Banco

def mostrar_menu():
    print("1. Llegar cliente")
    print("2. Atender cliente")
    print("3. Mostrar clientes en espera")
    print("4. Salir")

def main():
    banco = Banco()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            cliente = input("Ingrese el nombre del cliente: ")
            banco.llegar_cliente(cliente)
            print(f"Cliente {cliente} ha llegado.")
        elif opcion == "2":
            try:
                cliente_atendido = banco.atender_cliente()
                print(f"Atendiendo al cliente: {cliente_atendido}")
            except IndexError as e:
                print(e)
        elif opcion == "3":
            clientes_en_espera = banco.obtener_cliente_en_espera()
            print("Clientes en espera:", clientes_en_espera)
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()

