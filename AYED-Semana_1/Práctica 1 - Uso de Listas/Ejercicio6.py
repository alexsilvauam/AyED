""""Escribe un programa que recorra una lista de cadenas y elimine los 
espacios en blanco al principio y al final de cada cadena"""

lista = []

while True:
    texto = input("Introduce un texto: ")
    lista.append(texto)
    if input("¿Quieres agregar otro? (s/n): ").lower() == "n":
        break

def elim_esp(lista):
    for i in range(len(lista)):
        lista[i] = lista[i].strip()
    return lista
lista = elim_esp(lista)
print("Lista: ", lista)
