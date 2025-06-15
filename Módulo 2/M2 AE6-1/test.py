# -*- coding: utf-8 -*-
"""
Prueba de funcionalidad de las clases Libro y Biblioteca.
"""
from biblioteca import Libro, Biblioteca, LibroNoDisponibleError

sherlock = Libro("Sherlock Holmes", "Conan Doyle", 1)
witcher = Libro("The Witcher", "Andrzej Sapkowski", 3)
catalogo = {1: sherlock, 2: witcher}
biblioteca = Biblioteca(catalogo)
print(biblioteca)

biblioteca.prestar_libro("Sherlock Holmes")
print(biblioteca)

try:
    biblioteca.prestar_libro("Sherlock Holmes")
except LibroNoDisponibleError as e:
    print(e)
    print()

try:
    biblioteca.prestar_libro("Título inexistente")
except ValueError as e:
    print(e)
    print()

print(biblioteca)
