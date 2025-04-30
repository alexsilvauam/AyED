
from .estructuras import ListaEnlazada
from .paciente import Paciente

class GestionClinica:
    """Gestiona la cola de pacientes (FIFO - First-In, First-Out)."""

    def __init__(self):
        """Inicializa la cola (lista enlazada)."""
        self._cola_pacientes = ListaEnlazada()

    def ingresar_paciente(self, nombre_completo, edad, sintoma, prioridad):
        """Crea un paciente y lo agrega al final de la cola."""
        try:
            nuevo_paciente = Paciente(nombre_completo, edad, sintoma, prioridad)
            self._cola_pacientes.insertar_al_final(nuevo_paciente)
            return True, f"Paciente '{nombre_completo}' ingresado a la cola."
        except ValueError as e:
            return False, f"Error al crear paciente: {e}"
        except Exception as e:
            return False, f"Error inesperado al ingresar paciente: {e}"

    def atender_siguiente_paciente(self):
        """
        Elimina y devuelve al paciente al inicio de la cola (el que llegó primero).
        """
        paciente_atendido = self._cola_pacientes.eliminar_al_inicio()
        return paciente_atendido 
    def ver_proximo_paciente(self):
        """
        Devuelve el paciente al inicio de la cola sin eliminarlo.
        :
        """
        if self._cola_pacientes.esta_vacia():
            return None
        return self._cola_pacientes.cabeza.dato 
    def obtener_cola_pacientes(self):
        """Devuelve una lista Python con los pacientes en orden de llegada."""
        return list(self._cola_pacientes)

    def __str__(self):
        """Representación textual de la cola."""
        if self._cola_pacientes.esta_vacia():
            return "Cola de pacientes vacía."
        return " -> ".join(str(p.nombre_completo) for p in self._cola_pacientes)