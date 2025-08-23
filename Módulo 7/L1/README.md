# Resumen Ejecutivo

La empresa MarketTrend S.A., especializada en análisis de comportamiento
de consumidores, ha detectado que sus sistemas actuales de análisis no
son capaces de procesar la gran cantidad de datos que reciben
diariamente desde redes sociales, registros de compras, aplicaciones
móviles y encuestas online. Esto ha generado problemas para identificar
tendencias en tiempo real y ofrecer recomendaciones personalizadas a sus
clientes.

Dado lo anterior, en nuestro rol como analistas de datos, se nos ha
solicitado proponer una solución tecnológica basada en Big Data que
permite a la empresa capturar, almacenar, procesar y analizar la
información proveniente de múltiples fuentes, garantizando la eficiencia
y escalabilidad de la solución.

En particular, se nos nos solicita realizar las siguientes tareas:

1.  Analizar la situación inicial y describir cuáles de las 5V's de Big
    Data están presentes en este escenario y por qué.

2.  Proponer una arquitectura Big Data básica para MarketTrend,
    identificando:

    -   Qué tecnologías utilizarías para la adquisición de datos.

    -   Qué sistema de almacenamiento distribuido sería más adecuado.

    -   Qué herramientas de procesamiento distribuirías y por qué.

3.  Mencionar al menos tres beneficios que obtendría la empresa tras la
    implementación de la solución.

4.  Reflexionar y responder:

    -   ¿Qué riesgos o desafíos podría enfrentar la empresa al
        implementar esta solución?

    -   'Qué medidas recomendarías para garantizar la seguridad y
        calidad de los datos?

# Análisis del caso

Basándonos en el escenario que se presenta, se observa que se encuentran
presentes todas las 5V's de Big Data:

-   Volumen: Dadas las fuentes desde las que MarketTrend recopila datos,
    esta necesita almacenar grandes cantidades de datos en tiempo real.
    Las redes sociales generan miles de comentarios por segundo, y se
    pueden registrar miles de comprar también en un período muy acotado
    de tiempo.

-   Velocidad: Se menciona que los clientes de MarketTrend requiere de
    análisis en tiempo real para poder proveer de recomendaciones
    adecuados a sus usuarios e identificar tendencias en tiempo real.

-   Variedad: El hecho que se extraiga información de fuentes muy
    diversas, como redes sociales, registros de compras y aplicaciones
    móviles, que además generan datos no estructurados, implica que
    dicha información viene en una gran variedad de formatos.

-   Veracidad: Dado que estos datos se usarán para realizar análisis, se
    requiere que estos sean precisos y relevantes, para que estos
    análisis sean confiables.

-   Valor: Nuevamente, el hecho que estos datos se usen en análisis que
    resultan esenciales para los clientes demuestra que estos poseen un
    valor inmenso.

En cuanto a la arquitectura Big Data básica para resolver este problema,
se propone implementar un sistema que utilice una base de datos NoSQL
basada en columnas, como Cassandra, para el almacenamiento y adquisición
de datos de estas fuentes diversas. Cassandra permitirá extraer datos
para analizarlos en tiempo real de manera rápida y eficiente, pues esta
está optimizada para dicha tarea.

Por otro lado, se propone implementar un sistema de almacenamiento
distribuido usando la tecnología HDFS, lo cual permitirá almacenar los
datos en más de un nodo, permitiendo escalar horizontalmente el sistema
de base de datos propuesto, haciéndolo adaptable al creciente volumen de
datos que procesa la empresa.

Por último, se propone implementar la herramienta Apache Kafka para el
procesamiento de datos en tiempo real. De esta forma, es posible generar
recomendaciones personalizadas a los clientes e identificar tendencias,
todo ello en tiempo real, que es uno de los requerimientos de la
empresa.

Así, la arquitectura mencionada permitirá a la empresa almacenar y
extraer datos de forma eficiente y optimizada para su caso de uso,
escalar el sistema de almacenamiento agregando más nodos cuando sea
necesario, y permitirá analizar dichos datos en tiempo real, de acuerdo
con las necesidades de la empresa.

Sin embargo, la implementación de dicha arquitectura también implica
algunos desafíos. Por un lado, dado el ecosistema de datos actual de la
empresa, podría resultar complejo ejecutar la migración entre ambos
sistemas, representando un desafío técnico importante. Además, si no se
implementan controles de calidad y seguridad de los datos, no es posible
asegurar que los análisis realizados usando esta arquitectura sean
confiables.

Considerando lo anterior, se recomienda implementar una capa de acceso y
consulta de datos, para a los usuarios acceso a información relevante, a
la vez que se impide el acceso no autorizado. Adicionalmente, se
recomienda implementar un sistema de validación de datos, que permita
implementar reglas del negocio a los datos almacenados, y verificar que
se cumple con las métricas de calidad de datos fijadas por la empresa.

# Conclusión

La implementación de una arquitectura de datos adecuada permite a las
empresas extraer información valiosa para estas de datos con gran
variedad de formatos y en gran volumen. Esta resulta esencial para
asegurar la escalabilidad y adaptabilidad del sistema y que la
información relevante es entregada en lapsos de tiempo prudente, en
particular si dicha información se debe entregar en tiempo real.
