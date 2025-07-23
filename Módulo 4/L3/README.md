# Resumen Ejecutivo

Una empresa de servicios de streaming ha experimentado un crecimiento
exponencial en su base de usuarios y contenido multimedia. Actualmente
usan una base de datos relacional para almacenar información de
usuarios, historial de reproducción y recomendaciones personalizadas,
pero dado su actual crecimiento, ha detectado una disminución en la
velocidad de ejecución de las consultas a la base de datos, y que
escalar horizontalmente dicha base de datos sería costoso y complejo.

Debido a lo anterior, el equipo de tecnología está considerando migrar a
una base de datos NoSQL para mejorar el rendimiento y la escalabilidad
del sistema, y se solicita determinar que tipo de base de datos NoSQL es
más adecuada para nuestro caso de uso.

Dada la naturaleza del servicio prestado y las ventajas respecto a esto
que poseen los modelos basados en columnas, se recomienda migrar el
sistema de base de datos a Cassandra.

# Análisis del caso

De acuerdo a lo señalado, el rápido crecimiento de la empresa ha
provocado que su base de datos ralentice su velocidad de ejecución. Esto
se debe a las limitaciones de las bases de datos relacionales: al estar
diseñadas para mantener la consistencia de los datos, estas pueden
bloquear el acceso a los datos cuando estos se están actualizando, y los
liberan una vez termina de ejecutarse la actualización. Esto introduce
un período de latencia por operación, el cual se vuelve significativo
cuando se ejecutan muchas consultas en poco tiempo.

Para solucionar este problema, y que la solución sea fácil de escalar
horizontalmente, se determina que se debe migrar a un modelo de base de
datos NoSQL para asegurar la disponibilidad de los datos, y que la
ejecución de una gran cantidad de consultas no afecte el desempeño de la
base de datos.

A continuación, se realiza un análisis de los modelos de bases de datos
NoSQL existentes, señalando sus ventajas y desventajas para el caso de
uso actual.

## Modelos Clave-Valor

Este modelo es simple y entrega una alta eficiencia para la recuperación
rápida de datos. Notar, sin embargo, que en el modelo de negocios
también se escribe mucha información: cada vez un usuario visualiza
contenido, esta acción se añade a su historial, y de la misma forma las
recomendaciones personalizadas pueden ir cambiando en el tiempo,
dependiendo de lo que el usuario haya visualizado. Por lo anterior, esta
podría no ser la mejor opción para nuestro caso.

## Modelos Orientados a Documentos

Con este tipo de modelo de base de datos, es posible almacenar datos en
documentos de formato JSON o BSON, lo que permite estructuras flexibles
y fáciles de modificar, así como consultar datos de manera eficiente.

A pesar de lo anterior, la generación de recomendaciones personalizadas
requiere análisis de grandes cantidades de datos en tiempo real, tarea
para la cual este tipo de base de datos podría no ser la más adecuada.

## Modelos Orientados a Columnas

Este modelo está optimizado para manejar grandes volúmenes de datos en
entornos de análisis y procesamiento masivo, lo que lo hace ideal para
consultas que involucran agregación y análisis a gran escala. Dado que
la generación de recomendaciones en plataformas de streaming requiere
analizar grandes volúmenes de datos en tiempo real, este modelo de base
de datos sería el más adecuado para el caso de uso.

## Modelos Orientados a Grafos

Están diseñados para modelar relaciones complejas entre entidades,
utilizando nodos para representar conexiones. Dado que nuestro caso de
uso busca analizar el comportamiento de un solo usuario en tiempo real,
más que la relación entre usuarios, este modelo es poco adecuado para
nuestro caso.

# Conclusión

Tomando en cuenta todo lo anterior, migrar a un modelo columnar, en
particular a Cassandra, surge como la decisión natural para nuestro caso
de uso. Su capacidad de almacenar y realizar consultas de manera
eficiente, y su modelo orientado a la disponibilidad de datos con la
posibilidad de escalamiento horizontal, lo convierte en una excelente
opción para nuestro caso, en el cual se obtienen datos en tiempo real de
los usuarios.

Además, dado que la generación de recomendaciones personalizadas para
cada usuario requiere el análisis de grandes volúmenes de datos en
tiempo real, los modelos orientados a columnas resalta naturalmente en
este ámbito, pues está optimizado para el análisis de big data.

Considerando que Cassandra es una tecnología de bases de datos gratuita
y de código abierto, con una gran comunidad de usuarios, surge como la
elección ideal de tecnología para nuestro caso. Adicionalmente, dado que
su lenguaje de consultas, CQL, es similar al lenguaje de consultas que
usa la tecnología actual utilizada por la empresa, SQL, hace que el
proceso de migración sea más sencillo comparado con otras alternativas
NoSQL. Sin embargo, dado que Cassandra trabajo en torno a conceptos
distintos a los utilizados por bases de datos relacionales, esto podría
requerir ejecutar capacitaciones a los trabajadores de la empresa, en
especial a aquellos acostumbrados a realizar consultas SQL.
