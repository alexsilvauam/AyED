"""Escribe un programa que recorra una lista de cadenas y calcule la longitud 
de cada cadena, almacenando el resultado en una nueva lista."""

lista = []
longitudes = []

while True:
    texto = input("Introduce un texto: ")
    lista.append(texto)
    if input("¿Quieres agregar otro? (s/n): ").lower() == "n":
        break

for cadena in lista:
    longitudes.append(len(cadena))

print("Longitudes de las cadenas:", longitudes)
print("Cadenas:", lista)