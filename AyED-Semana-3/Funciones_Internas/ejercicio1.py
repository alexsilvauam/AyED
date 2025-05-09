from functools import reduce
#  Análisis de datos de ventas

"""Desarrollar un programa que procese un conjunto de registros de ventas (por ejemplo, listas de 
diccionarios) para extraer información relevante. Los estudiantes deberán aplicar funciones 
internas como map, filter y reduce para transformar y filtrar los datos, calculando totales y 
promedios. Este ejercicio busca que los estudiantes identifiquen y aprovechen las 
funcionalidades nativas de Python para la manipulación eficiente de estructuras de datos."""




def anadir_a_diccionario(diccionario, clave, valor):
    if clave not in diccionario:
        diccionario[clave] = [valor]
    else:
        diccionario[clave].append(valor)
    
    clave = input("Ingrese la clave: ")
    valor = input("Ingrese el valor: ")
    diccionario[clave] = valor
    return diccionario

def calcular_totales(diccionario):
    totales = {}
    for clave, valores in diccionario.items():
        totales[clave] = sum(valores)
    return totales

def calcular_promedios(diccionario):
    promedios = {}
    for clave, valores in diccionario.items():
        promedios[clave] = sum(valores) / len(valores) if valores else 0
    return promedios

def filtrar_ventas(diccionario, umbral):
    filtradas = {}
    for clave, valores in diccionario.items():
        filtradas[clave] = list(filter(lambda x: x > umbral, valores))
    return filtradas

def main():
    ventas = {
        'producto1': [100, 200, 300],
        'producto2': [150, 250, 350],
        'producto3': [200, 300, 400]
    }

    # Añadir un nuevo producto
    clave = input("Ingrese la clave del nuevo producto: ")
    valor = int(input("Ingrese el valor de la venta: "))
    anadir_a_diccionario(ventas, clave, valor)

    # Calcular totales
    totales = calcular_totales(ventas)
    print("Totales:", totales)

    # Calcular promedios
    promedios = calcular_promedios(ventas)
    print("Promedios:", promedios)

    # Filtrar ventas por umbral
    umbral = int(input("Ingrese el umbral para filtrar ventas: "))
    filtradas = filtrar_ventas(ventas, umbral)
    print("Ventas filtradas:", filtradas)
    
