import collections

class Grafo:
    def __init__(self, es_dirigido=False):
        self.grafo = {}
        self.es_dirigido = es_dirigido

    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = set()
            print(f"Vértice {vertice} agregado al grafo.")
        else:
            print(f"El vértice {vertice} ya existe en el grafo.")
        
    def agregar_arista(self, u, v, peso=1):
        self.agregar_vertice(u)
        self.agregar_vertice(v)

        self.grafo[u].add(v)
        print(f"Arista de {u} a {v} agregada con peso {peso}.")

        if not self.es_dirigido:
            self.grafo[v].add(u)
            print(f"Arista de {v} a {u} agregada con peso {peso} (grafo no dirigido).")

    def obtener_vecinos(self, vertice):
        if vertice in self.grafo:
            return list(self.grafo[vertice])
        return []

    def existe_arista(self, u, v):
        if u in self.grafo and v in self.grafo[u]:
            return True
        return False
    
    def bfs(self, inicio):
        visitados = set()
        cola = collections.deque()
        recorrido = []

        cola.append(inicio)
        visitados.add(inicio)

        while cola:
            vertice_actual = cola.popleft()
            recorrido.append(vertice_actual)
            for vecino in self.grafo[vertice_actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)

        return recorrido
    
    def dfs(self, inicio):
        visitados = set()
        recorrido = []

        def dfs_recursivo(vertice):
            visitados.add(vertice)
            recorrido.append(vertice)
            print(f"Visitando {vertice} en DFS.")
            for vecino in self.grafo[vertice]:
                if vecino not in visitados:
                    dfs_recursivo(vecino)

        dfs_recursivo(inicio)
        return recorrido
    
    def imprimir_grafo(self):
        print("Grafo:")
        for vertice, vecinos in self.grafo.items():
            print(f"{vertice}: {', '.join(vecinos)}")
        print("Fin del grafo.")

    def es_conexo(self):
        if not self.grafo:
            return True
        primer_vertice = next(iter(self.grafo))
        recorrido_bfs = self.bfs(primer_vertice)
        return len(recorrido_bfs) == len(self.grafo)

    def encontrar_camino(self, inicio, fin):
        if inicio not in self.grafo or fin not in self.grafo:
            print(f"Error: '{inicio}' o '{fin}' no están en el grafo.")
            return []
        
        cola = collections.deque()
        visitados = set()
        padres = {}

        cola.append(inicio)
        visitados.add(inicio)
        padres[inicio] = None

        while cola:
            vertice_actual = cola.popleft()
            if vertice_actual == fin:
                camino = []
                temp = fin
                while temp is not None:
                    camino.append(temp)
                    temp = padres[temp]
                return camino[::-1]
            for vecino in self.grafo[vertice_actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    padres[vecino] = vertice_actual
                    cola.append(vecino)
        print(f"No se encontró un camino de {inicio} a {fin}.")
        return []

# EJEMPLO DE EJECUCIÓN
if __name__ == "__main__":
    print("Ejemplo de ejecución:")
    mi_grafo = Grafo(es_dirigido=False)

    mi_grafo.agregar_arista("Managua", "Masaya")
    mi_grafo.agregar_arista("Managua", "Leon")
    mi_grafo.agregar_arista("Masaya", "Granada")
    mi_grafo.agregar_arista("Granada", "Rivas")
    mi_grafo.agregar_arista("Managua", "Granada")

    mi_grafo.imprimir_grafo()

    print("\n-Operaciones Basicas-")
    print(f"Vecinos de Managua: {mi_grafo.obtener_vecinos('Managua')}")
    print(f"Existe arista entre Managua y Masaya? {mi_grafo.existe_arista('Managua', 'Masaya')}")
    print(f"Existe arista entre Managua y Rivas? {mi_grafo.existe_arista('Managua', 'Rivas')}")

    print("\n-Recorridos-")
    print(f"Recorrido BFS desde Managua: {mi_grafo.bfs('Managua')}")
    print(f"Recorrido DFS desde Managua: {mi_grafo.dfs('Managua')}")

    print("\n- Conectividad y Caminos-")
    print(f"Es el grafo conexo? {mi_grafo.es_conexo()}")

    camino = mi_grafo.encontrar_camino("Managua", "Rivas")
    print(f"Camino de Managua a Rivas: {camino} ")

    camino_inexistente = mi_grafo.encontrar_camino("Managua", "Juigalpa")
    print(f"Camino de Managua a Juigalpa: {camino_inexistente} ")

    print("Creando un grafo dirigido...")
    grafo_dirigido = Grafo(es_dirigido=True)
    grafo_dirigido.agregar_arista("Inicio", "A")
    grafo_dirigido.agregar_arista("A", "B")
    grafo_dirigido.agregar_arista("B", "C")
    grafo_dirigido.agregar_arista("C", "Fin")
    grafo_dirigido.agregar_arista("Inicio", "D")

    grafo_dirigido.imprimir_grafo()

    print(f"Vecinos de Inicio: {grafo_dirigido.obtener_vecinos('Inicio')}")
    print(f"Vecinos de Fin: {grafo_dirigido.obtener_vecinos('Fin')}")
    print(f"Existe arista entre A y B? {grafo_dirigido.existe_arista('A', 'B')}")
    print(f"Existe arista entre B y A? {grafo_dirigido.existe_arista('B', 'A')}")

    print ("\n-Recorridos en grafo dirigido-")
    print(f"Recorrido BFS desde Inicio: {grafo_dirigido.bfs('Inicio')}")
    print(f"Recorrido DFS desde Inicio: {grafo_dirigido.dfs('Inicio')}")

    print("\n- Conectividad y Caminos en grafo dirigido-")
    camino_dirigido = grafo_dirigido.encontrar_camino("Inicio", "Fin")
    print(f"Camino de Inicio a Fin: {camino_dirigido} ")

    camino_dirigido_inexistente = grafo_dirigido.encontrar_camino("Inicio", "C")
    print(f"Camino de Inicio a C: {camino_dirigido_inexistente} ")