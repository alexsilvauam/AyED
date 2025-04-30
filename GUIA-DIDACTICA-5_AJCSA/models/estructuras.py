class Nodo:
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

    def __str__(self):
       
        return str(self.dato)

class NodoDoble(Nodo):
    """Representa un nodo para una lista doblemente enlazada."""
    def __init__(self, dato=None, siguiente=None, anterior=None):
        super().__init__(dato, siguiente)
        self.anterior = anterior

class ListaEnlazada:
    """Representa una lista enlazada simple."""
    def __init__(self):
        self.cabeza = None
        self.cola = None 
        self.tamano = 0

    def esta_vacia(self):
        """Verifica si la lista está vacía."""
        return self.cabeza is None

    def insertar_al_inicio(self, dato):
        """Inserta un dato al inicio de la lista."""
        nuevo_nodo = Nodo(dato, self.cabeza)
        self.cabeza = nuevo_nodo
        if self.cola is None: 
            self.cola = nuevo_nodo
        self.tamano += 1

    def insertar_al_final(self, dato):
        """Inserta un dato al final de la lista."""
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamano += 1

    def eliminar_al_inicio(self):
        """Elimina y devuelve el dato al inicio de la lista."""
        if self.esta_vacia():
         
            return None 

        dato_eliminado = self.cabeza.dato
        nodo_a_eliminar = self.cabeza

        if self.cabeza == self.cola: 
            self.cabeza = None
            self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente

        del nodo_a_eliminar 
        self.tamano -= 1
        return dato_eliminado

    def obtener_nodos(self):
        """Devuelve una lista de Python con todos los nodos."""
        nodos = []
        actual = self.cabeza
        while actual:
            nodos.append(actual)
            actual = actual.siguiente
        return nodos

    def obtener_datos(self):
        """Devuelve una lista de Python con todos los datos."""
        datos = []
        actual = self.cabeza
        while actual:
            datos.append(actual.dato)
            actual = actual.siguiente
        return datos

    def __iter__(self):
        """Permite iterar sobre los datos de la lista (ej: for dato in lista:)"""
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente

    def __len__(self):
        """Devuelve el tamaño de la lista."""
        return self.tamano

    def __str__(self):
        """Representación en string de la lista (útil para debugging rápido)."""
        nodos_str = []
        actual = self.cabeza
        while actual:
            nodos_str.append(str(actual.dato))
            actual = actual.siguiente
        return " -> ".join(nodos_str) if nodos_str else "Lista Vacía"

class ListaDoblementeEnlazada(ListaEnlazada):
    """Representa una lista doblemente enlazada."""
   
    def __init__(self):
        super().__init__()
    
    
    def insertar_al_inicio(self, dato):
        nuevo_nodo = NodoDoble(dato, self.cabeza, None)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamano += 1

    def insertar_al_final(self, dato):
        nuevo_nodo = NodoDoble(dato, None, self.cola)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamano += 1

    def eliminar_al_inicio(self):
        if self.esta_vacia():
            return None

        dato_eliminado = self.cabeza.dato
        nodo_a_eliminar = self.cabeza

        if self.cabeza == self.cola: 
            self.cabeza = None
            self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None 
        del nodo_a_eliminar
        self.tamano -= 1
        return dato_eliminado
        
    def eliminar_al_final(self):
        """Elimina y devuelve el dato al final de la lista."""
        if self.esta_vacia():
            return None
        
        dato_eliminado = self.cola.dato
        nodo_a_eliminar = self.cola

        if self.cabeza == self.cola: 
             self.cabeza = None
             self.cola = None
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = None 

        del nodo_a_eliminar
        self.tamano -= 1
        return dato_eliminado

