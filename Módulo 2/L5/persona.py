# -*- coding: utf-8 -*-
"""
Módulo que implementa la clase Persona.
"""
import re

class Persona:
    """
    Almacena y administra datos de una persona.

    Atributos
    ---------
    - nombre: El nombre de la persona.
    - edad: Edad de la persona.

    Propiedades
    -----------
    - correo_electronico: Correo

    Métodos
    -------
    - actualizar_datos
    - es_mayor_edad
    """
    def __init__(self, nombre, edad, correo_electronico):
        self.nombre = nombre
        self.edad = edad
        self.correo_electronico = correo_electronico


    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nCorreo: {self.correo_electronico}"
    
    @property
    def correo_electronico(self):
        return self._correo_electronico

    @correo_electronico.setter
    def correo_electronico(self, correo_electronico):
        match = re.search("[a-zA-Z]+@[a-zA-Z]+[.][a-zA-Z]", correo_electronico)
        if not match:
            raise ValueError("Correo inválido: Por favor revise el correo ingresado.")
        self._correo_electronico = correo_electronico

    def actualizar_datos(self, nombre, edad, correo_electronico):
        """
        Actualiza los datos de la persona.

        Parámetros
        ----------
        - nombre: Nuevo nombre de la persona.
        - edad: Nueva edad de la persona.
        - correo_electronico: Nuevo correo electrónico de la persona.

        Retorna
        -------
        None
        """
        self.nombre = nombre
        self.edad = edad
        self.correo_electronico = correo_electronico

    def es_mayor_edad(self):
        """
        Verifica si la persona es mayor de edad.

        Retorna
        -------
        es_mayor: True si la persona tiene 18 años o más, False en otro caso.
        """
        if self.edad < 18:
            return False
        else:
            return True

