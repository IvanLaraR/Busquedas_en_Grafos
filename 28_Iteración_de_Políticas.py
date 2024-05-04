# IvanL: Código de iteración de políticas en Python para resolver un problema de toma de decisiones.

def resolver_problema_toma_de_decisiones_politicas(recompensas, probabilidades_transicion, umbral_error):
    """
    IvanL: Función para resolver un problema de toma de decisiones utilizando iteración de políticas.

    Args:
    - recompensas: Diccionario que contiene las recompensas asociadas a cada estado.
    - probabilidades_transicion: Diccionario que contiene las probabilidades de transición entre estados.
    - umbral_error: Umbral de error para detener la iteración.

    Returns:
    - Política óptima para cada estado.
    """
    politica_optima = {}  # IvanL: Diccionario para almacenar la política óptima de cada estado.

    # IvanL: Inicialización de la política óptima.
    for estado in recompensas:
        politica_optima[estado] = None

    # IvanL: Iteración de políticas hasta que converja o se alcance el umbral de error.
    while True:
        politica_cambiada = False  # IvanL: Indica si la política cambió en esta iteración.

        # IvanL: Itera sobre cada estado para actualizar su política óptima.
        for estado in recompensas:
            accion_anterior = politica_optima[estado]
            mejor_accion = None
            mejor_valor = float('-inf')

            # IvanL: Verifica si el estado tiene transiciones definidas.
            if estado in probabilidades_transicion:
                # IvanL: Itera sobre las posibles acciones para encontrar la mejor.
                for accion, estado_siguiente in probabilidades_transicion[estado].items():
                    valor = recompensas[estado_siguiente]
                    if valor > mejor_valor:
                        mejor_valor = valor
                        mejor_accion = accion

                politica_optima[estado] = mejor_accion

            # IvanL: Verifica si la política cambió.
            if accion_anterior != mejor_accion:
                politica_cambiada = True

        # IvanL: Verifica si se alcanzó el umbral de error para detener la iteración.
        if not politica_cambiada:
            break

    return politica_optima

# IvanL: Ejemplo de uso del algoritmo para resolver un problema de toma de decisiones con iteración de políticas.
recompensas = {'Inicio': 0, 'A': -1, 'B': -2, 'C': 5, 'Fin': 0}  # IvanL: Recompensas asociadas a cada estado.
prob_transicion = {'Inicio': {'A': 'A'}, 'A': {'B': 'B', 'C': 'C'}, 'B': {'Fin': 'Fin', 'C': 'C'}, 'C': {'Fin': 'Fin'}, 'Fin': {}}  # IvanL: Probabilidades de transición entre estados.
umbral = 0.01  # IvanL: Umbral de error para detener la iteración.

politica_optima = resolver_problema_toma_de_decisiones_politicas(recompensas, prob_transicion, umbral)

print("Política óptima para cada estado:")
for estado, accion in politica_optima.items():
    print(f"{estado}: {accion}")
