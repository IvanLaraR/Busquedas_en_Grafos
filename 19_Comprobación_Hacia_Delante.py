# IvanL: Código de satisfacción de restricciones con comprobación hacia adelante en Python para planificar una fiesta.

def planificar_fiesta(asistentes, preferencias):
    """
    IvanL: Función para planificar una fiesta según las preferencias de los asistentes.

    Args:
    - asistentes: Diccionario que mapea nombres de asistentes a sus preferencias.
    - preferencias: Diccionario que mapea nombres de actividades a la cantidad de personas que pueden realizarlas simultáneamente.

    Returns:
    - True si se puede planificar la fiesta según las restricciones, False si no.
    """
    actividades_planificadas = {}  # IvanL: Diccionario para almacenar las actividades planificadas y sus asistentes.

    for asistente, preferencia in asistentes.items():
        actividad_elegida = encontrar_actividad(preferencia, preferencias, actividades_planificadas)
        if actividad_elegida is None:
            return False  # IvanL: Si no se puede encontrar una actividad para un asistente, se cancela la fiesta.
        actividades_planificadas.setdefault(actividad_elegida, []).append(asistente)

        # IvanL: Verifica si hay demasiadas personas para la actividad elegida.
        if len(actividades_planificadas[actividad_elegida]) > preferencias[actividad_elegida]:
            return False  # IvanL: Si se excede el límite de personas para una actividad, se cancela la fiesta.

    return True  # IvanL: Si se satisfacen todas las restricciones, la fiesta puede planificarse.

def encontrar_actividad(preferencia, preferencias, actividades_planificadas):
    """
    IvanL: Encuentra la actividad preferida de un asistente que aún no está llena.

    Args:
    - preferencia: Lista de actividades preferidas por el asistente.
    - preferencias: Diccionario que mapea nombres de actividades a la cantidad de personas que pueden realizarlas simultáneamente.
    - actividades_planificadas: Diccionario que almacena las actividades planificadas y sus asistentes.

    Returns:
    - Nombre de la actividad si se encuentra una adecuada, None si no.
    """
    for actividad in preferencia:
        if actividad in preferencias and len(actividades_planificadas.get(actividad, [])) < preferencias[actividad]:
            return actividad
    return None  # IvanL: Si no se puede encontrar una actividad adecuada, devuelve None.

# IvanL: Ejemplo de uso del algoritmo para planificar una fiesta.
preferencias_asistentes = {
    "Juan": ["Baile", "Juegos", "Cocina"],
    "María": ["Cocina", "Juegos", "Baile"],
    "Pedro": ["Juegos", "Baile", "Cocina"]
}

capacidad_actividades = {
    "Baile": 2,
    "Juegos": 3,
    "Cocina": 1
}

if planificar_fiesta(preferencias_asistentes, capacidad_actividades):
    print("¡La fiesta está planificada con éxito!")
else:
    print("No se puede planificar la fiesta debido a restricciones de capacidad.")
