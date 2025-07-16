from models.modelo import ColaPacientes

class Controlador:
    def __init__(self):
        self._modelo = ColaPacientes()

    def agregar_paciente(self, nombre):
        if nombre:
            self._modelo.enqueue(nombre)
            return f"Paciente '{nombre}' agregado a la cola."
        return "El nombre del paciente no puede estar vacío."

    def atender_paciente(self):
        paciente_atendido = self._modelo.dequeue()
        if paciente_atendido:
            return f"Atendiendo al paciente: {paciente_atendido}"
        return "La cola está vacía, no hay pacientes para atender."

    def siguiente_paciente(self):
        siguiente = self._modelo.peek()
        if siguiente:
            return f"El próximo paciente en la cola es: {siguiente}"
        return "No hay pacientes esperando en la cola."

    def obtener_cola_actual(self):
        return self._modelo.obtener_cola_completa()