class HistorialNavegador:
    def __init__(self):
        self.historial = []

    def visitar_pagina(self, url):
        self.historial.append(url)
        print(f"Visitando: {url}")

    def mostrar_historial(self):
        if self.historial:
            print("\nHistorial completo:")
            for pagina in self.historial:
                print(pagina)
        else:
            print("El historial está vacío.")

    def pagina_actual(self):
        if self.historial:
            return self.historial[-1]
        else:
            return "No hay páginas en el historial."

    def volver_pagina_anterior(self):
        if self.historial:
            pagina_cerrada = self.historial.pop()
            print(f"Volviendo de: {pagina_cerrada}")
            if self.historial:
                print(f"Ahora estás en: {self.historial[-1]}")
            else:
                print("No hay más páginas abiertas.")
        else:
            print("No hay páginas para retroceder.")


def main():
    navegador = HistorialNavegador()

    while True:
        print("\n¿Qué quieres hacer?")
        print("1. Visitar nueva página")
        print("2. Volver a la página anterior")
        print("3. Mostrar historial")
        print("4. Mostrar página actual")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            url = input("Ingresa la URL de la nueva página: ")
            navegador.visitar_pagina(url)
        elif opcion == "2":
            navegador.volver_pagina_anterior()
        elif opcion == "3":
            navegador.mostrar_historial()
        elif opcion == "4":
            print("Página actual:", navegador.pagina_actual())
        elif opcion == "5":
            print("Saliendo del navegador...")
            break
        else:
            print("Opción no válida. Por favor elige entre 1 y 5.")


if __name__ == "__main__":
    main()