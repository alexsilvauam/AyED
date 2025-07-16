class Exercise2View:
    def show_menu(self):
        print("\n=== EJERCICIO 2: VERIFICACIÓN DE PARÉNTESIS ===")
        print("1. Verificar expresión")
        print("2. Volver al menú principal")

    def show_result(self, is_balanced):
        if is_balanced:
            print("\nLa expresión está balanceada.")
        else:
            print("\nLa expresión NO está balanceada.")

    def show_invalid_option(self):
        print("Opción no válida. Por favor, intente de nuevo.") 