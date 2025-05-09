"""" Escribe un programa que recorra una lista de cadenas y divida cada cadena 
en subcadenas utilizando un delimitador específico (por ejemplo, una coma 
o un espacio). """

lista = []

while True:
    texto = input("Introduce un texto: ")
    lista.append(texto)
    if input("¿Quieres agregar otro? (s/n): ").lower() == "n":
        break

def delim_cadenas(lista, delim):
    return [cadena.split(delim) for cadena in lista]

delim = input("Introduce el delimitador: ")
lista = delim_cadenas(lista, delim)
print("Lista: ", lista)
