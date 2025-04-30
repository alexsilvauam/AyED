
from .estructuras import ListaDoblementeEnlazada, NodoDoble

class GestionHistorial:
    """Gestiona el historial de acciones usando una lista doblemente enlazada."""

    def __init__(self):
        """Inicializa el historial con un estado base."""
        self._historial = ListaDoblementeEnlazada()
        self._estado_inicial = "--- Documento Inicial ---"
        nodo_inicial = NodoDoble(self._estado_inicial)
        self._historial.cabeza = nodo_inicial
        self._historial.cola = nodo_inicial
        self._historial.tamano = 1
        self._cursor = nodo_inicial 

    def realizar_accion(self, accion_str):
        """
        Registra una nueva acción, invalidando el historial 'redo' si existe.
        Args:
            accion_str (str): Descripción de la acción realizada.
        """
        if not accion_str:
            return 

        nuevo_nodo = NodoDoble(accion_str)

       
        if self._cursor != self._historial.cola:
            self._historial.cola = self._cursor
            self._cursor.siguiente = None 

        nuevo_nodo.anterior = self._cursor
        self._cursor.siguiente = nuevo_nodo
        self._historial.cola = nuevo_nodo 
        self._cursor = nuevo_nodo
        self._historial.tamano += 1 


    def deshacer(self):
        """
        Mueve el cursor al estado anterior 
        
        """
        if self._cursor and self._cursor.anterior:
             self._cursor = self._cursor.anterior
             return self._cursor.dato
        return None 

    def rehacer(self):
        """
        Mueve el cursor al estado siguiente 
      
        """
        if self._cursor and self._cursor.siguiente:
             self._cursor = self._cursor.siguiente
             return self._cursor.dato
        return None 

    def obtener_estado_actual(self):
        """Devuelve el estado/acción en la posición actual del cursor."""
        return self._cursor.dato if self._cursor else "Historial vacío"

    def puede_deshacer(self):
        """Verifica si la operación Deshacer está disponible."""
        return self._cursor is not None and self._cursor.anterior is not None

    def puede_rehacer(self):
        """Verifica si la operación Rehacer está disponible."""
        return self._cursor is not None and self._cursor.siguiente is not None

    def obtener_historial_completo(self):
        """Devuelve una lista de Python con todas las acciones en el historial."""
        return list(self._historial)

    def obtener_posicion_cursor(self):
         """Devuelve el índice (basado en 0) del cursor en la lista completa."""
         if not self._cursor:
             return -1
         nodos_historial = self._historial.obtener_nodos()
         try:
             return nodos_historial.index(self._cursor)
         except ValueError:
             return -1 