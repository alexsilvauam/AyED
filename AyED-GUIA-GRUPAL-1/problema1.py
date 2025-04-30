"""Desarrolla una clase llamada PilaCaracteres para trabajar exclusivamente con caracteres (char). 
Implementa los métodos necesarios para agregar caracteres a la pila y eliminarlos. 
A continuación, crea un método llamado invertirCadena(String texto), que reciba una cadena, 
la almacene carácter por carácter en la pila, y luego reconstruya la cadena en orden inverso. 
En la clase Main, solicita al usuario que ingrese una cadena de texto y muestra en pantalla su versión invertida utilizando tu pila."""

class PilaCaracteres:
    def __init__(self, capacidad):
        self.pila = []
        self.capacidad = capacidad

    def push(self, c):
        if len(self.pila) < self.capacidad:
            self.pila.append(c)
        else:
            print("La pila está llena. No se puede agregar más caracteres.")

    def pop(self):
        if not self.esta_vacia():
            return self.pila.pop()
        else:
            print("La pila está vacía. No se puede eliminar ningún carácter.")
            return None

    def esta_vacia(self):
        return len(self.pila) == 0

    @staticmethod
    def invertir_cadena(texto):
        pila = PilaCaracteres(len(texto))

        for c in texto:
            pila.push(c)

        invertida = ''
        while not pila.esta_vacia():
            invertida += pila.pop()

        return invertida


def main():
    texto = input("Ingrese una cadena de texto: ")
    texto_invertido = PilaCaracteres.invertir_cadena(texto)
    print("Cadena invertida:", texto_invertido)


if __name__ == "__main__":
    main()
