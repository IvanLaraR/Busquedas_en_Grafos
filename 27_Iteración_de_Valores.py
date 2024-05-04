# IvanL: Código corregido de iteración de valores en Python para resolver un problema de toma de decisiones.

def resolver_problema_toma_de_decisiones(recompensas, probabilidades_transicion, factor_descuento, umbral_error):
    """
    IvanL: Función para resolver un problema de toma de decisiones utilizando iteración de valores.

    Args:
    - recompensas: Diccionario que contiene las recompensas asociadas a cada estado.
    - probabilidades_transicion: Diccionario que contiene las probabilidades de transición entre estados.
    - factor_descuento: Factor de descuento para las recompensas futuras.
    - umbral_error: Umbral de error para detener la iteración.

    Returns:
    - Valores óptimos para cada estado.
    """
    valores_optimos = {}  # IvanL: Diccionario para almacenar los valores óptimos de cada estado.

    # IvanL: Inicialización de los valores óptimos.
    for estado in recompensas:
        valores_optimos[estado] = 0

    # IvanL: Iteración de valores hasta que converja o se alcance el umbral de error.
    while True:
        max_error = 0  # IvanL: Inicializa el error máximo en esta iteración.

        # IvanL: Itera sobre cada estado para actualizar su valor óptimo.
        for estado in recompensas:
            valor_anterior = valores_optimos[estado]
            nuevo_valor = 0

            # IvanL: Verifica si el estado tiene transiciones definidas.
            if estado in probabilidades_transicion:
                # IvanL: Calcula el nuevo valor óptimo para el estado.
                for estado_siguiente in probabilidades_transicion[estado]:
                    prob_transicion = probabilidades_transicion[estado][estado_siguiente]
                    recompensa = recompensas[estado_siguiente]
                    nuevo_valor += prob_transicion * (recompensa + factor_descuento * valores_optimos[estado_siguiente])

            valores_optimos[estado] = nuevo_valor

            # IvanL: Actualiza el error máximo.
            max_error = max(max_error, abs(valor_anterior - nuevo_valor))

        # IvanL: Verifica si se alcanzó el umbral de error para detener la iteración.
        if max_error < umbral_error:
            break

    return valores_optimos

# IvanL: Ejemplo de uso del algoritmo para resolver un problema de toma de decisiones.
recompensas = {'Inicio': 0, 'A': -1, 'B': -2, 'C': 5, 'Fin': 0}  # IvanL: Recompensas asociadas a cada estado.
prob_transicion = {'Inicio': {'A': 1}, 'A': {'B': 0.7, 'C': 0.3}, 'B': {'Fin': 0.8, 'C': 0.2}, 'C': {'Fin': 1}, 'Fin': {}}  # IvanL: Probabilidades de transición entre estados.
descuento = 0.9  # IvanL: Factor de descuento para las recompensas futuras.
umbral = 0.01  # IvanL: Umbral de error para detener la iteración.

valores_optimos = resolver_problema_toma_de_decisiones(recompensas, prob_transicion, descuento, umbral)

print("Valores óptimos de los estados:")
for estado, valor in valores_optimos.items():
    print(f"{estado}: {valor}")
