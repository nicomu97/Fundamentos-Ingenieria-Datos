# -*- coding: utf-8 -*-
"""
Implementa una calculadora básica con validación de entradas del usuario.
"""
from operaciones import sumar, restar, multiplicar, dividir
from excepciones import DivisionPorCero, OperacionNoValida

def calcular():
    operaciones = {"+", "-", "*", "/"}
    operacion = input("Elija la operación que desea ejecutar (+|-|*|/) ")
    try:
        if operacion not in operaciones:
            raise OperacionNoValida(operacion, operaciones)
    except OperacionNoValida as e:
        print(e)
        return

    numero1 = input("Ingrese el primer operando: ")
    try:
        numero1 = int(numero1)
    except ValueError:
        print(f"Error de validación: El valor ingresado debe ser un valor numérico, pero se ingresó {numero1}.")
        return
    numero2 = input("Ingrese el segundpo operando: ")
    try:
        numero2 = int(numero2)
    except ValueError:
        print(f"Error de validación: El valor ingresado debe ser un valor numérico, pero se ingresó {numero2}.")
        return
    try:
        if operacion == "/" and numero2 == 0:
            raise DivisionPorCero()
    except DivisionPorCero as e:
        print(e)
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