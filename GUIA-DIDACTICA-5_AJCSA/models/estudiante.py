
class Estudiante:
    """Representa a un estudiante con sus datos."""
    def __init__(self, carnet, nombres, apellidos, peso, estatura, sexo, promedio):
        if not all([carnet, nombres, apellidos, sexo]):
             raise ValueError("Carnet, nombres, apellidos y sexo no pueden estar vacíos.")
        try:
            self.peso = float(peso)
            self.estatura = float(estatura)
            self.promedio = float(promedio)
            if self.peso <= 0 or self.estatura <= 0 or self.promedio < 0:
                 raise ValueError("Peso, estatura y promedio deben ser positivos.")
        except ValueError:
             raise ValueError("Peso, estatura y promedio deben ser números válidos.")

        self.carnet = str(carnet)
        self.nombres = str(nombres)
        self.apellidos = str(apellidos)
        self.sexo = str(sexo)

    def __str__(self):
        """Representación en string para mostrar el estudiante."""
        return (f"Carnet: {self.carnet}, Nombre: {self.nombres} {self.apellidos}, "
                f"Sexo: {self.sexo}, Peso: {self.peso:.2f} kg, "
                f"Estatura: {self.estatura:.2f} m, Promedio: {self.promedio:.2f}")

    def obtener_atributo(self, nombre_atributo):
        """Devuelve el valor de un atributo por su nombre."""
        mapa_atributos = {
            'carnet': self.carnet,
            'nombres': self.nombres.lower(), 
            'apellidos': self.apellidos.lower(), 
            'peso': self.peso,
            'estatura': self.estatura,
            'sexo': self.sexo.lower(),
            'promedio': self.promedio
        }
        atributo_limpio = nombre_atributo.lower().strip()
        if atributo_limpio in mapa_atributos:
            return mapa_atributos[atributo_limpio]
        else:
            raise AttributeError(f"El estudiante no tiene el atributo '{nombre_atributo}' para ordenar.")