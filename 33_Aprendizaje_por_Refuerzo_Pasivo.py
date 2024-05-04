# IvanL: Código de Aprendizaje por Refuerzo Pasivo en Python para entrenar un agente en un entorno simple.

# IvanL: Definición de la clase Entorno para representar el entorno en el que el agente interactúa.
class Entorno:
    def __init__(self):
        self.estado_actual = 0  # IvanL: Estado inicial del entorno.

    def tomar_accion(self, accion):
        # IvanL: Simula la acción del agente en el entorno.
        if accion == 'Izquierda':
            self.estado_actual -= 1
        elif accion == 'Derecha':
            self.estado_actual += 1

        # IvanL: Limita el estado actual dentro del rango [0, 10].
        self.estado_actual = max(0, min(self.estado_actual, 10))

        # IvanL: Calcula la recompensa basada en el estado actual.
        if self.estado_actual == 10:
            return 1  # IvanL: Recompensa positiva si alcanza el estado objetivo.
        else:
            return 0  # IvanL: Recompensa negativa en otros casos.

# IvanL: Definición de la función de aprendizaje por refuerzo pasivo.
def aprendizaje_refuerzo_pasivo(entorno, num_episodios):
    total_recompensa = 0  # IvanL: Inicializa el total de recompensa acumulada.

    # IvanL: Realiza múltiples episodios de interacción con el entorno.
    for _ in range(num_episodios):
        estado = entorno.estado_actual
        recompensa = entorno.tomar_accion('Derecha')  # IvanL: El agente siempre elige moverse a la derecha.

        total_recompensa += recompensa

    return total_recompensa

# IvanL: Creación del entorno.
entorno = Entorno()

# IvanL: Ejecución del aprendizaje por refuerzo pasivo.
num_episodios = 1000  # IvanL: Número de episodios de entrenamiento.
total_recompensa = aprendizaje_refuerzo_pasivo(entorno, num_episodios)

print(f"Total de recompensa acumulada después de {num_episodios} episodios: {total_recompensa}")
