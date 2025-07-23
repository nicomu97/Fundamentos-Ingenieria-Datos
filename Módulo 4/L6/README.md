# Resumen Ejecutivo

Una empresa de comercio electrónico ha experimentado un crecimiento
acelerado de su base de clientes y volúmenes de pedidos. Esto ha
producido que la base de datos relacional que actualmente utilizan
presente problemas de rendimiento ante grandes volúmenes de pedidos
simultáneos, provocando latencias en las respuestas y afectando
negativamente la experiencia del usuario.

Debido a lo anterior, el equipo de tecnología está evaluando Amazon
DynamoDB como una alternativa para mejorar la escalabilidad y
disponibilidad del sistema de gestión de pedidos.

En este documento se presenta un análisis detallado de como migrar a
Amazon DynamoDB puede mejorar la situación actual de esta empresa.

# Análisis del caso

Como se mencionó anteriormente, la tecnología de bases de datos
actualmente utilizada por esta empresa se está viendo sobrepasada por el
nivel de crecimiento que presenta. Dado que las bases de datos
relacionales están diseñadas para mantener una consistencia fuerte,
produce que se forme una cola de consultas cuando se realizan pedidos
simultáneos, solamente liberando los datos a nuevas consultas cuando la
actual ya fue procesada. Esto produce una alta latencia cuando se
procesan grandes cantidades de pedidos, reduciendo la disponibilidad de
los datos.

El problema señalado persistiría incluso si se intenta escalar la base
de datos, ya sea horizontal o verticalmente, ya que la base de datos
relacional intentará asegurar la consistencia a lo largo de todos los
nodos disponibles, y la mejora y/o expansión del nodo actual está
limitado por la tecnología actual y restricciones de espacio físico.

Al migrar a una base de datos NoSQL, es posible escalar horizontalmente
las bases de datos de manera rápida y sencilla, aumentando la
disponibilidad de los datos para todos los usuarios reduciendo la
consistencia.

En el caso de DynamoDB, esta tecnología nos permite omitir el
mantenimiento de la base de datos, dado que Amazon se hace cargo de la
mantención de su infraestructura, y se puede aumentar o reducir el
almacenamiento utilizado de manera dinámica, reduciendo costos al
liberar espacio que no se está utilizando.

Aunque DynamoDB tiene restricciones de tamaño de los documentos que se
pueden almacenar, y tiene un costo un poco más elevado que otras
alternativas, el hecho que una base de datos relacional ya no sea
suficiente para la empresa es un indicativo de que el tamaño de esta
permitiría costear los costos mencionados, y dado que trabajo con
transacciones comerciales, las limitaciones de espacio no debieran ser
un problema.

Cabe mencionar que, como se sacrifica la consistencia para aumentar la
disponibilidad de los datos, podrían producirse problemas, por ejemplo,
al actualizar el inventario de un producto, por lo que el cliente podría
terminar solicitando un producto que ya no está disponible. Teniendo
esto en cuenta, la empresa deberá tomar esto en cuenta antes de migrar a
DynamoDB.

En cuanto al diseño mismo de la base de datos, dado que esta almacenará
información sobre pedidos, se debe almacenar al menos el listado de
productos solicitados con la cantidad de unidades vendidas. Cada pedido
debe estar asociado a un ID de pedido, para poder buscar pedidos
específicos, así como la fecha y hora en que se realizó el pedido.

Tomando en cuenta lo anterior, se configurará el ID de pedido como una
clave primaria simple. Por otro lado, dado que la fecha de solicitud del
pedido se espera que sea frecuentemente consultada y es independiente a
la clave primaria, se aconseja configurarla como un índice secundario
global, para así generar consultas eficientes utilizando este atributo.

Por otro lado, como estrategia de optimización y escalabilidad, se
recomienda utilizar la capacidad de autoescalado que viene por defecto
configurado en DynamoDB, pues dado que la empresa trabaja en el rubro
del comercio, es esperable que tenga flujos cambiantes de volúmenes de
transacciones.

Por último, es necesario considerar la posibilidad de integrar la base
de datos con servicios de AWS como Sagemaker, para la producción de
modelos de aprendizaje de máquina para la generación de recomendaciones,
Lambda para la administración de eventos relacionados con las compras, y
API Gateway para la construcción de APIs.

# Conclusión

Dadas las necesidades actuales de la empresa, así como sus proyecciones
futuras, AWS DynamoDB resulta ser una herramienta ideal para resolver el
problema actual de almacenamiento y procesamiento de datos. Su capacidad
de escalar horizontalmente de manera dinámica permite adaptarse a flujos
de datos cambiantes, y su orientación a documentos permite almacenar
datos semi-estructurados de manera eficiente. Al realizar un diseño
eficiente de tablas de datos permitirá sacarle el máximo provecho a esta
herramienta.
