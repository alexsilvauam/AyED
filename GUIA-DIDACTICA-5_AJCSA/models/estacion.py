
class Estacion:
    """Representa una estación en una ruta."""
    def __init__(self, nombre, tiempo_siguiente=0):
        """
        Inicializa una estación.
   .
        """
        if not nombre:
            raise ValueError("El nombre de la estación no puede estar vacío.")
        if tiempo_siguiente < 0:
             raise ValueError("El tiempo a la siguiente estación no puede ser negativo.")

        self.nombre = str(nombre)
        try:
            self.tiempo_siguiente = float(tiempo_siguiente)
        except ValueError:
            raise ValueError("El tiempo a la siguiente estación debe ser un número.")


    def __str__(self):
        if self.tiempo_siguiente > 0:
            return f"Estación: {self.nombre} (Tiempo hasta la siguiente: {self.tiempo_siguiente} min)"
        else:
            return f"Estación: {self.nombre} (Destino final)"

    def __eq__(self, other):
        if isinstance(other, Estacion):
            return self.nombre.lower() == other.nombre.lower()
        if isinstance(other, str):
             return self.nombre.lower() == other.lower()
        return False