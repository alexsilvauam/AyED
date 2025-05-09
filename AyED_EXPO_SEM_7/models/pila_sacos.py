class PilaSacos:
    def __init__(self):
        self.sacos = []

    def apilar(self, saco):
        self.sacos.append(saco)

    def desapilar(self):
        if not self.esta_vacia():
            return self.sacos.pop()
        else:
            return None

    def ver_tope(self):
        if not self.esta_vacia():
            return self.sacos[-1]
        else:
            return None

    def esta_vacia(self):
        return len(self.sacos) == 0