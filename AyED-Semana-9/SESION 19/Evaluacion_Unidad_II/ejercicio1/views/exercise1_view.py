class Exercise1View:
    def show_menu(self):
        print("\n=== EJERCICIO 1: INVERSIÓN DE PALABRAS ===")
        print("1. Invertir una frase")
        print("2. Volver al menú principal")

    def show_result(self, result):
        print("\nFrase invertida:", result)

    def show_invalid_option(self):
        print("Opción no válida. Por favor, intente de nuevo.") 