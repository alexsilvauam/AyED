import models.clases as c
import controllers.dao_controller as dao
import os

os.system('cls' if os.name == 'nt' else 'clear')

materia = c.Materia("Calculo", "MAT101", 4)
dao = dao.MateriaDao()
dao.agregar_materia(materia)
dao.obtener_materias()
