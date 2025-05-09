""" Escribe un programa que recorra una lista de cadenas y cuente cuántas 
veces aparece un carácter específico en cada cadena. Al final, muestra el 
conteo para cada cadena."""

lista = []

while True:
    texto = input("Introduce un texto: ")
    lista.append(texto)
    if input("¿Quieres agregar otro? (s/n): ").lower() == "n":
        break

caracter = input("Introduce el carácter a contar: ")
lista = [cadena.count(caracter) for cadena in lista]
print("Lista: ", lista)