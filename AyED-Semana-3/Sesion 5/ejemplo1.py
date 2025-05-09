import statistics

class Edad:
    def __init__(self, edades):
        self.edades = edades

    def calcular_media(self):
        if not self.edades:
            return 0  # Evitar división por cero
        return sum(self.edades) / len(self.edades)

    def mostrar_media(self):
        
        media = self.calcular_media()
        return f"La edad media es: {media:.2f}"
    def calc_media(self):
        return statistics.mean(self.edades) if self.edades else 0

    def main():
        edades = []

        while True:
            try:
                entrada = input("Introduce una edad (o '-1' para terminar): ")
                edad = int(entrada)  # Convertir a entero
                if edad == -1:
                    break
                if edad < 0:
                    print("Por favor, introduce una edad válida (mayor o igual a 0).")
                    continue
                edades.append(edad)
            except ValueError:
                print("Por favor, introduce un número entero válido.")

       

        if not edades:
            print("No se han introducido edades.")
        else:
            edad_obj = Edad(edades)
            print(edad_obj.mostrar_media())
            print(f"La edad media usando statistics es: {edad_obj.calc_media():.2f}")

  

if __name__ == "__main__":
    Edad.main()