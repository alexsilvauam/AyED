import matplotlib.pyplot as plt

class Nodo:  
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:

    def __init__(self, raiz):  # Constructor de la clase ArbolBinario
        self.raiz = raiz  # Inicialización de la raíz del árbol
        self.valores_x = []  # Lista para almacenar las coordenadas x de los nodos
        self.valores_y = []  # Lista para almacenar las coordenadas y de los nodos
        self.etiquetas = {}  # Diccionario para almacenar las etiquetas de los nodos


    def insertar(self, valor):  # Método para insertar un nuevo nodo en el árbol

        if self.raiz is None:  # Si el árbol está vacío, el nuevo nodo se convierte en la raíz
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)  # Llama al método de inserción recursivo


    def _insertar_recursivo(self, valor, nodo_actual):  # Método de inserción recursivo
        if valor < nodo_actual.valor:  # Si el valor es menor que el valor del nodo actual
            if nodo_actual.izquierda is None:  # Si no hay un nodo a la izquierda, se inserta aquí
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.izquierda)  # Insertar recursivamente hacia la izquierda
        elif valor > nodo_actual.valor:  # Si el valor es mayor que el valor del nodo actual
            if nodo_actual.derecha is None:  # Si no hay un nodo a la derecha, se inserta aquí
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.derecha)  # Insertar recursivamente hacia la derecha
        else:
            # Valor ya existe, se puede manejar según el caso
            pass

    def _generar_coordenadas(self, nodo, nivel, pos):  # Método para generar las coordenadas de los nodos
        if nodo is not None:
            self.valores_x.append(pos)  # Agregar la coordenada x del nodo a la lista
            self.valores_y.append(nivel)  # Agregar la coordenada y del nodo a la lista
            self.etiquetas[(pos, nivel)] = nodo.valor  # Agregar la etiqueta del nodo al diccionario
            self._generar_coordenadas(nodo.izquierda, nivel-1, pos-2)  # Generar coordenadas para el subárbol izquierdo
            self._generar_coordenadas(nodo.derecha, nivel-1, pos+2)  # Generar coordenadas para el subárbol derecho


    def _dibujar_conexiones(self, nodo, nivel, pos):  # Método para dibujar las conexiones entre los nodos
        if nodo is not None:
            if nodo.izquierda is not None:  # Si hay un nodo hijo izquierdo
                plt.plot([pos, pos-2], [nivel, nivel-1], color='black')  # Dibujar una línea de conexión hacia él
                self._dibujar_conexiones(nodo.izquierda, nivel-1, pos-2)  # Dibujar conexiones recursivamente

            if nodo.derecha is not None:  # Si hay un nodo hijo derecho
                plt.plot([pos, pos+2], [nivel, nivel-1], color='black')  # Dibujar una línea de conexión hacia él
                self._dibujar_conexiones(nodo.derecha, nivel-1, pos+2)  # Dibujar conexiones recursivamente


    def mostrar_graficamente(self):  # Método para mostrar el árbol gráficamente
        self._generar_coordenadas(self.raiz, 0, 0)  # Generar las coordenadas de los nodos
        for (x, y), etiqueta in self.etiquetas.items():  # Iterar sobre las etiquetas del diccionario
            plt.text(x, y, str(etiqueta), fontsize=12, ha='center')  # Mostrar la etiqueta de cada nodo

        self._dibujar_conexiones(self.raiz, 0, 0)  # Dibujar las conexiones entre los nodos
        plt.scatter(self.valores_x, self.valores_y, c='blue', s=300, alpha=0.5)  # Graficar los nodos como puntos
        plt.axis('off')  # Desactivar los ejes
        plt.show()  # Mostrar el gráfico

# Ejemplo de uso

arbol = ArbolBinario(None)  # Crear un árbol binario vacío
valores = [5, 3, 7, 2, 4, 6, 8]  # Valores a insertar en el árbol

for v in valores:
    arbol.insertar(v)  # Insertar valores en el árbol

arbol.mostrar_graficamente()  # Mostrar el árbol gráficamente