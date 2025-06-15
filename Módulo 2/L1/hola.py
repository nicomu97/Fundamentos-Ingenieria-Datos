# hola.py - Tu primer programa en Python
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("Qué edad tienes? "))
mayor_o_menor = "mayor" if edad >= 18 else "menor"
print(f"¡Hola, {nombre}, {mayor_o_menor} de edad! Bienvenido al mundo de Python.")