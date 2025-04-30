
class Paciente:
    """Representa a un paciente en la cola de la clínica."""
    def __init__(self, nombre_completo, edad, sintoma, prioridad):
        if not nombre_completo or not sintoma:
             raise ValueError("Nombre completo y síntoma son requeridos.")
        try:
            self.edad = int(edad)
            self.prioridad = int(prioridad)
            if not (1 <= self.prioridad <= 5):
                 raise ValueError("La prioridad debe estar entre 1 y 5.")
            if self.edad < 0:
                 raise ValueError("La edad no puede ser negativa.")
        except ValueError:
             raise ValueError("Edad y prioridad deben ser números enteros.")

        self.nombre_completo = str(nombre_completo)
        self.sintoma = str(sintoma)

    def __str__(self):
        
        return (f"Paciente: {self.nombre_completo}, Edad: {self.edad}, "
                f"Síntoma: {self.sintoma}, Prioridad registrada: {self.prioridad}")