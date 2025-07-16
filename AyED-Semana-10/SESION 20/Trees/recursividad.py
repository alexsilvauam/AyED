def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
# Ejemplo de uso
if __name__ == "__main__":
    numero = 5
    resultado = factorial(numero)
    print(f"El factorial de {numero} es {resultado}")