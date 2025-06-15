# -*- coding: utf-8 -*-
"""
Ingresa calificaciones de manera aleatoria y valida las calificaciones aprobadas.
"""

import random

n_calificaciones = random.randint(8, 15)
calificaciones = []
for i in range(n_calificaciones):
    calificaciones.append(random.randint(0, 100))
print("Calificaciones:", calificaciones)

promedio = 0
aprobados = []
for calificacion in calificaciones:
    promedio += calificacion
    if calificacion >= 60:
        aprobados.append(calificacion)
promedio /= n_calificaciones

print("Promedio final:", promedio)
print("Número de aprobados:", len(aprobados))
print("Aprobados:", aprobados)