"""Crea una clase ValidadorParentesis que utilice internamente una pila para validar si una expresión
 matemática tiene paréntesis correctamente balanceados. Implementa un método
   esBalanceado(String expresion) que analice la expresión carácter por carácter, 
   apilando los paréntesis abiertos y desapilando cuando encuentres paréntesis cerrados. 
   El método debe retornar true si todos los paréntesis están correctamente balanceados, y false en caso contrario. 
   Prueba tu validador desde la clase Main, solicitando al usuario ingresar diferentes expresiones."""

# Clase que valida paréntesis balanceados
class ValidadorParentesis:
    def __init__(self):
        self.pila = []

    def esBalanceado(self, expresion):
        self.pila = []  
        for caracter in expresion:
            if caracter == '(':
                self.pila.append(caracter)  
            elif caracter == ')':
                if not self.pila:
                    return False  
                self.pila.pop() 
        return len(self.pila) == 0 

def main():
    validador = ValidadorParentesis()
    
    while True:
        expresion = input("Ingresa una expresión matemática (o escribe 'salir' para terminar): ")
        if expresion.lower() == 'salir':
            break
        
        if validador.esBalanceado(expresion):
            print("Los paréntesis están balanceados.")
        else:
            print("Los paréntesis NO están balanceados.")

if __name__ == "__main__":
    main()
