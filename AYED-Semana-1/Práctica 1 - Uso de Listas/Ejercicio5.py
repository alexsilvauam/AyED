""""Escribe un programa que recorra una lista de cadenas y reemplace todas 
las apariciones de un carácter específico con otro carácter, luego imprime la 
lista modificada. """

lista = []

while True:
    texto = input("Introduce un texto: ")
    lista.append(texto)
    if input("¿Quieres agregar otro? (s/n): ").lower() == "n":
        break


car_rempla = input("Introduce el carácter a reemplazar: ")
car_nuevo = input("Introduce el nuevo carácter: ")
for i in range(len(lista)):
    lista[i] = lista[i].replace(car_rempla, car_nuevo)  
print("Lista modificada:", lista)