# IvanL: Código de proceso de decisión de Markov parcialmente observable (POMDP) en Python para modelar la toma de decisiones en entornos con incertidumbre.

def resolver_problema_toma_de_decisiones_pomdp(recompensas, probabilidades_transicion, observaciones, factor_descuento, num_iteraciones):
    """
    IvanL: Función para resolver un problema de toma de decisiones utilizando el proceso de decisión de Markov parcialmente observable (POMDP).

    Args:
    - recompensas: Diccionario que contiene las recompensas asociadas a cada estado.
    - probabilidades_transicion: Diccionario que contiene las probabilidades de transición entre estados.
    - observaciones: Diccionario que contiene las probabilidades de observación para cada acción y estado.
    - factor_descuento: Factor de descuento para las recompensas futuras.
    - num_iteraciones: Número máximo de iteraciones para la convergencia.

    Returns:
    - Política óptima para cada estado.
    """
    politica_optima = {}  # IvanL: Diccionario para almacenar la política óptima de cada estado.

    # IvanL: Inicialización de la política óptima.
    for estado in recompensas:
        politica_optima[estado] = 0  # IvanL: Valor predeterminado para todos los estados.

    # IvanL: Iteración de políticas hasta que se alcance el número máximo de iteraciones.
    for _ in range(num_iteraciones):
        politica_cambiada = False  # IvanL: Indica si la política cambió en esta iteración.

        # IvanL: Itera sobre cada estado para actualizar su política óptima.
        for estado in recompensas:
            mejor_accion = None
            mejor_valor = float('-inf')

            # IvanL: Verifica si el estado tiene transiciones definidas.
            if estado in probabilidades_transicion:
                # IvanL: Itera sobre las posibles acciones para encontrar la mejor.
                for accion, estado_siguiente in probabilidades_transicion[estado].items():
                    valor = recompensas[estado_siguiente] + factor_descuento * politica_optima[estado_siguiente]
                    if valor > mejor_valor:
                        mejor_valor = valor
                        mejor_accion = accion

                # IvanL: Actualiza la política óptima para el estado.
                politica_optima[estado] = mejor_accion

                # IvanL: Verifica si la política cambió.
                if mejor_accion != politica_optima[estado]:
                    politica_cambiada = True

        # IvanL: Verifica si la política no cambió en esta iteración.
        if not politica_cambiada:
            break

    return politica_optima

# IvanL: Ejemplo de uso del algoritmo para resolver un problema de toma de decisiones POMDP.
recompensas = {'Inicio': 0, 'A': -1, 'B': -2, 'C': 5, 'Fin': 0}  # IvanL: Recompensas asociadas a cada estado.
prob_transicion = {'Inicio': {'A': 'A'}, 'A': {'B': 'B', 'C': 'C'}, 'B': {'Fin': 'Fin', 'C': 'C'}, 'C': {'Fin': 'Fin'}, 'Fin': {}}  # IvanL: Probabilidades de transición entre estados.
observaciones = {'A': 0.8, 'B': 0.5, 'C': 0.7}  # IvanL: Probabilidades de observación para cada acción y estado.
factor_descuento = 0.9  # IvanL: Factor de descuento para las recompensas futuras.
num_iteraciones = 100  # IvanL: Número máximo de iteraciones.

politica_optima = resolver_problema_toma_de_decisiones_pomdp(recompensas, prob_transicion, observaciones, factor_descuento, num_iteraciones)

print("Política óptima para cada estado:")
for estado, accion in politica_optima.items():
    print(f"{estado}: {accion}")
