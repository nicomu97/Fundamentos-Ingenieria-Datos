# Resumen Ejecutivo

La empresa DataStream Analytics S.A. se dedica a ofrecer servicios de
análisis de datos para empresas del sector financiero. Recientemente,
uno de sus clientes más importantes les solicitó generar reportes
diarios sobre movimientos financieros de sus usuarios, información que
proviene de diferentes sucursales distribuidas en todo el país. Estos
datos llegan en archivos grandes, con millones de registros que deben
ser procesados rápidamente para detectar patrones sospechosos y prevenir
fraudes.

Hasta el momento, la empresa utilizaba un sistema de procesamiento local
para este análisis, pero el volumen creciente de datos ha vuelto el
proceso lento y poco escalable. Por ello, el equipo de tecnología
decidió migrar a una solución basada en procesamiento distribuido con
Apache Spark.

Dado lo anterior, en nuestro rol de ingeniero de datos se nos ha
solicitado diseñar y explicar una solución utilizando Apache Spark,
aplicando los conceptos de RDD, transformaciones y acciones, para
procesar archivos de manera distribuida, rápida y eficiente, asegurando
la escalabilidad y la tolerancia a fallos. En particular, se nos ha
solicitado completar las siguientes tareas:

1.  Explicar cómo crearía un RDD a partir de archivos de datos
    recibidos.

2.  Proponer al menos tres transformaciones que aplicaría sobre el RDD
    para preparar datos.

3.  Identificar al menos dos acciones que utilizaría para obtener
    resultados concretos y generar los reportes solicitados.

4.  Describir brevemente qué será un Job Spark dentro de este contexto.

5.  Reflexionar y responder:

    -   ¿Por qué es importante el procesamiento distribuido en este
        caso?

    -   ¿Qué desafíos técnicos podría enfrentar el equipo al implementar
        esta solución?

# Análisis del caso

Una vez configurada la conexión con el clúster, la cual dependerá del
gestor de clúster utilizado, se debe crear un RDD para acceder al
archivo con datos a través de Spark. Para ello, usando la implementación
PySpark de Python, creamos una sesión usando la clase SparkSession, para
luego crear el RDD usando el método textFile de la clase SparkContext,
usando la ruta del archivo como argumento.

De esta forma, los datos contenidos en el RDD son distribuidos en
particiones que se almacenan en los nodos del clúster.

En cuanto a las transformaciones a aplicar, en primer lugar es útil
considerar la transformación filter, pues permite seleccionar elementos
del RDD que cumplan una determinada condición. De esta forma, podemos
seleccionar solo los datos que necesitaremos para el análisis o proceso
en cuestión.

Otra transformación útil sería map, que aplica una función a cada
elemento del RDD y devuelve un nuevo RDD como resultado. Así, podemos
aplicar transformaciones para preparar el RDD para un modelo de
aprendizaje de máquina, o realizar un proceso de limpieza y validación
de datos usando dicha transformación.

Por último, la transformación union nos permite combinar dos RDD, lo que
nos permitiría enriquecer los datos extraídos.

Por otro lado, para obtener resultados concretos de análisis, acciones
relacionadas con métricas estadísticas, como sum, min y stdev, nos
permitirán obtener métricas estadísticas y distribucionales de nuestros
datos. En este sentido, la acción top nos permitiría obtener, por
ejemplo las transacciones de mayor valor, y determinar se escapan de un
rango de valores basado en las métricas estadísticas mencionadas
anteriormente.

En este contexto, un Job Spark sería la tubería de datos, con
operaciones optimizadas, que involucra todas las transformaciones
acciones que se ejecutan sobre uno o más RDD, hasta generar reporte útil
para el cliente. Por ejemplo, sería el conjunto de operaciones
ejecutadas para determinar si una transacción corresponde o no a un
fraude.

# Conclusiones

El procesamiento distribuido es esencial para cualquier proceso que
requiera la manipulación de un gran volumen de datos de forma rápida y
eficiente. En el caso estudiado, podría significar la diferencia entre
lograr o no prevenir un potencial fraude de manera oportuna. De esta
forma, el procesamiento distribuido es una capa fundamental para generar
confianza entre la empresa y sus clientes, y así evitar pérdidas
financieras a sus clientes.

Sin embargo, la implementación de una solución que usa este tipo de
tecnología involucra varios desafíos técnicos. Por un lado, se debe
escoger una configuración de clúster que permita generar una conexión
adecuada y eficiente con la capa de almacenamiento distribuido. Por otro
lado, se deben crear tuberías de datos eficientes, que permitan obtener
el resultado deseado sin ejecutar operaciones innecesarias, de forma que
se aproveche al máximo las capacidades de la herramienta para optimizar
el flujo de trabajo.
