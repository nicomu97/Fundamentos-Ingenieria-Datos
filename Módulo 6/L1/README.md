# Resumen Ejecutivo

La empresa DataSolutions S.A., especializada en el análisis predictivo
de datos para clientes de distintos rubros, enfrenta un desafío
recurrente. Sus analistas reciben grandes volúmenes y necesitan
seleccionar el enfoque correcto de aprendizaje de máquina para resolver
diversos problemas de negocio, como predecir ventas, detectar clientes
que abandonarán el servicio, y segmentar perfiles de usuario.

La dirección de la empresa ha decidido incorporar un proceso sistemático
para seleccionar, diseñar y evaluar modelos de aprendizaje de máquina.
En particular, en nuestro rol como analista de datos se nos solicita
ejecutar las siguientes tareas:

1.  Clasificación del problema

    -   Analizar los tres problemas planteados y clasificar cada uno
        según el tipo de tarea de aprendizaje de máquina.

        Problema A: Predecir el monto de ventas semanales de una cadena
        de supermercados.

        Problema B: Detectar si un cliente abandonará un servicio de
        streaming.

        Problema C: Agrupar a los clientes bancarios por comportamiento
        de gasto sin tener etiquetas.

2.  Selección de modelos y justificación

    -   Para cada problema, seleccionar un algoritmo adecuado.

    -   Justificar la elección y menciona sus ventajas y limitaciones.

3.  Identificación de riesgos

    -   Describir posibles desafíos que pueden surgir al aplicar el
        modelo.

4.  Diseño del flujo de trabajo

    -   Elaborar un esquema donde se muestren las etapas típicas del
        proceso de aprendizaje de máquina aplicadas a uno de los casos.

# Análisis del caso

Se analizará cada problema de manera individual, dado que distintos
problemas requieren distintos enfoques.

## Problema A: Predicción de ventas semanales

Primero, notar que el valor a predecir en este caso es un valor
continuo, pues el valor de ventas semanales puede tomar cual valor mayor
o igual a 0, por lo que esta corresponde a una tarea de regresión.
Además, el hecho de poder usar ventas de semanas anteriores como valores
objetivos de entrenamiento nos permite abordar este problema como uno de
aprendizaje supervisado.

En cuanto al algoritmo a utilizar en este caso, dado que las ventas no
están acotados dentro de un rango fijo, y las ventas de la próxima
semana pueden depender de las ventas de semanas anteriores, así como de
variables temporales, un modelo de regresión lineal resulta adecuado
para este caso.

El modelo seleccionado cuenta con la ventaja de que es capaz de
extrapolar predicciones a valores que se encuentran fuera de los rangos
vistos durante el entrenamiento, lo cual es común al analizar variables
económicas. Además, nos permite introducir la variable tiempo como una
variable incremental. Sin embargo, dada la simplicidad del modelo, este
no es capaz de capturar comportamientos no lineales, por lo que la etapa
de procesamiento de datos podría requerir mayor trabajo para crear
variables que linealicen estos comportamientos.

En cuanto al problema en sí, este presenta el gran desafío de introducir
e interpretar variables temporales, además de la correlación entre la
variable objetivo y observaciones anteriores en la misma. Abordar este
tipo de desafíos normalmente requiere el uso de técnicos avanzadas de
análisis de series de tiempo.

En la imágen a continuacion se muestra el diagrama de flujo de trabajo
para este problema.

![image](Diagramas/L1_diagrama_flujo){width="\\textwidth"}

## Problema B: Detección de abandono de clientes

Este problema, como está planteado, se puede reducir a un problema de
clasificación binaria, pues se intenta predecir si un cliente abandona o
no el servicio contratado. Además, asumiendo que tenemos datos de
clientes que han abandonado el servicio, y de clientes que mantienen el
servicio contratado, este problema se puede tratar como uno de
aprendizaje supervisado.

Dada la naturaleza del problema, un algoritmo de regresión logística
resulta más adecuado para este problema pues, frente a otros modelos de
clasificación como los bosques aleatorios, entrega la ventaja adicional
de predecir probabilidades, lo que nos permite hacer un ranking de los
clientes que es más probable que abandonen el servicio.

Sin embargo, el modelo escogido tiene la limitación de que, al ser uno
de los modelos más sencillos dentro de la familia de modelos de
clasificación, podría no ser suficiente para entregar predicciones lo
suficientemente precisas para resolver este problema. Si la precisión es
más importante para el cliente que la estimación de probabilidades, un
bosque aleatorio de clasificación podría ser más adecuado.

Cabe señalar que este problema presenta el desafío de que el
comportamiento de los clientes cambia con el tiempo, por lo que se
podría requerir un análisis más detallado de los clientes que abandonan,
por ejemplo agrupándolos en distintos grupos, para determinar las
razones por las que estos abandonan, y así el cliente pueda tomar
medidas para mejorar su servicio. Por otro lado, la clasificación podría
requerir de una gran cantidad de variables, lo que podría generar un
problema de dimensionalidad, requiriendo la identificación de las
variables más relevantes para el problema.

## Problema C: Agrupación de clientes bancarios por comportamiento de gasto

En este caso, como se señala explícitamente la ausencia de etiquetas
para entrenamiento, este cae en un problema de aprendizaje no
supervisado. Además, como se nos señala que el objetivo es agrupar
clientes según su comportamiento, este además es un problema de
agrupamiento (clustering).

Dado lo anterior, y dado que el rubro financiero está altamente
regulado, el algoritmo KNN resulta la elección más adecuada para este
problema por su simplicidad y su capacidad de aprender categorías sin
conocerlas de antemano.

A pesar de lo anterior, el algoritmo KNN conlleva también una serie de
limitaciones: es computacionalmente costoso, por lo que podría no ser la
mejor opción si el conjunto de datos del cliente es muy grande. Por otro
lado, requiere ajustar el parámetro N para determinar la cantidad óptima
de grupos, lo cual requiere entrenar el modelo múltiples veces. Por
último, el algoritmo solo funciona de manera óptimo si las agrupaciones
tienen una geometría esférica, lo que solo se puede verificar una vez
identificados dichos grupos.

El principal desafío que presenta este problema en general es determinar
un escalamiento adecuado para las variables, dado que los algoritmos de
agrupamiento suelen ser sensibles a las distancias entre puntos. De esta
forma, si las variables están en distintas escalas, aquellas con valores
más altos podrían resultar muy dominantes en el modelo. Por último, el
elevado costo computacional que suele acompañar a los algoritmos de
agrupamiento puede requerir pasos de procesamiento de datos adicionales
para reducir la dimensionalidad del problema.

# Conclusiones

Al abordar un problema de aprendizaje de máquina, es importante primero
entender el problema antes de lanzarse a desarrollar una solución. Esto
nos permite comprender desde el inicio los objetivos que busca
satisfacer el proyecto, así como los modelos y métricas de evaluación
más adecuadas para este. De esta forma se acorta el proceso de
desarrollo, permitiendo un progreso rápido y una planificación adecuada
del proceso.
