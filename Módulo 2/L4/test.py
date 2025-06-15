"""
Prueba de funcionalidad del módulo operaciones_inventario.
"""

import operaciones_inventario as oi

inventario = dict()

oi.agregar_producto(inventario, "Galletas", 5, 660, "Alimentos")
oi.agregar_producto(inventario, "Helado", 3, 1_300, "Alimentos")
oi.agregar_producto(inventario, "Fideos", 0, 2_300, "Alimentos")
oi.agregar_producto(inventario, "Desodorante", 8, 750, "Higiene")
oi.agregar_producto(inventario, "Limpia Piso", 2, 3_500, "Aseo")
oi.agregar_producto(inventario, "Atún", 2, 350, "Alimentos")

print("Inventario Actual: \n", inventario)

oi.eliminar_producto(inventario, "Atún")

print("\nInventario sin Atún: \n", inventario)

oi.actualizar_producto(inventario, "Helado", 7, 1_100)

print("\nInventario con producto 'Helado' modificado: \n", inventario)

print("\nProductos en categoría 'Alimentos':", oi.listar_por_categoria(inventario, "Alimentos"))
print("\nProductos en categoría 'Aseo':", oi.listar_por_categoria(inventario, "Aseo"))
print("\nProductos en categoría 'Otros':", oi.listar_por_categoria(inventario, "Otros"))

print("\nValor total del inventario: \n", oi.calcular_valor_total(inventario))