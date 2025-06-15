# -*- coding: utf-8 -*-
"""
Prueba de funcionalidad del módulo math_utils.
"""
from math_utils import (
    area_circulo,
    area_rectangulo,
    area_triangulo,
    area_poligono_regular,
    factorial,
    es_primo
    )

print("Área de un círculo de radio 2:", area_circulo(2))
print("Área de un rectángulo de ancho 2 y alto 4:", area_rectangulo(2, 4))
print("Área de un Triángulo de base 2 y altura 4:", area_triangulo(2, 4))
print("Área de un triángulo equilátero de lado 1:", area_poligono_regular(3, 1))
print("Área de un cuadrado de lado 1:", area_poligono_regular(4, 1))
print("Factorial de 5 (5!):", factorial(5))
print("¿2 es primo?:", es_primo(2))
print("¿8 es primo?:", es_primo(8))
print("¿73 es primo?:", es_primo(73))