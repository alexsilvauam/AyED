from ejercicio5.models.linked_list import LinkedList
from ejercicio5.views.exercise5_view import Exercise5View

class Exercise5Controller:
    def __init__(self):
        self.linked_list = LinkedList()
        self.view = Exercise5View()

    def add_element(self, value):
        self.linked_list.add(value)
        return True

    def search_element(self, value):
        return self.linked_list.search(value)

    def show_list(self):
        return self.linked_list.get_list()

    def start(self):
        while True:
            self.view.show_menu()
            option = input("Seleccione una opción: ")
            
            if option == "1":
                value = input("Ingrese el valor a agregar: ")
                self.add_element(value)
                self.view.show_success("Elemento agregado exitosamente")
            elif option == "2":
                value = input("Ingrese el valor a buscar: ")
                position = self.search_element(value)
                self.view.show_search_result(value, position)
            elif option == "3":
                elements = self.show_list()
                self.view.show_list(elements)
            elif option == "4":
                break
            else:
                self.view.show_invalid_option() 