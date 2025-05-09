import models.clases as c

class MateriaDao():
    def __init__(self):
        self.materias = []

    def agregar_materia(self, materia):
        self.materias.append(materia)

    def obtener_materias(self):
        for materia in self.materias:
            print(materia.__str__())

