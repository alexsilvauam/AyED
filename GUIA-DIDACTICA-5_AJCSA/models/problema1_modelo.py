
from .estructuras import ListaEnlazada
from .estudiante import Estudiante 
class GestionEstudiantes:
    """Gestiona la lista enlazada de estudiantes y sus operaciones."""

    CAMPOS_ORDENABLES = ['carnet', 'nombres', 'apellidos', 'peso', 'estatura', 'sexo', 'promedio']

    def __init__(self):
        """Inicializa la lista enlazada de estudiantes."""
        self._lista_estudiantes = ListaEnlazada() 

    def agregar_estudiante(self, carnet, nombres, apellidos, peso, estatura, sexo, promedio):
        """Crea un objeto Estudiante y lo agrega a la lista."""
        try:
            nuevo_estudiante = Estudiante(carnet, nombres, apellidos, peso, estatura, sexo, promedio)
            self._lista_estudiantes.insertar_al_final(nuevo_estudiante)
            return True, "Estudiante agregado correctamente."
        except ValueError as e:
            return False, f"Error al crear estudiante: {e}"
        except Exception as e:
            return False, f"Error inesperado al agregar estudiante: {e}"

    def obtener_estudiantes(self):
        """Devuelve una lista Python con todos los objetos Estudiante."""
        return list(self._lista_estudiantes)

    def ordenar_estudiantes_por(self, atributo):
        """
        Ordena la lista de estudiantes según el atributo especificado.
        Retorna True si se pudo ordenar, False si el atributo no es válido.
        """
        atributo_limpio = atributo.lower().strip()

        if atributo_limpio not in self.CAMPOS_ORDENABLES:
            return False, f"Error: No se puede ordenar por el atributo '{atributo}'. Válidos: {', '.join(self.CAMPOS_ORDENABLES)}"

        if self._lista_estudiantes.esta_vacia():
            return True, "La lista está vacía, no hay nada que ordenar."

        estudiantes_actuales = self.obtener_estudiantes()

        try:
            estudiantes_ordenados = sorted(
                estudiantes_actuales,
                key=lambda est: est.obtener_atributo(atributo_limpio)
                
            )
        except AttributeError as e:
             return False, f"Error interno al obtener atributo para ordenar: {e}"
        except Exception as e:
             return False, f"Error inesperado durante la ordenación: {e}"


        nueva_lista_ordenada = ListaEnlazada()
        for est in estudiantes_ordenados:
            nueva_lista_ordenada.insertar_al_final(est)

        self._lista_estudiantes = nueva_lista_ordenada
        return True, f"Lista de estudiantes ordenada por '{atributo_limpio}'."

    def __str__(self):
        """Representación textual de la gestión (muestra la lista)."""
        if self._lista_estudiantes.esta_vacia():
            return "No hay estudiantes registrados."
        return str(self._lista_estudiantes)