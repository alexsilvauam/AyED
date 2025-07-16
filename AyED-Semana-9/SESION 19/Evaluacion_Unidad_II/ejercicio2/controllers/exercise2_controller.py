from ejercicio2.models.stack import Stack
from ejercicio2.views.exercise2_view import Exercise2View

class Exercise2Controller:
    def __init__(self):
        self.stack = Stack()
        self.view = Exercise2View()

    def is_balanced(self, expression):
        opening_brackets = {'(', '{', '['}
        closing_brackets = {')': '(', '}': '{', ']': '['}
        
        for char in expression:
            if char in opening_brackets:
                self.stack.push(char)
            elif char in closing_brackets:
                if self.stack.is_empty() or self.stack.pop() != closing_brackets[char]:
                    return False
        
        return self.stack.is_empty()

    def start(self):
        while True:
            self.view.show_menu()
            option = input("Seleccione una opción: ")
            
            if option == "1":
                expression = input("Ingrese la expresión a verificar: ")
                result = self.is_balanced(expression)
                self.view.show_result(result)
            elif option == "2":
                break
            else:
                self.view.show_invalid_option() 