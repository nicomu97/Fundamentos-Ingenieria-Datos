# Resumen Ejecutivo

Una empresa tecnológica en crecimiento ha decidido mejorar su
infraestructura de almacenamiento de datos para soportar una cantidad
creciente de clientes y transacciones. La empresa actualmente utiliza
bases de datos relacionales para almacenar información, pero con el
incremento de clientes y operaciones, las consultas tardan más en
ejecutarse y los costos de mantenimiento van al alza.

En nuestro rol de arquitectos de bases de datos, tras analizar
detenidamente el problema y examinar las posibles soluciones, se ha
determinado que la mejor solución es migrar a una base de datos NoSQL en
Cassandra y escalarlo horizontalmente junto con el negocio.

# Análisis del caso

En la situación actual, la empresa presenta problemas de degradación del
rendimiento del sistema de bases de datos, lo que ha traído como
consecuencia la pérdida de velocidad en la ejecución de consultas y el
aumento en los costos de mantenimiento.

La degradación antes mencionada se produce a causa de un aumento en el
volumen de datos que se debe procesar. Dado que la capacidad de
procesamiento de información está limitada por el sistema de
almacenamiento de datos y hardware actuales, este problema seguirá
empeorando a medida que el negocio vaya escalando. En este sentido, la
solución debe ser capaz de escalar junto con la empresa y adaptarse a
los cambios que este crecimiento conlleve.

Tomando en consideración lo anterior, tenemos dos posibilidades
generales que es posible implementar para este caso. La primera es
escalar verticalmente el servidor ya existente, lo cual implica ampliar
la capacidad del servidor existente contratando más capacidad de
procesamiento. Esta solución puede resultar menos costosa en el corto
plazo, sin embargo, esta opción está limitada en el largo plazo por las
capacidades tecnológicas actuales y el espacio físico que puede ocupar
el servidor.

Una segunda posibilidad considera el escalamiento horizontal a través de
la contratación de nuevos servidores, de forma que la capacidad de
procesamiento se pueda distribuir a lo largo de cada uno de los nodos
contratados. Esta opción suele ser más costosa, pero para nuestro caso,
en que la empresa se encuentra en constate crecimiento, sería una
solución más sostenible en el largo plazo. Por lo tanto, esta opción
sería más adecuada para nuestro caso de uso.

A continuación, es necesario considerar la tecnología a través de la
cual se implementaría este escalamiento horizontal. Una tecnología de
base de datos relacionales, nos permitiría una integración sencilla con
el sistema de datos actual, ya que este ya utiliza una tecnología de
almacenamiento de datos SQL. Esto también nos permitiría realizar
consultas complejas de manera eficiente, pero su estructura rígida le
impediría a la base de datos adaptarse a cambios repentinos.

En el mundo de las bases de datos relacionales, hay tres opciones
populares que nos permitirían escalar horizontalmente nuestro sistema de
almacenamiento de datos: MySQL, PostgreSQL y SQL Server.

Por un lado, MySQL es una opción gratuita de código abierto que nos
permite particionar la base de datos a lo largo de diverso nodos usando
funciones de hashing. Esto nos permite definir a ubicación de los datos
a partir de claves de partición, evitando cuellos de botella y
simplificando la mantención.

Por otro lado, PostgreSQL es otra opción gratuita de código abierto que
puede crear índices de partición para distribuir los datos. Esto, sin
embargo, requiere definir manualmente dichos índices, lo que complejiza
el mantenimiento de la base de datos.

Finalmente, SQL Server es una herramienta comercial que nos permite
contratar nuevos servidores directamente, con un costo asociada a cada
nuevo servidor. Esta opción nos permite asignar automáticamente una
partición a los valores que caigan en un rango determinado, asignando
nuevas particiones a los datos que queden fuera de dicha umbral. Esto
permite automatizar el proceso de particionamiento y simplifica el
mantenimiento de la base de datos.

Cabe mencionar que, en el caso de las opciones gratuitas, de igual
manera es necesario contratar los servidores correspondientes, por lo
que este se podría considerar un costo común de todas las opciones
mencionadas. Considerando esto, SQL Server sería la mejor opción en la
categoría de bases de datos relacionales, en términos de costos y
eficiencia.

Ahora bien, en el mundo de las bases de datos NoSQL también existen
varias alternativas que nos permitirían distribuir los datos en varios
servidores. De hecho, estas alternativas están diseñadas en torno a este
concepto, por lo que su implementación tiende a ser más eficiente que
con bases de datos SQL. Sin embargo, es necesario tomar en cuenta que es
más complejo migrar desde una base SQL a una NoSQL, lo que podría
introducir costos adicionales.

En particular, está Cassandra, un administrador de base de datos basado
en columnas, gratuita y de código abierto. Este modelo de bases de datos
permite almacenar datos en columnas, permitiendo consultas eficientes
para extraer datos. Cassandra permite adaptar el nivel de consistencia
para balancear esta con la velocidad de consulta. Sin embargo, podría
volverse ineficiente para el caso de consultas complejas.

Dada la necesidad de escalamiento del negocio junto con una mejora del
desempeño actual, y tomando en cuenta el rápido crecimiento de la
empresa, lo que podría producir cambios abruptos en su estructura, a
largo plazo Cassandra se convierte en la mejor opción entre las
tecnologías analizadas, en términos de costo y eficiencia.

# Conclusión

El rápido crecimiento de la empresa y de su número de clientes exige la
migración a un sistema de base de datos NoSQL. Esto permitirá introducir
cambios a la base de datos cuando sea necesario y contratar nuevos nodos
cuando la capacidad actual no sea suficiente, convirtiéndose así en una
opción sostenible en el largo plazo.

En este sentido, Cassandra surge como una solución natural a este
problema. Sin embargo, hay que considerar que la migración desde una
base de datos SQL a una NoSQL podría introducir nuevos desafíos, dado
que ambos conceptos giran en torno a paradigmas distintos.
