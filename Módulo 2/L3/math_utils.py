"""
Este módulo implementa utilidades matemáticas para cálculos comunes.

El módulo implementa las siguientes funciones:
    
    - area_circulo
    - area_rectangulo
    - area_triangulo
    - area_poligono_regular
    - factorial
    - es_primo
"""
import math

def area_circulo(r):
    """
    Calcula el área de un círculo, dado su radio.

    Parámetros
    ----------
    - r: Radio del círculo

    Retorna
    -------
    - area: El área del círculo.
    """
    return math.pi * r**2

def area_rectangulo(ancho, alto):
    """
    Cálcula el área de un rectángulo dado su ancho y alto.

    Parámetros
    ----------
    - ancho: El ancho del rectángulo.
    - alto: El alto del rectángulo.

    Retorna
    -------
    area: El área del rectángulo.
    """
    return ancho * alto

def area_triangulo(base, altura):
    """
    Calcula el área de un triángulo, dada su base y altura.

    Parámetros
    ----------
    - base: Medida de la base del triángulo.
    - altura: La altura del triángulo.

    Retorna
    -------
    area. El área del triángulo.
    """
    return base * altura / 2

def area_poligono_regular(n_lados, lado):
    """
    Calcula el área de un polígono regular dado el número de lados y su lado.

    Parámetros
    ----------
    - n_lados: Número de lados del polígono.
    - lado: Medida del lado del polígono regular.

    Retorna
    -------
    area: El área del polígono.
    """
    return n_lados * (lado ** 2) * (1 / math.tan(math.pi / n_lados)) / 4

def factorial(n):
    """
    Calcula el factorial de un número natural n.

    Parámetros
    ----------
    - n: El número al cual se le calculará su factorial.

    Retorna
    -------
    resultado: El resultado de la operación n!.
    """
    if n < 0:
        return 0
    if n < 2:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def es_primo(n):
    """
    Determina si un número natural n es o no primo.

    Parámetros
    ----------
    n: El número a consultar.

    Retorna
    -------
    resultado: True si n es primo, False en otro caso.
    """
    if n <= 1:
        return False
    if n > 3 and n % 6 not in {1, 5}:
        return False

    maximo_divisor = int(n ** 0.5)
    for i in range(2, maximo_divisor + 1):
        if n % i == 0:
            return False
    return True
