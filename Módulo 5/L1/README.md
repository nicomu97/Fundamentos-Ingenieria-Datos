# Resumen Ejecutivo

InfoHealth, una empresa del sector salud, ha experimentado un
crecimiento acelerado en la digitalización de sus procesos clínicos y
administrativos. Actualmente cuenta con múltiples fuentes de datos en
entornos compartidos: historias clínicas electrónicas, sensores IoT de
monitoreo remoto, formularios de pacientes, correos electrónicos y hojas
de cálculo. Sin embargo, no poseen una arquitectura de datos definida,
lo que ha generado problemas como duplicación de datos, falta de
trazabilidad, riesgos de seguridad y escasa integración entre áreas.

En este contexto, en nuestro rol de arquitecto de datos junior, nuestro
trabajo será realizar un diagnóstico inicial del estado de la
arquitectura de datos y proponer un plan de mejora basado en buenas
prácticas, principios de modelado y gobierno de datos, garantizando
accesibilidad, escalabilidad y seguridad. En particular, nuestras tareas
serán:

1.  Identificar y documentar los principales problemas actuales de la
    empresa respecto al manejo de datos.

2.  Proponer una arquitectura de datos base considerando las siguientes
    capas:

    -   Fuentes de datos.

    -   Almacenamiento (estructurado y no estructurado).

    -   Procesamiento y limpieza.

    -   Acceso y visualización.

    -   Seguridad y gobernanza.

3.  Especificar al menos dos herramientas que podrían implementarse en
    cada capa.

4.  Definir 3 principios clave de arquitectura (según DAMA BOK) para
    aplicar en el diseño.

5.  Justificar por qué esta arquitectura propuesta es escalable y
    adecuada para el sector salud.

6.  Crear un pequeño esquema visual o tabla resumen que detalle la
    solución propuesta.

# Análisis del caso

Antes de comenzar, es necesario comprender el contexto y las necesidades
de la empresa a analizar. En primer lugar, dado que es una empresa del
sector salud, los distintos departamentos deben tener acceso, cuando
corresponda, a datos clínicos del paciente, pues un mismo paciente
podría atenderse con distintos especialistas en distintos momentos, y
estos especialistas deben poder acceder a la información del paciente.
Esto también ocurre con otros tipos de datos, como sensores IoT, por lo
que debe existir alta accesibilidad de dicha información.

Por otro lado, información como historiales clínicos y correos
electrónicos son datos sensibles, por lo que se requiere resguardar
dicha información para que solo las personas autorizadas puedan acceder
a estos. Además, la información debe ser trazable, pues, por ejemplo, un
paciente y su médico tratante deben ser capaces de conocer que
profesionales de la salud han hecho determinados diagnósticos, y en que
información se basó su decisión.

Cabe mencionar que la información a la que accedan las partes
involucradas debe ser completa, consistente y actual: para dar una
atención de calidad, el personal médico debe tener acceso a toda la
historia clínica del paciente hasta el momento, y la información
disponible debe ser consistente entre los distintos departamentos para
dar confianza a las decisiones que toma el personal médico.

Tomando en cuenta lo anterior, al no tener una arquitectura de datos
bien definida, los objetivos antes mencionados son difíciles de lograr:
una gobernanza de datos inexistente podría permitir que cualquier
usuario acceda a datos sensibles, o que los datos no estén disponibles
en el momento que se requieren, y una arquitectura de datos deficiente
impediría tener una trazabilidad, además de no poder asegurar que la
información accedida sea confiable y actual.

Todo lo anterior podría afectar gravemente la calidad del servicio
entregado por la empresa. La falta de información completa podría
impedir a los médicos dar diagnósticos precisos a los pacientes, y la
falta de trazabilidad y accesibilidad podría obstruir procesos de
auditoria periódicos, solo para dar algunos ejemplos.

Para dar solución a los problemas mencionados, es necesario diseñar una
arquitectura de datos que permita una alta interoperabilidad entre los
distintos departamentos, a la vez que implementa procesos de gobernanza
de datos que protejan información sensible y estandaricen protocolos de
nomenclatura de archivos. Además, la propuesta debe ser capaz de
almacenar datos en diversos formatos de manera flexible, y que estos
lleguen a su destino asegurando la consistencia, validez y actualidad de
los datos.

Considerando lo anterior, se propone la siguiente arquitectura de datos
para las siguientes capas:

-   **Fuentes de datos**: Dado que la empresa genera datos a través de
    distintos procesos, dichos procesos se convierten en nuestras
    fuentes de datos. En particular, las hojas de cálculo se pueden
    generar usando herramientas como Excel, y los datos generados por
    los sensores IoT se pueden conectar a la capa de almacenamiento a
    través de middleware que sirva de conexión entre ambas capas.

-   **Almacenamiento**: Dada la diversidad de formatos con los que se
    debe tratar, se propone implementar un DataLake donde se almacenarán
    los datos crudos, que luego serán procesados y almacenados en
    DataMarts que satisfagan las necesidades de cada departamento.

-   **Procesamiento y limpieza**: El proceso más estándar de
    procesamiento y limpieza de datos se ejecutaría a través de
    herramientas especializadas como Talend, mientras que procesos de
    validación más específicos se realizarían en algún lenguaje de
    programación, como Python. Se implementaría un proceso ETL usando
    estas herramientas, extrayendo los datos crudos desde el DataLake, y
    depositando los datos procesados y validados en el DataMart
    respectivo.

-   **Acceso y visualización**: Para este propósito se propone, por un
    lado, implementar una interfaz gráfica de usuario que permita al
    personal médico autenticarse en el sistema y, de esta forma, obtener
    acceso seguro al historial médico del paciente en cuestión. Para la
    evaluación de KPIs y otras métricas, se propone utilizar
    herramientas de BI como Power BI o Tableau, que permiten visualizar
    métricas de negocios, limitando el acceso a dichos reportes.

-   **Seguridad y gobernanza**: En el contexto de la gobernanza, se
    propone crear e implementar protocolos de acceso de los datos para
    prevenir el acceso no autorizado a estos, así como protocolos de
    nomenclatura para mantener un estándar que facilite la
    automatización de procesos. Dichos protocolos se implementarían
    aprovechando las capacidades de control de acceso, complementándolo
    con tecnologías especializadas en gobernanza de datos, como Azure
    Purview.

El diseño propuesto permite mantener una base de datos centralizada con
una alta capacidad de escalabilidad horizontal, gracias a la
implementación de un DataLake, lo que permite a la empresa adaptarse
según su proyección de crecimiento, a la vez que permite adaptarse
fácilmente a cambios repentinos producidos, por ejemplo, por el
surgimiento de nuevas tecnologías médicas.

Por otro lado, permite la integración de los datos entre los distintos
departamentos al mantener una base de datos centralizada, mientras que
se satisfacen las necesidades particulares de cada uno de estos al
implementar DataMarts para cada uno de los departamentos que lo
requieran. Lo anterior, además, permite una alta accesibilidad de la
información, a la vez que se mantiene un firme control de acceso a
través de los DataMarts.

Finalmente, la implementación de una capa de procesamiento y limpieza de
datos mixta entre la extracción de información desde el DataLake y su
deposición en el DataMart respectivo permite implementar reglas de
validación especificas del giro y de cada departamento, manteniendo
altos estándares de calidad para los datos. Por otro lado, esta
arquitectura permite implementar cambios específicos en cada
departamento sin afectar la totalidad del sistema, lo cual permite una
alta adaptabilidad a los cambios.

Dado lo mencionado anteriormente, esta arquitectura de datos cumple, en
particular, con los principios de integración, acceso, calidad y
seguridad de los datos, entre otros.

Para finalizar, a continuación se detalla en un cuadro resumen el
detalle de la solución propuesta:

# Conclusiones

La implementación de una arquitectura de datos que siga las buenas
prácticas y se enfoque en las necesidades de la empresa es indispensable
para asegurar el cumplimiento de las normativas vigentes, entregar una
buena experiencia de usuario y tomar decisiones con confianza. De no
tener una buena gobernanza de datos y una buena arquitectura de datos se
puede producir un desorden administrativo que impacte negativamente en
la productividad, que se vean expuestos datos sensibles de los clientes
o la empresa, que los datos no sean accesibles cuando se necesitan o se
tomen decisiones sesgadas o incorrectas, basadas en datos de baja
calidad.

Entender el funcionamiento de una empresa y sus necesidades resulta
esencial para implementar una arquitectura de datos efectiva, segura y
confiable que aporte valor a la empresa y se adapte a sus necesidades
futuras.
