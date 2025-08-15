# Resumen Ejecutivo

La empresa AutoPredict S.A., dedicada al desarrollo de sistemas de
predicción de precios para concesionarios de automóviles, ha recibido la
solicitud de un nuevo cliente, el cual desea un modelo capaz de estimar
el precio de venta de vehículos usados en función de características
como antigüedad, kilometraje y número de puertas.

El equipo de científicos de datos de AutoPredict ha desarrollado un
primer modelo utilizando regresión lineal, pero no cuenta con un
procedimiento documentado para evaluar si el modelo es adecuado o si
existen oportunidades de mejora. En nuestro rol de científicos de datos,
la gerencia nos ha solicitado realizar un análisis detallado para
validar y ajustar el modelo antes de ponerlo en producción. En
particular, se nos solicita realizar las siguientes tareas:

1.  Analizar el fragmento de datos en la tabla
    1 proporcionados por el cliente

      ID  | Antigüedad (años)  | Kilometraje (km)  | Puertas  | Precio (USD)
      ----| -------------------| ------------------| ---------| --------------
      1   | 5                  | 50000             | 4        | 12000
      2   | 3                  | 30000             | 2        | 15000
      3   | 7                  | 70000             | 4        | 9000
      4   | 2                  | 25000             | 2        | 16000

    Tabla 1: Datos provistos por el cliente

3.  Crear un modelo de regresión lineal para predecir el precio en
    función de variables: Antigüedad, Kilometraje y Puertas.

4.  Dividir los datos en un conjunto de entrenamiento y prueba
    (80%-20%).

5.  Entrenar el modelo y realizar las predicciones correspondientes.

6.  Calcular las métricas de desempeño: MAE, MSE, RMSE y R$^2$.

7.  Analizar los resultados y responder:

    -   ¿Qué tan preciso es el modelo?

    -   ¿Qué decisiones tomarías para mejorar su desempeño?

8.  Realizar un gráfico comparativo de los precios reales y los
    predichos.

# Análisis del caso

Al realizar una inspección rápida de los datos, observamos que este
conjunto de datos no contiene datos perdidos, y además todas las
variables se encuentran en rangos razonables. Además, no hay variables
categóricas en los datos. Sin embargo, dado que los modelos de regresión
lineal son sensibles a la escala de las variables, es necesario realizar
un escalamiento a las variables para que se encuentren en un rango de
valores similar. Dado que los valores de observaciones futuras pueden no
estar dentro del rango visto en este conjunto de datos, optaremos por un
escalamiento usando el método Z-Score.

Al entrenar el modelo y evaluarlo en el conjunto de prueba, se obtienen
las siguientes métricas:

-   MAE: 437.5

-   MSE: 191406.24

-   RMSE: 437.5

De lo anterior, se observa un buen desempeño del modelo, pues el error
representa alrededor del 5% del valor real. Notar que no se incluye la
métrica del coeficiente R$^2$ debido a que esta métrica requiere de al
menos dos observaciones en el conjunto de prueba, mientras que, dado el
tamaño pequeño del conjunto de datos original, nuestro conjunto de
prueba contiene solo una observación.

Para sortear este obstáculo, se calculó el coeficiente R$^2$ en el
conjunto de entrenamiento y en el conjunto completo, observando el
decaimiento del coeficiente en este último respecto del primero. Al
respecto, se obtuvieron los siguientes resultados.

-   R$^2$ en el conjunto de prueba: 1.0

-   R$^2$ en el conjunto completo: 0.9936

De lo anterior, se observa un pequeño decaimiento en el valor del
coeficiente, lo que demuestra una gran precisión del modelo elaborado.

Para mejorar el desempeño del modelo se sugiere obtener una mayor
cantidad de observaciones pues, aunque el desempeño del modelo se
muestra excepcional, su comportamiento se podría volver inestable en un
entorno real, dada la pequeña cantidad de datos usadas en su
entrenamiento.

En la figura 1 se muestra un gráfico comparativo de los
precios reales de los vehículos contra sus precios predichos por el
modelo.

![Precios Reales vs Predichos](https://github.com/nicomu97/Fundamentos-Ingenieria-Datos/blob/main/M%C3%B3dulo%206/L6/Imagenes/real_vs_predicho.png)

Figura 1: Comparación entre precios reales vs precios predichos.

# Conclusiones

La etapa de validación de un modelo es fundamental para asegurar la
calidad de sus predicciones y, por extensión, la calidad del servicio
ofrecido. Si no se evalúa el modelo, tanto en la etapa de desarrollo
como en producción, es imposible determinar si el modelo se adecúa a las
necesidades del problema que se está resolviendo, y puede caer
rápidamente en la obsolescencia sin que nos demos cuenta.

Por lo tanto, la elección de métricas de evaluación, así como el proceso
mismo de evaluación del modelo son parte fundamental del ciclo de vida
de un modelo de aprendizaje de máquina.
