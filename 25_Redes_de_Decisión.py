# IvanL: Código de redes de decisión en Python para modelar la toma de decisiones basada en diferentes escenarios.

def tomar_decision_red(escenario):
    """
    IvanL: Función para tomar una decisión basada en un escenario dado.

    Args:
    - escenario: Escenario que describe la situación actual y las posibles decisiones.

    Returns:
    - Decisión tomada en base al escenario.
    """
    if escenario == "Día soleado":
        return "Ir a la playa"  # IvanL: Si el día es soleado, la decisión es ir a la playa.
    elif escenario == "Día lluvioso":
        return "Ver una película en casa"  # IvanL: Si el día es lluvioso, la decisión es ver una película en casa.
    else:
        return "Hacer ejercicio en el gimnasio"  # IvanL: Si no se especifica el escenario, la decisión por defecto es hacer ejercicio.

# IvanL: Ejemplo de uso del algoritmo para tomar una decisión basada en el escenario actual.
escenario_actual = "Día soleado"  # IvanL: El escenario actual es un día soleado.

decision_tomada = tomar_decision_red(escenario_actual)

print("Decisión tomada:", decision_tomada)
