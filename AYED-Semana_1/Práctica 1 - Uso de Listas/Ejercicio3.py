"""Escribe un programa que recorra una lista de cadenas y convierta cada 
cadena a mayúsculas o minúsculas dependiendo de un criterio. Si la 
longitud de la cadena es par, se convertirá a mayúsculas; si es impar, a 
minúsculas."""
lista = []

while True:
    texto = input("Introduce un texto: ")
    lista.append(texto)
    if input("¿Quieres agregar otro? (s/n): ").lower() == "n":
        break

lista = [cadena.upper() if len(cadena) % 2 == 0 else cadena.lower() for cadena in lista]

print("Cadenas:", lista)