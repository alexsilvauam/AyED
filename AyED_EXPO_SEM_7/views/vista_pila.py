class VistaPila:
    def mostrar_menu(self):
        print("\n--- Gestión de Sacos ---")
        print("1. Apilar saco")
        print("2. Desapilar saco")
        print("3. Ver tope de la pila")
        print("4. Mostrar pila")
        print("5. Salir")

    def obtener_opcion(self):
        return input("Seleccione una opción: ")

    def obtener_nombre_saco(self):
        return input("Ingrese el nombre del saco a apilar: ")

    def mostrar_saco_desapilado(self, saco):
        if saco:
            print(f"Se ha desapilado el saco: {saco}")
        else:
            print("La pila está vacía, no se puede desapilar.")

    def mostrar_tope_pila(self, saco):
        if saco:
            print(f"El saco en el tope de la pila es: {saco}")
        else:
            print("La pila está vacía.")

    def mostrar_pila(self, pila):
        if pila:
            print("La pila de sacos es (el último ingresado está arriba):")
            for saco in reversed(pila):
                print(f"- {saco}")
        else:
            print("La pila está vacía.")