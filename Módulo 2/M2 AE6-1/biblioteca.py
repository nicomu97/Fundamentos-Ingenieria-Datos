# -*- coding: utf-8 -*-
"""
Se implementan las clases base para la gestión de la biblioteca.

Calses
------
- LibroNoDisponibleError
- Libro
- Biblioteca
"""

class LibroNoDisponibleError(ValueError):
    """Excepción que se levanta cuando no hay stock de un libro a prestar."""

    def __init__(self, libro):
        self.libro = libro
        super().__init__(f"Libro no disponible: El libro {self.libro.titulo} no tiene stock para préstamo.")


class Libro:
    """
    Implementa las propiedades básicas de un libro.

    Propiedades
    -----------
    - titulo: String representando el título del libro.
    - autor: Nombre del autor de este libro.
    - stock: Cantidad de libros disponible para préstamo.
    """

    def __init__(self, titulo, autor, stock=0):
        self.titulo = titulo
        self.autor = autor
        self.stock = stock

    def __str__(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nUnidades en stock: {self.stock}"

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        if not isinstance(titulo, str):
            raise ValueError(f"Títutlo debe ser una variable tipo str, pero se recibió {type(titulo)}")
        self._titulo = titulo

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, autor):
        if not isinstance(autor, str):
            raise ValueError(f"Autor debe ser una variable tipo str, pero se recibió {type(autor)}")
        self._autor = autor

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, stock):
        if not isinstance(stock, int):
            raise ValueError(f"Stock debe ser un número entero, pero se recibió {type(stock)}")
        if stock < 0:
            raise ValueError(f"Stock debe ser un número no negativo, pero se recibió {stock}")
        self._stock = stock


class Biblioteca:
    """
    Realiza operaciones de gestión sobre instancias de la clase Libro.

    Métodos
    -------
    - prestar_libro
    """

    def __init__(self, catalogo):
        self.catalogo = catalogo

    def __str__(self):
        msg = "Catálogo:\n"
        for id_libro, libro in self.catalogo.items():
            msg += f"ID: {id_libro}\n"
            msg += f"\t- Título: {libro.titulo}\n"
            msg += f"\t- Autor: {libro.autor}\n"
            msg += f"\t- Unidades en stock: {libro.stock}\n\n"
        return msg

    @property
    def catalogo(self):
        return self._catalogo

    @catalogo.setter
    def catalogo(self, catalogo):
        if not isinstance(catalogo, dict):
            raise ValueError(f"Se espera que catalogo sea un diccionario de libros, pero se recibió {type(catalogo)}")
        for id_libro, libro in catalogo.items():
            if not isinstance(libro, Libro):
                raise ValueError(f"Elemento con ID {id_libro} no es de clase Libro, sino de tipo {type(libro)}.")
        self._catalogo = catalogo

    def prestar_libro(self, titulo):
        """
        Entrega un libro en préstamo.

        Si no hay stock del libro, este método levanta una excepción
        LibroNoDisponibleError. En otro caso, se actualiza el stock del libro.

        Parámetros
        ----------
        - libro: una instancia de la clase Libro que se va a prestar.

        Retorna
        -------
        None
        """
        en_catalogo = False
        for id_libro, libro in self.catalogo.items():
            if titulo == libro.titulo:
                #id_prestamo = id_libro
                libro_prestamo = libro
                en_catalogo = True
                break
        if not en_catalogo:
            raise ValueError(f"Libro no encontrado: el título {titulo} no se encuentra en el catálogo.")

        if libro_prestamo.stock == 0:
            raise LibroNoDisponibleError(libro_prestamo)
        libro_prestamo.stock -= 1
