# IvanL: Código de exploración vs. explotación en Aprendizaje por Refuerzo en Python.

import random

# IvanL: Función para simular un entorno simple donde se elige entre dos opciones: A y B.
def simular_entorno():
    # IvanL: Se elige aleatoriamente una opción (A o B).
    opcion = random.choice(['A', 'B'])
    # IvanL: Se define la recompensa asociada a cada opción.
    recompensa = 1 if opcion == 'A' else 0
    return opcion, recompensa

# IvanL: Algoritmo de exploración vs. explotación.
def exploracion_vs_explotacion(num_intentos):
    # IvanL: Inicialización de los contadores de veces que se selecciona cada opción.
    contador_opcion_A = 0
    contador_opcion_B = 0
    # IvanL: Inicialización del total de recompensa acumulada.
    recompensa_acumulada = 0

    # IvanL: Realiza múltiples intentos.
    for _ in range(num_intentos):
        # IvanL: Se decide si explorar o explotar.
        if random.uniform(0, 1) < 0.1:  # IvanL: 10% de probabilidad de explorar.
            opcion, recompensa = simular_entorno()  # IvanL: Exploración: se elige aleatoriamente una opción.
        else:
            if contador_opcion_A == 0 and contador_opcion_B == 0:
                opcion = random.choice(['A', 'B'])  # IvanL: Si no se ha seleccionado ninguna opción antes, se elige aleatoriamente.
            else:
                # IvanL: Explotación: se elige la opción con mayor recompensa promedio hasta el momento.
                opcion = 'A' if contador_opcion_A / (contador_opcion_A + contador_opcion_B) > 0.5 else 'B'
            recompensa = 1 if opcion == 'A' else 0

        # IvanL: Actualiza el contador de la opción seleccionada y la recompensa acumulada.
        if opcion == 'A':
            contador_opcion_A += 1
        else:
            contador_opcion_B += 1
        recompensa_acumulada += recompensa

    return contador_opcion_A, contador_opcion_B, recompensa_acumulada

# IvanL: Ejecución del algoritmo exploración vs. explotación.
num_intentos = 1000  # IvanL: Número de intentos.
contador_A, contador_B, recompensa_total = exploracion_vs_explotacion(num_intentos)

print(f"Después de {num_intentos} intentos:")
print(f"Veces que se seleccionó la opción A: {contador_A}")
print(f"Veces que se seleccionó la opción B: {contador_B}")
print(f"Recompensa total acumulada: {recompensa_total}")
