class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

class ArbolBin:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self.insertar_recursivo(self.raiz, valor)

    def insertar_recursivo(self, node, valor):
        if node is None:
            return Nodo(valor)
        if valor < node.valor:
            node.left = self.insertar_recursivo(node.left, valor)
        else:
            node.right = self.insertar_recursivo(node.right, valor)
        return node
    
    def buscar(self, valor):
        return self.buscar_recursivo(self.raiz, valor)
    
    def buscar_recursivo(self, node, valor):
        if node is None:
            return False
        if node.valor == valor:
            return True
        elif valor < node.valor:
            return self.buscar_recursivo(node.left, valor)
        else:
            return self.buscar_recursivo(node.right, valor)
    
    def recorrido_inorden(self, node):
        if node is not None:
            self.recorrido_inorden(node.left)
            print(node.valor, end=' ')  
            self.recorrido_inorden(node.right)

tree = ArbolBin()
tree.insertar(5)
tree.insertar(3)
tree.insertar(7)
tree.insertar(2)
tree.insertar(4)
tree.insertar(6)
tree.insertar(8)

print("Recorrido inorden del árbol binario:")
print(tree.buscar(4))  # Buscar un valor
print(tree.buscar(10))  # Buscar un valor que no existe
tree.recorrido_inorden(tree.raiz)
