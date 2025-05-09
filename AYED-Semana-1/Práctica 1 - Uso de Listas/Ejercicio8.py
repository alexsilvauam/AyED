""""Escribe un programa que recorra una lista de cadenas y las ordene 
alfabéticamente en orden ascendente.    """

lista = []

while True:
    texto = input("Introduce un texto: ")
    lista.append(texto)
    if input("¿Quieres agregar otro? (s/n): ").lower() == "n":
        break

print("La lista ordenada es: ", sorted(lista))