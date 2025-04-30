import time
import sys #

class Tarea:
    def __init__(self, nombre: str, descripcion: str, prioridad: str):
        self.nombre = nombre
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.timestamp_creacion = time.time()

    def __str__(self) -> str:
        return (f"--- Tarea ---\n"
                f"Nombre: {self.nombre}\n"
                f"Descripción: {self.descripcion}\n"
                f"Prioridad: {self.prioridad}\n"
                f"Creada: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.timestamp_creacion))}")

class PilaTareas:

    def __init__(self):
        self._tareas = []

    def push(self, tarea: Tarea):
        if isinstance(tarea, Tarea):
            self._tareas.append(tarea)
        else:
            print("Solo se pueden agregar objetos de tipo Tarea.")

    def pop(self) -> Tarea | None:
        if not self.esta_vacia():
            return self._tareas.pop()
        else:
            return None

    def peek(self) -> Tarea | None:
        if not self.esta_vacia():
            return self._tareas[-1]
        else:
            return None

    def esta_vacia(self) -> bool:
        return len(self._tareas) == 0

    def __len__(self) -> int:
        return len(self._tareas)

    def mostrar_todas(self):
        if self.esta_vacia():
            print("\n>> La pila de tareas está vacía.")
            return

        print("\n Tareas Actuales en la Pila (Más reciente arriba):")
        for i in range(len(self._tareas) - 1, -1, -1):
            tarea = self._tareas[i]
            print(f"\nPosición {len(self._tareas) - 1 - i} (desde la cima) ")
            print(tarea)
        print("Fin de la Lista de Tareas.\n")

def mostrar_menu():
    print("1. Agregar nueva tarea")
    print("2. Procesar última tarea agregada (Pop)")
    print("3. Ver última tarea agregada (Peek)")
    print("4. Mostrar todas las tareas")
    print("5. Ver número de tareas pendientes")
    print("0. Salir")

def main():
    pila_de_tareas = PilaTareas()
    print("Gestor de Tareas Pendientes")

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            print("\nAgregar Nueva Tarea")
            nombre = input("Nombre de la tarea: ")
            descripcion = input("Descripción: ")
            prioridad = input("Prioridad (ej. Alta, Media, Baja): ")
            if nombre: 
                 nueva_tarea = Tarea(nombre, descripcion, prioridad)
                 pila_de_tareas.push(nueva_tarea)
                 print(f"\nTarea '{nombre}' agregada correctamente.")
            else:
                 print("\nEl nombre de la tarea no puede estar vacío.")

        elif opcion == '2':
            print("\nProcesar Última Tarea ")
            tarea_procesada = pila_de_tareas.pop()
            if tarea_procesada:
                print("Procesando y eliminando la siguiente tarea:")
                print(tarea_procesada)
                print("\nTarea procesada y eliminada.")
            else:
                print("\nLa pila está vacía, no hay tareas para procesar.")

        elif opcion == '3':
            print("\n Ver Última Tarea (sin eliminar)")
            tarea_actual = pila_de_tareas.peek()
            if tarea_actual:
                print("La tarea más reciente en la pila es:")
                print(tarea_actual)
            else:
                print("\n La pila está vacía.")

        elif opcion == '4':
            pila_de_tareas.mostrar_todas()

        elif opcion == '5':
            num_tareas = len(pila_de_tareas)
            if num_tareas == 1:
                 print(f"\n Hay {num_tareas} tarea pendiente.")
            else:
                 print(f"\n Hay {num_tareas} tareas pendientes.")

        elif opcion == '0':
            print("\nSaliendo. ")
            sys.exit() 
        else:
            print("\n Opción no válida.")

        input("\nPresiona Enter para continuar")

if __name__ == "__main__":
    main()
