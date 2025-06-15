"""
Módulo que implementa funciones para administrar inventarios.

Las funciones implementadas son:
    - agregar_producto
    - eliminar_producto
    - actualizar_producto
    - listar_por_categoria
    - calcular_valor_total
"""

def agregar_producto(inventario, producto, cantidad, precio, categoria):
    """
    Agrega un nuevo producto al inventario.

    Parámetros
    ----------
    - inventario: Diccionario de inventario a modificar.
    - producto: Nombre del producto a agregar.
    - cantidad: Cantidad disponible del producto en inventario.
    - precio: Precio del producto.
    - categoria: Categoría a la que pertenece el producto.

    Retorna
    -------
    None
    """
    inventario[producto] = {
        "Cantidad": cantidad,
        "Precio": precio,
        "Categoría": categoria
        }

def eliminar_producto(inventario, producto):
    """
    Elimina un producto del inventario.

    Parámetros
    ----------
    - inventario: Diccionario de inventario a modificar.
    - producto: Nombre del producto a eliminar.

    Retorna
    -------
    None
    """
    del inventario[producto]

def actualizar_producto(inventario, producto, cantidad, precio):
    """
    Actualiza el precio y cantidad de un producto en inventario.

    Parámetros
    -------
    - inventario: Diccionario de inventario a modificar.
    - producto: Nombre del producto a actualizar.
    - cantidad: Cantidad del producto.
    - precio: Nuevo precio del producto.

    Retorna
    -------
    None
    """
    inventario[producto]["Precio"] = precio
    inventario[producto]["Cantidad"] = cantidad

def listar_por_categoria(inventario, categoria):
    """
    Lista todos los productos disponibles en una categoría específica.

    Parámetros
    ----------
    - inventario: Inventario del cual se extraen los productos.
    - categoría: Categoría a listar.

    Retorna
    -------
    - productos: lista con los productos disponibles para la categoría especificada.
    """
    productos = []
    for producto, detalle in inventario.items():
        if detalle["Cantidad"] > 0 and detalle["Categoría"] == categoria:
            productos.append(producto)
    return productos

def calcular_valor_total(inventario):
    """
    Calcula el valor total del inventario.

    Parámetros
    ----------
    - inventario: Inventario del cual se calcula el total.

    Retorna
    - total: valor total del inventario.
    """
    total = 0
    for producto, detalle in inventario.items():
        total += detalle["Precio"] * detalle["Cantidad"]
    return total