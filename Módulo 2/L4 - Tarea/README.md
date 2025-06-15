# Objetivos de la actividad

Esta actividad busca comprobar el manejo práctico del estudiante sobre programación orientada a objetos (POO), a través del análisis de código preexistente.

# Descripción de la actividad

En esta actividad se entrega un código base escrito en Python, el cual se debe optimizar y hacer más legible a través de estructuras de datos estándar de Python, como diccionarios y conjuntos.

# Resultados

Tras analizar el código, se eliminaron algunos bucles reemplazándolos por funciones de las librerías estándar de Python, como las funciones [sum](https://docs.python.org/3/library/functions.html#sum) y
[filter](https://docs.python.org/3/library/functions.html#filter). Además, se reemplazan algunas estructuras de datos por otras más eficientes para el caso abordado, como el reemplazo de listas por conjuntos para la
verificación de unicidad de categorías.

El resultado de la refactorización del código se encuentra en el módulo analizador_financiero.py, mientras que en el script test.py se implementan y ejecutan funciones diseñadas para probar que
las funciones implementadas funcionan correctamente, en las cuales se implementan datos predefinidos y se comparan los resultados obtenidos con los esperados.
Al ejecutar el script, se obtienen las salidas mostradas en la siguiente imágen.

![image](https://github.com/user-attachments/assets/a1a794dd-2181-44ae-a6d9-4c17798a6153)

Como se indica en la imágen, todas las funciones funcionan con normalidad. Cabe señalar que en el archivo "Analizador Financiero.ipynb" se encuentra un Jupyter notebook que implementa esta misma funcionalidad
de manera interactiva.
