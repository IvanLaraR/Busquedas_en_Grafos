# IvanL: Código de satisfacción de restricciones con propagación de restricciones en Python para planificar un menú semanal.

def planificar_menu(platos, restricciones):
    """
    IvanL: Función para planificar un menú semanal respetando las restricciones alimenticias.

    Args:
    - platos: Diccionario que mapea días de la semana a los platos disponibles.
    - restricciones: Diccionario que mapea platos a las restricciones alimenticias de los comensales.

    Returns:
    - Diccionario que mapea días de la semana a los platos seleccionados para cada día, o None si no se puede planificar.
    """
    menu_semanal = {}  # IvanL: Diccionario para almacenar el menú semanal planificado.

    for dia, plato in platos.items():
        if dia not in menu_semanal:
            menu_semanal[dia] = plato

            # IvanL: Aplica la propagación de restricciones para eliminar platos prohibidos en otros días.
            for otro_dia, otro_plato in platos.items():
                if otro_dia != dia and not es_compatible(plato, otro_plato, restricciones):
                    return None  # IvanL: Si se viola una restricción, no se puede planificar el menú.
    
    return menu_semanal  # IvanL: Devuelve el menú semanal planificado.

def es_compatible(plato1, plato2, restricciones):
    """
    IvanL: Verifica si dos platos son compatibles según las restricciones alimenticias.

    Args:
    - plato1: Primer plato a comparar.
    - plato2: Segundo plato a comparar.
    - restricciones: Diccionario que mapea platos a las restricciones alimenticias de los comensales.

    Returns:
    - True si los platos son compatibles, False si no.
    """
    if plato1 in restricciones and plato2 in restricciones[plato1]:
        return False
    if plato2 in restricciones and plato1 in restricciones[plato2]:
        return False
    return True  # IvanL: Si no se viola ninguna restricción, los platos son compatibles.

# IvanL: Ejemplo de uso del algoritmo para planificar un menú semanal.
platos_disponibles = {
    "Lunes": "Pollo asado",
    "Martes": "Ensalada",
    "Miércoles": "Pasta",
    "Jueves": "Sopa",
    "Viernes": "Pizza"
}

restricciones_alimenticias = {
    "Pollo asado": ["Vegetariano"],
    "Pasta": ["Gluten"],
    "Pizza": ["Vegetariano", "Gluten"]
}

menu = planificar_menu(platos_disponibles, restricciones_alimenticias)
if menu:
    print("Menú semanal planificado:")
    for dia, plato in menu.items():
        print(f"{dia}: {plato}")
else:
    print("No se puede planificar un menú que cumpla con todas las restricciones.")
