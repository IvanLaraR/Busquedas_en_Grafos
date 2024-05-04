# IvanL: Código de satisfacción de restricciones con acondicionamiento del corte en Python para planificar un menú de comidas.

def planificar_menu(comidas, restricciones):
    """
    IvanL: Función para planificar un menú de comidas respetando restricciones.

    Args:
    - comidas: Lista de comidas disponibles para el menú.
    - restricciones: Diccionario que contiene las restricciones de las comidas.

    Returns:
    - Lista de comidas planificadas respetando las restricciones, o None si no se puede planificar.
    """
    menu_planificado = []  # IvanL: Lista para almacenar el menú planificado.

    for comida in comidas:
        if comida not in restricciones:
            menu_planificado.append(comida)
        else:
            comida_alternativa = encontrar_comida_alternativa(comida, restricciones)
            if comida_alternativa:
                menu_planificado.append(comida_alternativa)
            else:
                return None  # IvanL: Devuelve None si no se puede planificar el menú.

    return menu_planificado  # IvanL: Devuelve el menú planificado.

def encontrar_comida_alternativa(comida, restricciones):
    """
    IvanL: Encuentra una comida alternativa que cumpla con las restricciones.

    Args:
    - comida: Comida que se desea reemplazar.
    - restricciones: Diccionario que contiene las restricciones de las comidas.

    Returns:
    - Comida alternativa que cumple con las restricciones, o None si no se encuentra.
    """
    for comida_alt in restricciones[comida]:
        if comida_alt not in restricciones.values():
            return comida_alt
    return None  # IvanL: Devuelve None si no se encuentra comida alternativa.

# IvanL: Ejemplo de uso del algoritmo para planificar un menú.
comidas_disponibles = ['Ensalada', 'Sopa', 'Pasta', 'Pollo']
restricciones_comidas = {'Ensalada': ['Pollo'], 'Sopa': ['Pasta'], 'Pasta': ['Pollo']}

menu_planificado = planificar_menu(comidas_disponibles, restricciones_comidas)

if menu_planificado:
    print("Menú planificado:")
    for comida in menu_planificado:
        print(comida)
else:
    print("No se puede planificar el menú con las restricciones dadas.")
