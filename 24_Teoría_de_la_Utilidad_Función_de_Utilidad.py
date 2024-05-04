# IvanL: Código de teoría de la utilidad en Python para calcular la utilidad de una decisión.

def calcular_utilidad(costo, beneficio, riesgo):
    """
    IvanL: Función para calcular la utilidad de una decisión.

    Args:
    - costo: Costo asociado a la decisión.
    - beneficio: Beneficio asociado a la decisión.
    - riesgo: Nivel de riesgo asociado a la decisión.

    Returns:
    - Utilidad de la decisión.
    """
    utilidad = beneficio - costo * riesgo  # IvanL: Calcula la utilidad restando el costo ponderado por el riesgo al beneficio.
    return utilidad

# IvanL: Ejemplo de uso del algoritmo para tomar una decisión.
costo_compra = 20  # IvanL: Costo de comprar un producto.
beneficio_utilidad = 50  # IvanL: Beneficio en utilidad de comprar el producto.
nivel_riesgo = 0.2  # IvanL: Nivel de riesgo asociado a comprar el producto.

utilidad_decision = calcular_utilidad(costo_compra, beneficio_utilidad, nivel_riesgo)

print("Utilidad de la decisión:", utilidad_decision)
