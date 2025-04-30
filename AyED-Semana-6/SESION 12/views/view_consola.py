def mostrar_menu_principal():
    """Muestra el menú principal y devuelve la opción elegida."""
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Comprueba si la pila está vacía.")    
    print("2. Agrega un nuevo ítem en el tope de la pila.")
    print("3. Elimina el ítem en el tope de la pila.")
    print("4. Ver el tope de la pila")
    print("5. Ver el tamanio de la pila")
    print("0. Salir")
    while True:
        opcion = input("Seleccione una opción: ")
        if opcion.isdigit() and 0 <= int(opcion) <= 5:
            return int(opcion)
        else:
            print("Opción no válida. Intente de nuevo.")