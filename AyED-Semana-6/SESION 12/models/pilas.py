class Pila:
     def __init__(self):
         """   Constructor de la clase Pila
         """
         self.items = []

     def estaVacia(self):
         """"comprueba si la pila está vacía. No requiere parámetros y devuelve un valor booleano."""
         return self.items == []

     def incluir(self, item):
         """ agrega un nuevo ítem en el tope de la pila. Requiere el ítem y no devuelve valor."""
         self.items.append(item)

     def extraer(self):
         """elimina el ítem en el tope de la pila. No requiere parámetros y devuelve el ítem. La pila se modifica."""
         return self.items.pop()

     def inspeccionar(self):
         """devuelve el ítem en el tope de la pila pero no lo elimina. No requiere parámetros. La pila no se modifica."""
         return self.items[len(self.items)-1]

     def tamano(self):
         """devuelve el número de ítems en la pila. No requiere parámetros y devuelve un entero."""
         return len(self.items)