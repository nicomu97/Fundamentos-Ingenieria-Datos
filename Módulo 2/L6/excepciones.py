# -*- coding: utf-8 -*-
"""
Implementa las excepciones para la calculadora básica.

Clases:
    - DivisionPorCero
    - OperacionNoValida
"""

class DivisionPorCero(ArithmeticError):
    """Excepción en español para la división por cero."""

    def __init__(self):
        super().__init__("Error de división: No se puede divididr por cero.")
        

class OperacionNoValida(ValueError):
    """Excepción utilizada cuando el usuario ingresa una operación no reconocida."""

    def __init__(self, operacion, operaciones={"+", "-", "*", "/"}):
        self.operacion = operacion
        self.operaciones = operaciones
        super().__init__(
            f"Operación no reconocida: La operación ingresada debe ser una de "
            f"las siguientes opciones: {self.operaciones}, pero se recibió {self.operacion}"
            )