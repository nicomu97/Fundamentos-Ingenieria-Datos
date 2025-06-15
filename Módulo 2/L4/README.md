# Objetivos de la actividad

Esta actividad busca reforzar los conocimientos sobre estructuras de datos y sentencias iterativas a través de la implementación de un sistema de gestión de inventarios.

# Descripción de la actividad

Se debe implementar un sistema de gestión de inventario usando estructuras de datos estándar de Python. Este sistema gestiona inventarios escritos como diccionarios de Python, los cuales incluyen cantidad,
precio y categoría del producto, y debe permitir realizar las siguientes acciones:
- Agregar productos al inventario.
- Eliminar productos del inventario.
- Actualizar la cantidad y precio de un producto.
- Listar los productos disponibles en una categoría específica.
- Calcular el valor total del inventario.

# Resultados

Las funciones solicitadas se implementan en el módulo operaciones_inventario.py, y son puestas a prueba en el script test.py. Para probar la funcionalidad del módulo, primero se crea un inventario vacío
(sin productos) y se va poblando a través de la función agregar_producto, procediento a imprimir el inventario para comprobar si los productos se ingresaron correctamente.

Posteriormente, se procede a eliminar un producto del inventario, y a actualizar otro producto. Tras cada paso, se imprime en consola el inventario para comprobar si se ejecutaron los cambios.
Después, se procede a listar algunos productos por categoría, imprimiendo los resultados obtenidos, para finalmente calcular el valor total del inventario.

![image](https://github.com/user-attachments/assets/314f5c19-ca59-4fe1-9847-91d85fcc257a)

Como se puede observar en la imágen, las funciones implementadas funcionan según lo esperado.
