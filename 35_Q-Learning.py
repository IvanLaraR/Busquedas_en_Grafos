# IvanL: Código de Q-Learning en Python para el aprendizaje por refuerzo en un entorno simple.

import random

# IvanL: Definición de la clase Entorno para representar el entorno en el que el agente interactúa.
class EntornoQLearning:
    def __init__(self):
        self.posicion_actual = 0  # IvanL: Posición inicial del agente en el entorno.

    def tomar_accion(self, accion):
        # IvanL: Simula la acción del agente en el entorno.
        if accion == 'Izquierda':
            self.posicion_actual -= 1
        elif accion == 'Derecha':
            self.posicion_actual += 1

        # IvanL: Limita la posición actual dentro del rango [0, 10].
        self.posicion_actual = max(0, min(self.posicion_actual, 10))

        # IvanL: Calcula la recompensa basada en la posición actual.
        if self.posicion_actual == 10:
            return 1  # IvanL: Recompensa positiva si alcanza la posición objetivo.
        else:
            return 0  # IvanL: Recompensa negativa en otros casos.

# IvanL: Función de Q-Learning para el aprendizaje por refuerzo.
def q_learning(entorno, num_episodios, tasa_aprendizaje=0.1, factor_descuento=0.9):
    # IvanL: Inicialización de la tabla Q con valores arbitrarios.
    q_table = {(estado, accion): 0 for estado in range(11) for accion in ['Izquierda', 'Derecha']}

    # IvanL: Realiza múltiples episodios de aprendizaje.
    for _ in range(num_episodios):
        estado_actual = entorno.posicion_actual
        accion = seleccionar_accion(q_table, estado_actual)

        # IvanL: Toma la acción y observa el resultado.
        recompensa = entorno.tomar_accion(accion)
        nuevo_estado = entorno.posicion_actual

        # IvanL: Actualiza el valor Q del par (estado, acción) con la fórmula de Q-Learning.
        mejor_valor_q = max([q_table.get((nuevo_estado, a), 0) for a in ['Izquierda', 'Derecha']])
        q_table[(estado_actual, accion)] += tasa_aprendizaje * (recompensa + factor_descuento * mejor_valor_q - q_table[(estado_actual, accion)])

    return q_table

# IvanL: Función para seleccionar una acción usando la tabla Q.
def seleccionar_accion(q_table, estado):
    # IvanL: Selecciona la acción con la probabilidad epsilon-greedy.
    epsilon = 0.1
    if random.uniform(0, 1) < epsilon:
        return random.choice(['Izquierda', 'Derecha'])
    else:
        return max(q_table, key=lambda x: q_table[x] if x[0] == estado else float('-inf'))[1]

# IvanL: Creación del entorno.
entorno_qlearning = EntornoQLearning()

# IvanL: Ejecución del aprendizaje por refuerzo con Q-Learning.
num_episodios = 1000  # IvanL: Número de episodios de entrenamiento.
tabla_q = q_learning(entorno_qlearning, num_episodios)

print("Tabla Q resultante:")
for estado, accion in tabla_q:
    print(f"Estado: {estado}, Acción: {accion}, Valor Q: {tabla_q[(estado, accion)]}")
