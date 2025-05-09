"""Crea una lista de cadenas de texto. Escribe un programa que recorra esta 
lista y concatene todas las cadenas en una sola cadena, separadas por un 
espacio. """

lista = []

while True:
    texto = input("Introduce un texto: ")
    lista.append(texto)
    if input("¿Quieres agregar otro? (s/n): ").lower() == "n":
        break
    
print("Cadena concatenada:", " ".join(lista))