# Almacenar un listado de estudiantes, calcular su promedio de n clases

# Clases básicas o módulos
class Asignatura:   
    def __init__(self, nombre, descripcion, credito):
        self.nombre = nombre
        self.descripcion = descripcion
        self.credito = credito
    
    def __str__(self):
        return f"""Asignatura: { '{' } "Nombre": "{self.nombre}", "descripcion": 
        "{self.descripcion}", "credito": "{self.credito}" {'}'},"""

# Crear una instancia de la clase y mostrarla
asig = Asignatura("Matematica", "Matematica Basica", 3)
print(asig)

class Estudiantes:
    def __init__(self, cif, nombre, apellido, carrera):
        self.cif = cif
        self.nombre = nombre
        self.apellido = apellido
        self.carrera = carrera

    def __str__(self):
        return f"""Estudiante: { '{' } "CIF": "{self.cif}", "Nombre": "{self.nombre}", 
        "Apellido": "{self.apellido}", "Carrera": "{self.carrera}" {'}'},"""
    
class Notas:
    def __init__(self, estudiante, asignatura, nota):
        self.estudiante = estudiante
        self.asignatura = asignatura
        self.nota = nota

    def __str__(self):
        return f"""Notas: { '{' } "Estudiante": "{self.estudiante}", "Asignatura": "{self.asignatura}", 
        "Nota": "{self.nota}" {'}'},"""
