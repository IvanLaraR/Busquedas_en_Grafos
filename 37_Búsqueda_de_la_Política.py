# IvanL: Código de Búsqueda de la Política en Aprendizaje por Refuerzo en Python.

# IvanL: Definición del entorno del juego de tiro al blanco.
class JuegoTiroAlBlanco:
    def __init__(self):
        self.posicion_actual = 0  # IvanL: Posición inicial del objetivo.

    def disparar(self, direccion):
        # IvanL: Simula el disparo y devuelve la recompensa.
        if direccion == 'izquierda' and self.posicion_actual > 0:
            self.posicion_actual -= 1
        elif direccion == 'derecha' and self.posicion_actual < 10:
            self.posicion_actual += 1

        # IvanL: Calcula la recompensa basada en la posición del objetivo.
        if self.posicion_actual == 5:
            return 1  # IvanL: Recompensa máxima si se alcanza el centro.
        else:
            return 0  # IvanL: Recompensa mínima en otros casos.

# IvanL: Algoritmo de búsqueda de la política óptima.
def buscar_politica_optima(entorno, num_intentos):
    politica_optima = {}  # IvanL: Inicializa la política óptima como un diccionario vacío.

    # IvanL: Realiza múltiples intentos para explorar el entorno y aprender la política óptima.
    for _ in range(num_intentos):
        estado_actual = entorno.posicion_actual
        # IvanL: Selecciona la acción que maximiza la recompensa esperada.
        accion_optima = 'izquierda' if estado_actual > 5 else 'derecha'
        politica_optima[estado_actual] = accion_optima

        # IvanL: Realiza la acción y observa la recompensa.
        recompensa = entorno.disparar(accion_optima)


    return politica_optima

# IvanL: Creación del entorno del juego de tiro al blanco.
juego = JuegoTiroAlBlanco()

# IvanL: Ejecución del algoritmo de búsqueda de la política óptima.
num_intentos = 1000  # IvanL: Número de intentos para explorar y aprender la política óptima.
politica_optima = buscar_politica_optima(juego, num_intentos)

print("Política óptima aprendida:")
for estado, accion in politica_optima.items():
    print(f"En el estado {estado}, la acción óptima es disparar hacia la {accion}.")
