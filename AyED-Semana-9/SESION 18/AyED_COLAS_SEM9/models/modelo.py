class ColaPacientes:
    """
    Representa la cola de espera de pacientes y gestiona sus operaciones.
    Utiliza una lista de Python donde el final de la lista es el final de la cola
    y el principio de la lista (índice 0) es el frente de la cola.
    """
    def __init__(self):
        """Inicializa una cola de pacientes vacía."""
        self._pacientes = []  # Usamos _ para indicar que es un atributo "privado"

    def enqueue(self, paciente):
        """
        Agrega un nuevo paciente al final de la cola.

        Args:
            paciente (str): El nombre o identificador del paciente a agregar.
        """
        self._pacientes.append(paciente)

    def dequeue(self):
        """
        Elimina y devuelve el paciente al frente de la cola (el que llegó primero).

        Returns:
            str: El paciente que fue atendido.
            None: Si la cola está vacía.
        """
        if not self.is_empty():
            return self._pacientes.pop(0)
        return None

    def peek(self):
        """
        Devuelve el paciente al frente de la cola sin eliminarlo.

        Returns:
            str: El siguiente paciente a ser atendido.
            None: Si la cola está vacía.
        """
        if not self.is_empty():
            return self._pacientes[0]
        return None

    def is_empty(self):
        """
        Verifica si la cola de pacientes está vacía.

        Returns:
            bool: True si la cola está vacía, False en caso contrario.
        """
        return len(self._pacientes) == 0

    def obtener_cola_completa(self):
        """
        Devuelve una copia de la lista de pacientes actual (para visualización segura).
        """
        return self._pacientes[:]  # Devuelve una copia