# -*- coding: utf-8 -*-
"""
Prueba que la clase AnalizadorFinanciero funcione correctamente.
"""
from analizador_financiero import AnalizadorFinanciero

def prueba_total_ingresos():
    transacciones = [100000, 200000, 500000, 200000]
    total_esperado = 1000000
    analizador = AnalizadorFinanciero()
    total_ingresos = analizador.calcular_total_ingresos(transacciones)
    if total_ingresos == total_esperado:
        print("Método calcular_total_ingresos funcionando correctamente")
    else:
        print(f"Error en método calcular_total_ingresos: {total_ingresos} != {total_esperado}")

def prueba_filtrar_ingresos():
    transacciones = [100000, 200000, 500000, 200000]
    umbral = 150000
    resultado_esperado = [200000, 500000, 200000]
    analizador = AnalizadorFinanciero()
    ingresos_altos = analizador.filtrar_ingresos_altos(transacciones, umbral)
    if ingresos_altos == resultado_esperado:
        print("Método filtrar_ingresos_altos funcionando correctamente")
    else:
        print(f"Error en método filtrar_ingresos_altos: {ingresos_altos} != {resultado_esperado}")

def prueba_agrupar():
    transacciones = [100000, 200000, 500000, 200000]
    categorias = ["alimentos", "vestuario", "vehiculos", "alimentos"]
    resultado_esperado = {
        "alimentos": [100000, 200000],
        "vestuario": [200000],
        "vehiculos": [500000]
    }
    analizador = AnalizadorFinanciero()
    agrupado = analizador.agrupar_por_categoria(transacciones, categorias)
    if agrupado == resultado_esperado:
        print("Método agrupar_por_categoria funcionando correctamente")
    else:
        print(f"Error en método agrupar_por_categoria: {agrupado} != {resultado_esperado}")

prueba_total_ingresos()
prueba_filtrar_ingresos()
prueba_agrupar()