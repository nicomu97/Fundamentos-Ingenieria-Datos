# -*- coding: utf-8 -*-
"""
Se implementa la clase AnalizadorFinanciero para operaciones sobre transacciones.
"""

class AnalizadorFinanciero:
    """
    Clase que realiza una serie de operaciones sobre transacciones.

    Métodos
    -------
    - calcular_total_ingresos
    - filtrar_ingresos_altos
    - agrupar_por_categoria
    """

    def calcular_total_ingresos(self, transacciones):
        """Calcula el total de ingresos en una lista de transacciones."""
        return sum(transacciones)

    def filtrar_ingresos_altos(self, transacciones, umbral):
        """Filtra y retorna solo los ingresos mayores a un umbral dado."""
        return list(filter(lambda x: x > umbral, transacciones))

    def agrupar_por_categoria(self, transacciones, categorias):
        """Agrupa ingresos en un diccionario por categorias"""
        agrupado = {}
        categorias_vistas = set()
        for categoria, ingreso in zip(categorias, transacciones):
            if categoria in categorias_vistas:
                agrupado[categoria].append(ingreso)
            else:
                categorias_vistas.add(categoria)
                agrupado[categoria] = [ingreso]
        return agrupado

