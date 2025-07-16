
# Constructor de nodo
class Nodo:
    def __init__(self, valor):
        self.dato = valor
        self.izq = None
        self.der = None 

class Arbol:
    def __init__(self): #Constructor del árbol
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.dato:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izq, valor)
        elif valor > nodo.dato:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.der, valor)

arbol = Arbol()
arbol.insertar(10)
arbol.insertar(3)
arbol.insertar(7)

def imprimir_arbol(nodo, nivel=0):
    if nodo is not None:
        imprimir_arbol(nodo.der, nivel + 1)
        print(' ' * 4 * nivel + '->', nodo.dato)
        imprimir_arbol(nodo.izq, nivel + 1)

print ("Árbol binario:")
imprimir_arbol(arbol.raiz)