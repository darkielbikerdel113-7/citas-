def calcular_punto_equilibrio(costos_fijos, precio_unitario, costo_variable_unitario):
    """
    Calcula el punto de equilibrio en unidades.
    :param costos_fijos: Total de costos fijos
    :param precio_unitario: Precio de venta por unidad
    :param costo_variable_unitario: Costo variable por unidad
    :return: Punto de equilibrio en unidades
    """
    if precio_unitario <= costo_variable_unitario:
        raise ValueError("El precio unitario debe ser mayor al costo variable unitario.")
    
    punto_equilibrio = costos_fijos / (precio_unitario - costo_variable_unitario)
    return round(punto_equilibrio, 2)


# Ejemplo de uso:
costos_fijos = 5000
precio_unitario = 25
costo_variable_unitario = 10

print("Punto de equilibrio en unidades:", calcular_punto_equilibrio(costos_fijos, precio_unitario, costo_variable_unitario))
