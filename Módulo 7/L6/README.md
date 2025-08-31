# Resumen Ejecutivo

Una empresa de e-commerce está experimentando un aumento significativo
en la cantidad de datos que recibe diariamente de sus clientes:
registros de navegación, historial de compras y calificaciones de
productos. El equipo de datos de la empresa se enfrenta al desafío de
analizar estos datos para predecir si un cliente realizará una compra en
los próximos días, con el fin de personalizar campañas publicitarias y
mejorar la experiencia del usuario.

Hasta ahora, los analistas han utilizado soluciones de Machine Learning
tradicionales, pero el volumen de datos actual supera la capacidad de
procesamiento de sus herramientas. Por ello, la empresa decidió
implementar un modelo de Machine Learning escalable utilizando Apache
Spark MLib, que les permite procesar millones de registros de forma
distribuida y eficiente.

En nuestro rol de Data Scientist se nos ha encargado diseñar e
implementar una solución predictiva usando MLib. En particular, se nos
solicita realizar las siguientes tareas:

1.  Preparar los datos de entrada, asegurándonos de que contengan las
    características necesarias y la etiqueta objetivo.

2.  Utilizar las herramientas de MLib para transformar y vectorizar las
    características.

3.  Implementar un modelo supervisado de clasificación.

4.  Dividir los datos en conjunto de entrenamiento y prueba.

5.  Ajustar los hiperparámetros del modelo utilizando validación
    cruzada.

6.  Evaluar el desempeño del modelo utilizando métricas como Área bajo
    la curva ROC y Precisión.

7.  Presentar un informe con los resultados obtenidos y sugerencias para
    futuras mejoras.

# Análisis del caso

Para esta actividad, se usó el conjunto de datos disponible en [este
link](https://www.kaggle.com/datasets/adilshamim8/online?resource=download).
Este conjunto de datos contiene información sobre la intención de compra
de más de 12.000 sesiones web, recopilada a lo largo de un año, la cual
incluye la columna "Revenue" como variable objetivo.

Para desarrollar el modelo de clasificación, se implementa código en
pyspark con un pipeline que va desde la etapa de preprocesamiento de
datos hasta la selección de hiperparámetros del modelo utilizado, el
cual corresponde a un Random Forest Classifier.

A lo largo, del pipeline se procesan las variables categóricas para
crear un StringIndex y, posteriormente, convertirlas en variables
numéricas usando el método One-Hot Encoding. Dado que no se encuentran
valores faltantes en el dataset, no se requiere imputar datos en la
etapa de preprocesamiento. Además, dado que el modelo utilizado no es
sensible a la escala de los datos, tampoco es necesario implementar una
etapa de escalamiento.

Una vez preprocesados los datos, el pipeline alimenta el modelo con las
características resultantes. Los hiperparámetros son seleccionados a
través de un CrossValidator con 5 folds, al se le entrega el pipeline
completo para ser refinado. Para evaluar el desempeño del modelo, se
utiliza la métrica área bajo la curva ROC, la cual también es utilizada
para seleccionar los hiperparámetros del modelo.

Antes de entrenar el modelo, se separa el conjunto de datos en conjunto
de entrenamiento y prueba, en una proporción de 60%-40%,
respectivamente, usando técnicas de muestreo estratificado. Posterior al
entrenamiento del modelo, se obtiene un ROCAUC de 0.97 para el conjunto
de entrenamiento y 0.91 para el conjunto de prueba, lo cual es un
indicativo de que el modelo está sobreajustado.

A pesar de lo anterior, debido al alto valor obtenido en la métrica al
evaluar el modelo en el conjunto de prueba, se observa que el modelo
generaliza bastante bien los patrones aprendidos.

Para mejorar los resultados obtenidos, se sugiere:

- Analizar las características utilizadas en mayor profundidad, para
  detectar posibles problemas de multi-colinearidad y tomar medidas en
  consecuencia.

- Realizar un proceso de selección de variables para identificar las que
  sean más significativas, filtrando las que aporten poco o nulo valor
  al análisis predictivo.

- Probar distintos algoritmos de clasificación binaria para determinar
  que técnica se ajusta mejor al problema.

- Realizar una selección de hiperparámetros sobre un espacio más
  extenso, utilizando técnicas de búsqueda más eficientes, como búsqueda
  bayesiana (usando, por ejemplo, [optuna](https://optuna.org/) para
  dicho propósito), reduciendo los riesgos de sobre ajuste.

# Conclusión

Spark resulta ser una herramienta sumamente versátil para el desarrollo
de diversas aplicaciones de big data. Sus variadas librerías integradas
en una sola tecnología nos permite ejecutar todo el ciclo de vida de un
modelo, desde la extracción y preparación de datos, hasta la selección
de hiperparámetros y la implementación del modelo. Todo lo anterior, de
forma horizontalmente escalable, dado que Spark nos permite realizar
dicho proceso en un cluster de cientos, o incluso miles de nodos.

De esta forma, Spark se convierte en una herramienta en gran medida
esencial para trabajar en procesos de big data.
