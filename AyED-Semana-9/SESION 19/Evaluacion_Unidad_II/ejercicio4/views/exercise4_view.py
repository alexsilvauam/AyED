class Exercise4View:
    def show_menu(self):
        print("\n=== EJERCICIO 4: COLA DE PRIORIDAD ===")
        print("1. Agregar elemento")
        print("2. Eliminar elemento")
        print("3. Mostrar cola")
        print("4. Volver al menú principal")

    def show_success(self, message):
        print(f"\n✓ {message}")

    def show_error(self, message):
        print(f"\n✗ {message}")

    def show_removed_element(self, element):
        print(f"\nElemento eliminado: {element[0]} (Prioridad: {element[1]})")

    def show_queue(self, queue):
        print("\nCola de prioridad actual:")
        if not queue:
            print("La cola está vacía")
        else:
            for i, (name, priority) in enumerate(queue, 1):
                print(f"{i}. {name} (Prioridad: {priority})")

    def show_invalid_option(self):
        print("Opción no válida. Por favor, intente de nuevo.") 