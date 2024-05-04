# IvanL - Búsqueda en Profundidad Iterativa para encontrar un tesoro enterrado en la playa

# Definimos la playa como una cuadrícula donde 0 representa arena y 1 representa el tesoro enterrado
playa = [
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Posición inicial donde empezamos a buscar
inicio = (0, 0)

# Función para verificar si una posición es válida en la playa
def es_valida(posicion):
    x, y = posicion
    if 0 <= x < len(playa) and 0 <= y < len(playa[0]):
        return True
    return False

# Función para encontrar el tesoro enterrado usando búsqueda en profundidad iterativa
def buscar_tesoro():
    # Definimos la profundidad máxima inicial
    profundidad_maxima = 0
    while True:
        # Realizamos una búsqueda en profundidad limitada con la profundidad máxima actual
        if buscar_tesoro_dfs(inicio, profundidad_maxima):
            return True
        # Incrementamos la profundidad máxima para la próxima iteración
        profundidad_maxima += 1

# Función para realizar la búsqueda en profundidad limitada
def buscar_tesoro_dfs(posicion, profundidad):
    # Verificamos si la posición actual tiene el tesoro
    if playa[posicion[0]][posicion[1]] == 1:
        print("¡Encontramos el tesoro en la ubicación:", posicion, "!")
        return True
    # Verificamos si alcanzamos la profundidad máxima
    if profundidad <= 0:
        return False
    # Exploramos los movimientos posibles
    movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for movimiento in movimientos:
        nueva_posicion = (posicion[0] + movimiento[0], posicion[1] + movimiento[1])
        # Verificamos si la nueva posición es válida
        if es_valida(nueva_posicion):
            # Realizamos una búsqueda en profundidad recursiva con la profundidad reducida
            if buscar_tesoro_dfs(nueva_posicion, profundidad - 1):
                return True
    # Si no se encuentra el tesoro en ninguna dirección desde esta posición
    return False

# Realizamos la búsqueda del tesoro
if not buscar_tesoro():
    print("No se encontró el tesoro en la playa.")
