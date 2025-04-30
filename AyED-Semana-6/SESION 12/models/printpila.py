from pilas import Pila

p=Pila()

print("Comprueba si esta vacia: ", p.estaVacia())
p.incluir(4)
p.incluir('perro')
print("Devuelve el tope: ", p.inspeccionar())
p.incluir(True)
print("Devuelve el tamanio: ", p.tamano())
print("Comprueba si esta vacia: ", p.estaVacia())
p.incluir(8.4)
print("Imprime y extra el ultimo termino: ", p.extraer())
print("Imprime y extra el ultimo termino: ",p.extraer())
print("Devuelve el tamanio: ",p.tamano())
