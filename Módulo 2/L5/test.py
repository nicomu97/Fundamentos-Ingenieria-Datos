# -*- coding: utf-8 -*-
"""
Se realiza una comprobación de funcionalidad de la clase Persona.
"""
from persona import Persona

# Correo inválido
try:
    persona1 = Persona("Roberto", 23, "abc")
except ValueError as e:
    print(e)
    print()

persona2 = Persona("Roberto", 23, "roberto@gmail.com")
print(persona2)
persona2.actualizar_datos("Robert", 24, "robert@gmail.cl")

print()
print(persona2)

if persona2.es_mayor_edad():
    print(f"Persona {persona2.nombre} es mayor de edad")
else:
    print(f"Persona {persona2.nombre} es menor de edad")