"""Escribe un programa que busque si una sub cadena está presente en cada 
una de las cadenas de una lista. El programa debe devolver una lista con 
valores booleanos que indiquen si la sub cadena fue encontrada en cada 
cadena. """
lista = []

while True:
    texto = input("Introduce un texto: ")
    lista.append(texto)
    if input("¿Quieres agregar otro? (s/n): ").lower() == "n":
        break

subcadena = input("Introduce la subcadena a buscar: ")
resultado = [subcadena in cadena for cadena in lista]
print("Resultado:", resultado)