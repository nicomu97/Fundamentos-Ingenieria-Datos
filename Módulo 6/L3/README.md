# Resumen Ejecutivo

La empresa RetailData Analytics, dedicada a ofrecer soluciones basadas
en datos para comercios minoristas, ha sido contratada por una cadena de
supermercados para desarrollar un modelo predictivo que identifique el
perfil de los clientes más propensos a realizar compras recurrentes.

Durante la fase inicial del proyecto, el equipo de ciencia de datos ha
recibido un conjunto de datos que contiene información demográfica y de
comportamiento de los clientes. Sin embargo, al analizar los datos,
identificaron problemas como valores nulos, variables categóricas no
codificadas y diferencias significativas en escala de las variables
numéricas.

La empresa, en nuestro rol de especialista en preparación de datos, nos
ha solicitado realizar un proceso completo de preprocesamiento y
escalamiento de datos. En particular, se nos solicita realizar las
siguientes tareas:

1.  Analizar el fragmento de datos en la siguiente tabla, proporcionados por el
    cliente

      |ID  | Edad  | Ciudad     | Ingresos (USD)
      |----| ------| -----------| ----------------
      |1   | 25    | Madrid     | 30000
      |2   | 45    | Sevilla    | 50000
      |3   | 30    | Madrid     | NaN
      |4   | 40    | Barcelona  | 40000


2.  Realizar las siguientes tareas usando Python y Scikit-Learn:

    -   Imputar el valor faltante en la columna Ingresos usando la
        media.

    -   Transformar la columna Ciudad utilizando Label Encodig y One-Hot
        Encoding.

    -   Aplicar el método de Variables Dummy para la columna Ciudad.

    -   Escalar las columnas Edad e Ingresos usando:

        -   Normalización Min-Max.

        -   Estandarización Z-Score.

3.  Reflecionar y responder brevemente:

    -   ¿Por qué es importante realizar estas tareas antes de entrenar
        un modelo de Machine Learning?

    -   ¿Qué diferencias observaste entre la normalización y
        estandarización?

# Análisis del caso

Al realizar una inspección inicial de los datos entregados por el
cliente, se detectan varios problemas relativos a su uso en modelos de
aprendizaje de máquina:

1.  La variable Ciudad no está codificada. Dado que los modelos de
    machine learning utilizan datos exclusivamente numéricos para
    realizar estimaciones, este problema es un impedimento grave para
    realizar dicha tarea.

2.  De forma similar, la columna Ingresos tiene un dato perdido, lo que
    nuevamente es un impedimento para usar este conjunto de datos en un
    modelo de aprendizaje de máquina.

3.  Se nos entrega la columna ID, la cual no es útil para la tarea de
    estimaciones.

4.  Finalmente, se detecta una diferencia significativa de escala entre
    las variables Edad e Ingresos, lo cual podría sesgar algunos modelo
    de aprendizaje automático, dándole gran importancia al uso de la
    variable ingresos.

Tomando lo anterior en cuento, debemos preparar estos datos para que
sean utilizables por cualquier algoritmo de aprendizaje de máquina que
se desea utilizar. A continuación, se adjuntan imágenes del proceso
realizado.

![Datos originales.](https://github.com/nicomu97/Fundamentos-Ingenieria-Datos/blob/main/M%C3%B3dulo%206/L3/Imagenes/Datos_originales.png){#fig:datos-originales}

![Datos imputados.](https://github.com/nicomu97/Fundamentos-Ingenieria-Datos/blob/main/M%C3%B3dulo%206/L3/Imagenes/Datos_imputados.png){#fig:datos-imputados}

![Datos con columna Ciudad codificada con Label
Encoder.](https://github.com/nicomu97/Fundamentos-Ingenieria-Datos/blob/main/M%C3%B3dulo%206/L3/Imagenes/Datos_label_encoded.png){#fig:datos-label-encoded}

![Datos con columna Ciudad codificada con One-Hot
Encoder.](https://github.com/nicomu97/Fundamentos-Ingenieria-Datos/blob/main/M%C3%B3dulo%206/L3/Imagenes/Datos_onehot_encoded.png){#fig:datos-onehot-encoded}

![Datos con columna Ciudad transformada con variables
Dummy.](https://github.com/nicomu97/Fundamentos-Ingenieria-Datos/blob/main/M%C3%B3dulo%206/L3/Imagenes/Datos_dummy.png){#fig:datos-dummy}

![Datos con columnas Edad e Ingresos escalados con método
Min-Max.](https://github.com/nicomu97/Fundamentos-Ingenieria-Datos/blob/main/M%C3%B3dulo%206/L3/Imagenes/Datos_escalados_minmax.png){#fig:datos-escalados-minmax}

![Datos con columnas Edad e Ingresos escalados con método
Z-Score.](https://github.com/nicomu97/Fundamentos-Ingenieria-Datos/blob/main/M%C3%B3dulo%206/L3/Imagenes/Datos_escalados_zscore.png){#fig:datos-escalados-zscore}

# Conclusiones

Las tareas de preprocesamiento de datos es un paso esencial antes de
entrenar un modelo de aprendizaje de máquina. Este proceso permite
asegurar que los datos estén en un formato que la máquina pueda
comprender, asegura la calidad de los datos para asegurar estimaciones
precisas y permite explicitar información para el modelo, facilitando su
entrenamiento y eliminando sesgos.

En particular, el escalamiento de datos permite evitar que una variable
domine por sobre las otras en el modelo solo por tener un orden de
magnitud mayor. En particular, el método Min-Max nos permite fijar los
valores de las variables en un intervalo determinado (en nuestro, entre
0 y 1, como muestra la figura
[6](#fig:datos-escalados-minmax){reference-type="ref"
reference="fig:datos-escalados-minmax"}), mientras que el método Z-Score
nos permite fijar la varianza de las variables en 1, y sus promedios en
0, como muestra la figura
[7](#fig:datos-escalados-zscore){reference-type="ref"
reference="fig:datos-escalados-zscore"}.
