class Exercise5View:
    def show_menu(self):
        print("\n=== EJERCICIO 5: BÚSQUEDA EN LISTA ENLAZADA ===")
        print("1. Agregar elemento")
        print("2. Buscar elemento")
        print("3. Mostrar lista")
        print("4. Volver al menú principal")

    def show_success(self, message):
        print(f"\n✓ {message}")

    def show_search_result(self, value, position):
        if position != -1:
            print(f"\nEl valor '{value}' se encontró en la posición {position}")
        else:
            print(f"\nEl valor '{value}' no se encontró en la lista")

    def show_list(self, elements):
        print("\nLista actual:")
        if not elements:
            print("La lista está vacía")
        else:
            for i, element in enumerate(elements):
                print(f"{i}. {element}")

    def show_invalid_option(self):
        print("Opción no válida. Por favor, intente de nuevo.") 