# -*- coding: utf-8 -*-
"""
Se prueba que la clase Auto funciona correctamente.
"""
from auto import Auto

auto = Auto(
    "Blanco",
    1.2,
    2.3,
    1.4,
    4.2,
    6,
    12,
    "Limosina",
    "Dañado"
    )
print(auto)
print()

auto.acelerar()
auto.arrancar()
auto.frenar()
auto.girar()