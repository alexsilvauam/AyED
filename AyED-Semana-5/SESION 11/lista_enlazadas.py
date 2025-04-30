class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
    
    def mostrar(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.valor, end=" -> ")
            nodo_actual = nodo_actual.siguiente
        print("None")
    
    def buscar(self, valor):
        nodo_actual = self.cabeza
        while nodo_actual:
            if nodo_actual.valor == valor:
                return True
            nodo_actual = nodo_actual.siguiente
        return False
    
    def eliminar(self, valor):
        if not self.cabeza:
            return False
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            return True
        nodo_actual = self.cabeza
        while nodo_actual.siguiente:
            if nodo_actual.siguiente.valor == valor:
                nodo_actual.siguiente = nodo_actual.siguiente.siguiente
                return True
            nodo_actual = nodo_actual.siguiente
        return False
    

if __name__ == "__main__":
    lista = ListaEnlazada()
    lista.agregar(1)
    lista.agregar(2)
    lista.agregar(3)
    lista.mostrar()  # Salida: 1 -> 2 -> 3 -> None
    print(lista.buscar(2))  # Salida: True