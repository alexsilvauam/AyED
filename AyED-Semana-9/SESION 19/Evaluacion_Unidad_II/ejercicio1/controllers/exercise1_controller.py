from ejercicio1.models.stack import Stack
from ejercicio1.views.exercise1_view import Exercise1View

class Exercise1Controller:
    def __init__(self):
        self.stack = Stack()
        self.view = Exercise1View()

    def reverse_words(self, phrase):
        # Dividir la frase en palabras
        words = phrase.split()
        
        # Apilar las palabras
        for word in words:
            self.stack.push(word)
        
        # Construir la frase invertida
        reversed_phrase = []
        while not self.stack.is_empty():
            reversed_phrase.append(self.stack.pop())
        
        return " ".join(reversed_phrase)

    def start(self):
        while True:
            self.view.show_menu()
            option = input("Seleccione una opción: ")
            
            if option == "1":
                phrase = input("Ingrese la frase a invertir: ")
                result = self.reverse_words(phrase)
                self.view.show_result(result)
            elif option == "2":
                break
            else:
                self.view.show_invalid_option() 