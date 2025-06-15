# -*- coding: utf-8 -*-
"""
Define un diccionario de empleado.

Se crea una lista con los empleados mayores a 30 años y se imprimen los nombre de los
menores a 30.
"""

empleados = {
    "emp1": {"Nombre": "Pedro", "Edad": 31},
    "emp2": {"Nombre": "Pablo", "Edad": 13},
    "emp3": {"Nombre": "Emilia", "Edad": 25},
    "emp4": {"Nombre": "Cristina", "Edad": 43},
    "emp5": {"Nombre":"Alejandro", "Edad": 62},
}

mayores = []
for emp, datos in empleados.items():
    if datos["Edad"] > 30:
        mayores.append(datos["Nombre"])
    else:
        print(f"El empleado {datos['Nombre']} tiene {datos['Edad']} años.")
print("N° empleados mayores a 30 años:", len(mayores))
print("empleados mayores a 30 años:", mayores)