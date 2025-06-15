# Objetivos de la actividad

Esta actividad busca enseñarle al estudiante como se puede organizar código escrito en Python, de forma que el código se mantenga organizado y bien documentado. Además, busca reforzar las ventajas de escribir código
de manera modular, como la reutilización de código.

# Descripción de la actividad

Esta actividad consiste en implementar un módulo de utilidades matemáticas que implemente funciones que ejecutan procedimientos matemáticos comunes. En particular, dichas funciones deben:
- Calcular el área de un círculo dado su radio.
- Calcular el área de un rectángulo dado su ancho y alto.
- Calcular el área de un triángulo dada su base y altura.
- Calcular el factorial de un número.
- Determinar si un número es primo.

Opcionalmente, se solicita implementar una función que calcule el área de un polígono regular dado el número de lados y su lado.

# Resultados

Las funciones solicitadas, incluída la función para calcular el área de un polígono regular, fueron implementadas en el módulo math_utils.py, mientras que el script test.py  está escrito para probar que el módulo
mencionado funciona según lo esperado.

Cabe señalar que la función es_primo utiliza algunas propiedades conocidas de los números primos para optimizar el algoritmo. En particular, que todo número primo mayor a 3 es de la forma $6n \pm 1$, y que para buscar posibles
divisores de un número $k$ basta con buscar hasta $\sqrt{k}$. Además, la función para calcular el área de un polígono regular se puede encontrar en [este link](https://www.mathopenref.com/polygonregulararea.html).

Al ejecutar el script test.py se obtiene el siguiente resultado.

![image](https://github.com/user-attachments/assets/d6bb0be1-8d93-4e45-9b62-93ae1d833329)

Al comprobar con una calculadora, todos los resultados (salvo errores de redondeo) son correctos.
