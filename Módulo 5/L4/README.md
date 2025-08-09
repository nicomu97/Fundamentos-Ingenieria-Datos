# Resumen Ejecutivo

La empresa de retail Mercato busca mejorar su sistema de análisis de
datos. Actualmente, sus reportes están basados en consultas sobre su
base de datos transaccional (OLTP), lo cual genera lentitud en las
consultas y complejidad para los analistas.

Tomando en cuenta lo anterior, se ha propuesto implementar un modelo
multidimensional para soportar el análisis histórico de ventas,
comportamiento de clientes y desempeño de productos, por lo que se ha
encargado al equipo de datos diseñar un esquema optimizado para
consultas OLAP que facilite la generación de reportes, dashboards y
proyecciones.

En ese contexto, en nuestro rol como analistas de datos, se nos ha
solicitado ejecutar las siguientes tareas:

1.  Análisis de contexto

    -   Describir porque una base OLTP no es ideal para análisis
        complejos y cómo un modelo OLAP puede aportar valor en este
        caso.

    -   Identificar las principales entidades del negociio (ventas,
        productos, tiendas, fechas, clientes) y clasificar cuales serían
        hechos y cuales dimensiones.

2.  Diseño del modelo multidimensional

    -   Diseñar un esquema estrella que represente el proceso de ventas,
        incluyendo al menos una tabla de hechos con métricas clave:
        monto de venta, cantidad, descuentos; y cuatro tablas de
        dimensiones: tiempo, cliente, producto y tienda.

    -   Mostrar el esquema con un diagrama.

3.  Jerarquías y agregaciones

    -   Definir jerarquías dentro de las dimensiones.

    -   Proponer al menos dos formas de agregaciones útiles para el
        análisis de negocio

4.  Buenas prácticas de diseño

    -   Justificar el uso de un esquema estrella frente al copo de
        nieve.

    -   Reflexionar sobre la decisión de normalizar o desnormalizar
        dimensiones.

    -   Explicar como estas prácticas impactan en el rendimiento de las
        consultas.

5.  Casos de uso

    -   Redactar tres consultas típicas que el modelo debería consultar.

# Análisis del caso

Las bases de datos OLTP están enfocados en la consistencia y la
precisión de los datos y, por tanto, están optimizadas para la
escritura, construyéndose en torno a tablas normalizadas para asegurar
dichas propiedades. Esto sin embargo produce que consultas orientadas a
la extracción de datos sean lentas y complejas, dada la gran cantidad de
operaciones Join que es necesario ejecutar para recuperar dicha
información.

Las bases de datos OLAP, en cambio, están optimizadas para el análisis,
trabajando en torno a tablas desnormalizadas que se actualizan
periódicamente. Esto permite reducir la complejidad de las consultas de
extracción de datos al requerir menos operaciones para recuperar la
información necesaria.

Dado lo anterior, el diseño de una base de datos OLAP es ideal para
resolver la problemática actual de la empresa, dado que está optimizada
para la ejecución de operaciones analíticas.

En cuanto a las entidades que incluirá esta base de datos, se mencionó
anteriormente que Mercato realiza análisis históricos de ventas,
comportamiento de clientes y desempeño de productos, por lo que la base
de datos OLAP debe incluir, como mínimo, las entidades clientes, ventas
y productos. Adicionalmente, la empresa probablemente posea varias
tiendas en diversas regiones y países, por lo que es importante incluir
la entidad tiendas en el diseño. Por último, es importante tener
información de la fecha en que se ejecutó una venta para facilitar el
análisis de desempeño de productos, por lo que es necesario incluir la
entidad fecha en el diseño como una tabla desnormalizada.

En síntesis, se incluirán las entidades clientes, ventas, productos,
tiendas y fechas en el diseño de la base de datos OLAP. Dado que las
necesidades de la empresa consisten principalmente mejorar el
rendimiento de consultas analíticas, más que la reutilización de los
datos, y dado que ya posee una base de datos OLTP para asegurar la
consistencia de los datos, las tablas se diseñarán en torno a un esquema
estrella con tablas desnormalizadas.

En base a lo anterior, a continuación se muestra el diagrama
entidad-relación correspondiente al diagrama estrella de este modelo de
datos.

![image](Diagramas/L4_diagrama_er){width="\\textwidth"}

Dicho esquema consiste en las siguientes tablas:

1.  Ventas: Tabla de hechos que contiene los ids de las entidades
    relacionadas a cada venta, así como métricas básicas asociadas a
    cada venta, y cuenta con los siguientes atributos:

    -   id_venta: Identificador único asociado a la venta. Actúa como
        llave primaria de esta tabla.

    -   id_tienda: Clave foránea correspondiente al identificador de la
        tienda donde se ejecutó la venta.

    -   id_producto: Clave foránea correspondiente al identificador del
        producto vendido.

    -   id_cliente: Clave foránea correspondiente al identificador del
        cliente que compró el producto.

    -   id_fecha: Clave foránea correspondiente al identificador de la
        fecha en que se ejecutó la venta.

    -   monto_venta: Valor neto de la venta.

    -   cantidad: Cantidad de unidades de producto vendidos.

    -   descuentos: Descuentos asociados al producto en el momento de la
        venta.

2.  Tiendas: Tabla de dimensiones que contiene información de cada
    tienda que posee Mercato, incluyendo información de la ubicación
    superficie que ocupa cada tienda.

    -   id_tienda: Clave primaria correspondiente al identificador único
        de cada tienda.

    -   pais: País en el que se ubica la tienda.

    -   region: región geográfica del país donde se ubica la tienda.

    -   ciudad: Ciudad en la que se ubica la tienda.

    -   dirección: Dirección dentro de la ciudad donde se ubica la
        tienda.

    -   superficie: m$^2$ construidos que ocupa la tienda.

    -   latitud, longitud: ubicación geográfica de la tienda.

3.  Productos: Tabla de dimensiones que modelo la entidad productos y
    contiene la información básica de cada producto.

    -   id_producto: Clave primaria correspondiente al identificador
        único de cada producto.

    -   sku: Código SKU del producto.

    -   categoría: Categoría a la cual pertenece el producto.

    -   marca: Marca del producto.

    -   precio: Precio actual del producto.

    -   nombre: Nombre asignado al producto.

    -   descripción: Descripción que detalla las características del
        producto.

4.  Clientes: Tabla de dimensiones que detalla información básica de los
    clientes.

    -   id_cliente: Clave primaria que corresponde al identificador
        único asignado a cada cliente.

    -   rut: RUT del cliente.

    -   nombre, apellido: Nombre y apellido del cliente.

    -   direccion: dirección ingresada por el cliente.

5.  Fechas: Tabla de dimensiones detallando información de cada fecha
    donde se ejecutó una venta.

    -   id_fecha: Clave primaria correspondiente al identificador
        asociado a cada fecha.

    -   año, mes, dia, hora, minuto, segundo: Valores correspondientes a
        la fecha.

    -   trimestre: Trimestre al cual pertenece la fecha, y corresponde a
        un valor del 1 al 4.

    -   nombre_mes, nombre_dia: Nombres del mes y día asociados a cada
        fecha.

Notar que, en el esquema anterior, se evidencian tres jerarquías de
datos:

-   Tabla Tiendas: País Región Ciudad Dirección

-   Tabla Productos: SKU Categoría Marca

-   Tabla Fechas: Año Mes Día Hora Minuto Segundo

Estas jerarquías permiten agilizar consultas agregadas respecto a
productos, zonas geográficas e intervalos de tiempo. En particular,
facilita las siguientes agregaciones:

-   Desempeño de un producto por zona geográfica.

-   Ingresos generados por las tiendas en el último año, por mes.

-   Productos más vendidos por categoría.

Por otro lado, dada recurrencia con la que esta información será
consultada para análisis, sería útil crear índices para dichos atributos
para acelerar consultas relacionadas a estos atributos. En particular
crear un índices de varias columnas para dicho propósito.

En este sentido, el modelo soportará, entre otras, las siguientes
consultas típicas:

-   Total de ventas por categoría y mes, en el último año:

                SELECT p.categoria, f.nombre_mes, SUM(v.monto_venta)
                FROM Ventas AS v
                LEFT JOIN Productos AS p ON v.id_producto=p.id_producto
                LEFT JOIN Fechas AS f ON v.id_fecha=f.id_fecha
                WHERE f.año=2025
                GROUP BY p.categoria, f.nombre_mes

-   Total de ventas por país y categoría, en el último año:

                SELECT t.pais, p.categoria, SUM(v.monto_venta)
                FROM Ventas AS v
                LEFT JOIN Productos AS p ON v.id_producto=p.id_producto
                LEFT JOIN Tiendas AS t ON v.id_tienda=t.id_tienda
                WHERE Fechas.año=2025
                GROUP BY p.categoria, t.pais

-   Unidades vendidas de producto por mes y región en Chile en el último
    año:

                SELECT t.region, f.nombre_mes, SUM(v.cantidad)
                FROM Ventas AS v
                LEFT JOIN Tiendas AS t ON v.id_tienda=t.id_tienda
                LEFT JOIN Fechas AS f ON v.id_fecha=f.id_fecha
                WHERE f.año=2025 AND t.pais="Chile"
                GROUP BY p.categoria, f.nombre_mes

# Conclusiones

El modelamiento de datos es un paso esencial para asegurar la eficiencia
de las operaciones en una empresa, tanto si el propósito de la base de
datos es mantener la consistencia de los datos almacenados, o realizar
consultas complejas para efectos de análisis.

Un diseño de esquema de base de datos eficiente y alineado con los
objetivos y la estrategia del negocio permite obtener rápidamente acceso
a la información necesaria para la toma de decisiones, a la vez que se
asegura la calidad de los datos extraídos.
