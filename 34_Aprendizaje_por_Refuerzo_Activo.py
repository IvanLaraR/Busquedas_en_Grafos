# IvanL: Código de Aprendizaje por Refuerzo Activo en Python para entrenar un agente en un entorno simple.

# IvanL: Definición de la clase Entorno para representar el entorno en el que el agente interactúa.
class Entorno:
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

# IvanL: Definición de la función de aprendizaje por refuerzo activo.
def aprendizaje_refuerzo_activo(entorno, politica, num_episodios):
    recompensa_total = 0  # IvanL: Inicializa la recompensa total acumulada.

    # IvanL: Realiza múltiples episodios de interacción con el entorno.
    for _ in range(num_episodios):
        estado = entorno.posicion_actual
        accion = politica(estado)  # IvanL: El agente elige una acción basada en la política.

        recompensa = entorno.tomar_accion(accion)  # IvanL: El agente realiza la acción y recibe una recompensa.
        recompensa_total += recompensa

    return recompensa_total

# IvanL: Definición de una política simple para el agente.
def politica_simple(estado):
    # IvanL: El agente siempre elige moverse a la derecha.
    return 'Derecha'

# IvanL: Creación del entorno.
entorno = Entorno()

# IvanL: Ejecución del aprendizaje por refuerzo activo.
num_episodios = 1000  # IvanL: Número de episodios de entrenamiento.
recompensa_total = aprendizaje_refuerzo_activo(entorno, politica_simple, num_episodios)

print(f"Recompensa total acumulada después de {num_episodios} episodios: {recompensa_total}")
