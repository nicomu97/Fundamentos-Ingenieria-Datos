# -*- coding: utf-8 -*-
"""
Módulo que implementa la clase auto.
"""

class Auto:
    """
    Clase que implementa las propiedades y métodos básicos de un auto.

    Propiedades
    -----------
    - color: String que representa el color del auto.
    - peso: Variable numérica positiva indicando el peso del auto en toneladas.
    - tamano: Variable numérica positiva que indica el tamaño del auto en metros cúbicos.
    - alto: Variable numérica positiva indicando el alto del auto en metros.
    - largo: Variable numérica positiva que indica el largo del auto en metros.
    - n_ruedas: Número entero positivo que indica el número de ruedas que tiene el auto.
    - n_puertas: Número entero positivo que indica el número de puertas.
    - tipo: String que representa el tipo del auto.
    - estado: String que indica el estado del auto. Los posibles estados son:
        - Detenido
        - Circulando
        - Estacionado
        - Dañado

    Métodos
    -------
    - arrancar
    - frenar
    - acelerar
    - girar
    """
    def __init__(self, color, peso, tamano, alto, largo, n_ruedas, n_puertas, tipo, estado):
        self.color = color
        self.peso = peso
        self.tamano = tamano
        self.alto = alto
        self.largo = largo
        self.n_ruedas = n_ruedas
        self.n_puertas = n_puertas
        self.tipo = tipo
        self.estado = estado

    def __str__(self):
        mensaje = (f"Color: {self.color}\n"
                   f"Peso: {self.peso} toneladas\n"
                   f"Tamaño: {self.tamano} m3\n"
                   f"Alto: {self.alto} m\n"
                   f"Largo {self.largo} m\n"
                   f"Número de ruedas: {self.n_ruedas}\n"
                   f"Número de puertas. {self.n_puertas}\n"
                   f"Tipo: {self.tipo}\n"
                   f"Estado: {self.estado}")
        return mensaje

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise ValueError(f"Color debe ser un string, pero se recibió un {type(color)}.")
        self._color = color

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, peso):
        if not isinstance(peso, (int, float)):
            raise ValueError(f"Peso debe ser una variable numérica, pero se recibió un {type(peso)}.")
        if peso <= 0:
            raise ValueError("Peso debe ser un número positivo.")
        self._peso = peso

    @property
    def tamano(self):
        return self._tamano

    @tamano.setter
    def tamano(self, tamano):
        if not isinstance(tamano, (int, float)):
            raise ValueError(f"Tamano debe ser una variable numérica, pero se recibió un {type(tamano)}.")
        if tamano <= 0:
            raise ValueError("Tamaño debe ser un número positivo.")
        self._tamano = tamano

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if not isinstance(alto, (int, float)):
            raise ValueError(f"Alto debe ser una variable numérica, pero se recibió un {type(alto)}.")
        if alto <= 0:
            raise ValueError("Alto debe ser un número positivo.")
        self._alto= alto

    @property
    def largo(self):
        return self._largo

    @largo.setter
    def largo(self, largo):
        if not isinstance(largo, (int, float)):
            raise ValueError(f"Largo debe ser una variable numérica, pero se recibió un {type(largo)}.")
        if largo <= 0:
            raise ValueError("Largo debe ser un número positivo.")
        self._largo = largo

    @property
    def n_ruedas(self):
        return self._n_ruedas

    @n_ruedas.setter
    def n_ruedas(self, n_ruedas):
        if not isinstance(n_ruedas, int):
            raise ValueError(f"n_ruedas debe ser un entero, pero se recibió un {type(n_ruedas)}.")
        if n_ruedas <= 0:
            raise ValueError("El número de ruedas debe ser un entero positivo.")
        self._n_ruedas = n_ruedas

    @property
    def n_puertas(self):
        return self._n_puertas

    @n_puertas.setter
    def n_puertas(self, n_puertas):
        if not isinstance(n_puertas, int):
            raise ValueError(f"n_puertas debe ser un entero, pero se recibió un {type(n_puertas)}.")
        if n_puertas <= 0:
            raise ValueError("El número de puertas debe ser un entero positivo.")
        self._n_puertas = n_puertas

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        if not isinstance(tipo, str):
            raise ValueError(f"Tipo debe ser un string, pero se recibió un {type(tipo)}.")
        self._tipo = tipo

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        estados = {"Detenido", "Circulando", "Estacionado", "Dañado"}
        if estado not in estados:
            raise ValueError(f"Estado debe ser un uno de los siguientes valores: {estados}. Se recibió {estado}.")
        self._estado = estado

    def arrancar(self):
        """Imprime un mensaje indicando que el auto está arrancando."""
        print("El auto está arrancando.")

    def frenar(self):
        """Imprime un mensaje indicando que el auto está frenando."""
        print("El auto está frenando.")

    def acelerar(self):
        """Imprime un mensaje indicando que el auto está acelerando."""
        print("El auto está acelerando.")

    def girar(self):
        """Imprime un mensaje indicando que el auto está girando."""
        print("El auto está girando.")
