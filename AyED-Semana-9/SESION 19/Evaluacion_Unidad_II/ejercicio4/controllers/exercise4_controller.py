from ejercicio4.models.priority_queue import PriorityQueue
from ejercicio4.views.exercise4_view import Exercise4View

class Exercise4Controller:
    def __init__(self):
        self.priority_queue = PriorityQueue()
        self.view = Exercise4View()

    def add_element(self, name, priority):
        try:
            priority = int(priority)
            self.priority_queue.enqueue(name, priority)
            return True
        except ValueError:
            return False

    def remove_element(self):
        return self.priority_queue.dequeue()

    def show_queue(self):
        return self.priority_queue.get_queue()

    def start(self):
        while True:
            self.view.show_menu()
            option = input("Seleccione una opción: ")
            
            if option == "1":
                name = input("Ingrese el nombre: ")
                priority = input("Ingrese la prioridad (número entero): ")
                if self.add_element(name, priority):
                    self.view.show_success("Elemento agregado exitosamente")
                else:
                    self.view.show_error("La prioridad debe ser un número entero")
            elif option == "2":
                element = self.remove_element()
                if element:
                    self.view.show_removed_element(element)
                else:
                    self.view.show_error("La cola está vacía")
            elif option == "3":
                queue = self.show_queue()
                self.view.show_queue(queue)
            elif option == "4":
                break
            else:
                self.view.show_invalid_option() 