def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular():
    operacion = input("Elija la operación que desea ejecutar (+|-|*|/) ")
    if operacion not in {"+", "-", "*", "/"}:
        print("Operación no reconocida. Por favor, inténtelo de nuevo.")
        return
    numero1 = int(input("Ingrese el primer operando: "))
    numero2 = int(input("Ingrese el segundpo operando: "))
    if operacion == "/" and numero2 == 0:
        print("Opración inválida: no se puede dividir por cero. Por favor, intételo de nuevo.")
        return

    if operacion == "+":
        resultado = sumar(numero1, numero2)
    elif operacion == "-":
        resultado = restar(numero1, numero2)
    elif operacion == "*":
        resultado = multiplicar(numero1, numero2)
    else:
        resultado = dividir(numero1, numero2)
    
    print(f"{numero1} {operacion} {numero2} = {resultado}")

calcular()