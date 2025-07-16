from model.clas import Cola

class ColaDAO:
    def __init__(self):
        self.cola = Cola()
        self.id =1
    
    def agregar(self, elemento):
        if self.existe(elemento):
            return False
        self.cola.agregar([self.id,elemento])
        self.id += 1
        return True
    
    def quitar(self):
        return self.cola.quitar()
    
    def vacia(self):
        return self.cola.vacia()
    
    def retornar(self):
        return list(self.cola.cola.queue)
    
    def existe(self, elemento):
        for i in self.cola.cola.queue:
            if i[1] == elemento:
                return True
        return False