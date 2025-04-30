
from .estructuras import ListaEnlazada
from .estacion import Estacion

class GestionRutas:
    """Gestiona la lista enlazada de estaciones y calcula tiempos."""

    def __init__(self):
        """Inicializa la ruta (lista enlazada de estaciones)."""
        self._ruta = ListaEnlazada()

    def agregar_estacion(self, nombre, tiempo_siguiente):
        """Agrega una nueva estación al FINAL de la ruta."""
        for est in self._ruta:
            if est.nombre.lower() == nombre.lower():
                 return False, f"Error: Ya existe una estación llamada '{nombre}'."
        try:
          
            if not self._ruta.esta_vacia():
                if self._ruta.cola.dato.tiempo_siguiente <= 0:
                     return False, "Error: No se puede agregar después del destino final. Modifique el tiempo de la última estación primero."
                

            nueva_estacion = Estacion(nombre, tiempo_siguiente)
            self._ruta.insertar_al_final(nueva_estacion)
            return True, f"Estación '{nombre}' agregada a la ruta."
        except ValueError as e:
            return False, f"Error al crear estación: {e}"
        except Exception as e:
             return False, f"Error inesperado al agregar estación: {e}"

    def obtener_ruta(self):
        """Devuelve una lista Python con todas las estaciones en orden."""
        return list(self._ruta) 
    def calcular_tiempo_ruta(self, nombre_origen, nombre_destino):
        """
        Calcula el tiempo estimado entre dos estaciones de la ruta.
        """
        if self._ruta.esta_vacia():
            return False, "La ruta está vacía."
        if nombre_origen.lower() == nombre_destino.lower():
             return True, 0.0 

        nodo_actual = self._ruta.cabeza
        tiempo_total = 0.0
        encontrado_origen = False

        while nodo_actual:
            estacion_actual = nodo_actual.dato

            if not encontrado_origen and estacion_actual.nombre.lower() == nombre_origen.lower():
                encontrado_origen = True
                if nodo_actual == self._ruta.cola:
                     return False, f"La estación de origen '{nombre_origen}' es el destino final de la ruta."


            if encontrado_origen:
                if estacion_actual.nombre.lower() == nombre_destino.lower():
                    return True, tiempo_total

                
                if nodo_actual.siguiente:
                    tiempo_a_sumar = estacion_actual.tiempo_siguiente
                    if tiempo_a_sumar <= 0 and nodo_actual.siguiente.dato.nombre.lower() != nombre_destino.lower():
                        return False, f"La ruta se interrumpe o termina en '{estacion_actual.nombre}' antes de llegar a '{nombre_destino}'."

                    tiempo_total += tiempo_a_sumar
                else:
                    return False, f"La estación de destino '{nombre_destino}' no se encontró en la ruta después de '{nombre_origen}'."

            nodo_actual = nodo_actual.siguiente

        if not encontrado_origen:
            return False, f"La estación de origen '{nombre_origen}' no se encontró en la ruta."

        return False, "Error inesperado en el cálculo de la ruta."


    def __str__(self):
        """Representación textual de la ruta."""
        if self._ruta.esta_vacia():
            return "Ruta Vacía"
        return " -> ".join(str(estacion.nombre) for estacion in self._ruta)