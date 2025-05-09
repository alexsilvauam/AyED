""" Escribe un programa que recorra una lista de cadenas y elimine aquellas 
que estén vacías. Imprime la lista resultante. """

lista = []

while True:
    texto = input("Introduce un texto: ")
    lista.append(texto)
    if input("¿Quieres agregar otro? (s/n): ").lower() == "n":
        break

print("Lista original: ", lista)
lista = [cadena for cadena in lista if cadena.strip() != '']
print("Lista: ", lista)