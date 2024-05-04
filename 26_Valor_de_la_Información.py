# IvanL: Código de valor de la información en Python para evaluar la utilidad de obtener nueva información.

def calcular_valor_informacion(utilidad_actual, utilidad_futura):
    """
    IvanL: Función para calcular el valor de la información.

    Args:
    - utilidad_actual: Utilidad actual antes de obtener nueva información.
    - utilidad_futura: Utilidad esperada después de obtener nueva información.

    Returns:
    - Valor de la información.
    """
    valor_informacion = utilidad_futura - utilidad_actual  # IvanL: Calcula el cambio en la utilidad.
    return valor_informacion

# IvanL: Ejemplo de uso del algoritmo para evaluar el valor de obtener nueva información.
utilidad_antes = 100  # IvanL: Utilidad antes de obtener nueva información.
utilidad_despues = 150  # IvanL: Utilidad esperada después de obtener nueva información.

valor_de_la_informacion = calcular_valor_informacion(utilidad_antes, utilidad_despues)

print("Valor de la información:", valor_de_la_informacion)
