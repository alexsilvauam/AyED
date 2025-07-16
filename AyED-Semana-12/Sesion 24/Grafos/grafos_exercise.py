from collections import deque

class Grafo:
    def __init__(self, es_dirigido=False):
        self.adyacencia = {}
        self.es_dirigido = es_dirigido

    def agregar_vertice(self, vertice):
        if vertice not in self.adyacencia:
            self.adyacencia[vertice] = []

    def agregar_arista(self, u, v, peso=1):
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        self.adyacencia[u].append((v, peso))
        if not self.es_dirigido:
            self.adyacencia[v].append((u, peso))

    def obtener_vecinos(self, vertice):
        return [vecino for vecino, _ in self.adyacencia.get(vertice, [])]

    def existe_arista(self, u, v):
        return any(vecino == v for vecino, _ in self.adyacencia.get(u, []))

    def bfs(self, inicio):
        visitados = set()
        cola = deque([inicio])
        resultado = []
        while cola:
            actual = cola.popleft()
            if actual not in visitados:
                visitados.add(actual)
                resultado.append(actual)
                for vecino, _ in self.adyacencia.get(actual, []):
                    if vecino not in visitados:
                        cola.append(vecino)
        return resultado

    def dfs(self, inicio):
        visitados = set()
        resultado = []
        def dfs_recursivo(vertice):
            if vertice not in visitados:
                visitados.add(vertice)
                resultado.append(vertice)
                for vecino, _ in self.adyacencia.get(vertice, []):
                    dfs_recursivo(vecino)
        dfs_recursivo(inicio)
        return resultado

    def es_conexo(self):
        if not self.adyacencia:
            return True
        inicio = next(iter(self.adyacencia))
        return len(self.bfs(inicio)) == len(self.adyacencia)

    def encontrar_camino(self, inicio, fin):
        if inicio not in self.adyacencia or fin not in self.adyacencia:
            return []
        cola = deque([inicio])
        padres = {inicio: None}
        while cola:
            actual = cola.popleft()
            if actual == fin:
                break
            for vecino, _ in self.adyacencia.get(actual, []):
                if vecino not in padres:
                    padres[vecino] = actual
                    cola.append(vecino)
        if fin not in padres:
            return []
        camino = []
        while fin is not None:
            camino.append(fin)
            fin = padres[fin]
        camino.reverse()
        return camino

def menu():
    dirigido = input("¿Deseas un grafo dirigido? (s/n): ").lower() == 's'
    g = Grafo(es_dirigido=dirigido)

    while True:
        print("\n--- Menú ---")
        print("1. Agregar arista")
        print("2. Ver vecinos de un vértice")
        print("3. Verificar existencia de una arista")
        print("4. BFS desde un vértice")
        print("5. DFS desde un vértice")
        print("6. Verificar si el grafo es conexo")
        print("7. Encontrar camino entre dos vértices")
        print("8. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            u = input("Vértice origen: ")
            v = input("Vértice destino: ")
            peso = input("Peso (por defecto 1): ")
            peso = int(peso) if peso else 1
            g.agregar_arista(u, v, peso)
            print(f"Arista agregada de {u} a {v} con peso {peso}")
        elif opcion == "2":
            v = input("Vértice: ")
            vecinos = g.obtener_vecinos(v)
            print("Vecinos:", vecinos)
        elif opcion == "3":
            u = input("Vértice origen: ")
            v = input("Vértice destino: ")
            existe = g.existe_arista(u, v)
            print("Existe arista:", existe)
        elif opcion == "4":
            inicio = input("Vértice inicial: ")
            print("BFS:", g.bfs(inicio))
        elif opcion == "5":
            inicio = input("Vértice inicial: ")
            print("DFS:", g.dfs(inicio))
        elif opcion == "6":
            print("¿Es conexo?:", g.es_conexo())
        elif opcion == "7":
            inicio = input("Vértice de inicio: ")
            fin = input("Vértice de fin: ")
            print("Camino encontrado:", g.encontrar_camino(inicio, fin))
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()