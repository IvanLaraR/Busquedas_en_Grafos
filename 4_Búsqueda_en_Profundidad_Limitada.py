# IvanL - Búsqueda en Profundidad Limitada para encontrar la receta perdida en un libro de cocina

# Definimos el libro de cocina como una lista de páginas donde 0 representa una página sin receta y 1 representa una página con receta
libro_cocina = [
    [1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [1, 0, 0, 1, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1]
]

# Ubicación inicial donde empezamos a buscar
inicio = (0, 0)

# Función para verificar si una ubicación es válida en el libro de cocina
def es_valido(ubicacion):
    fila, columna = ubicacion
    if 0 <= fila < len(libro_cocina) and 0 <= columna < len(libro_cocina[0]) and libro_cocina[fila][columna] == 1:
        return True
    return False

# Función para encontrar la receta perdida usando búsqueda en profundidad limitada
def buscar_receta(ubicacion, profundidad_limite):
    # Verificamos si la ubicación actual tiene la receta
    if libro_cocina[ubicacion[0]][ubicacion[1]] == 1:
        print("¡Encontramos la receta en la ubicación:", ubicacion, "!")
        return True
    elif profundidad_limite == 0:
        # Si alcanzamos el límite de profundidad y no encontramos la receta
        return False
    else:
        # Marcamos la ubicación actual como visitada
        libro_cocina[ubicacion[0]][ubicacion[1]] = 0
        # Movimientos posibles: arriba, abajo, izquierda, derecha
        movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Exploramos los movimientos posibles
        for movimiento in movimientos:
            nueva_ubicacion = (ubicacion[0] + movimiento[0], ubicacion[1] + movimiento[1])
            # Si la nueva ubicación es válida, continuamos la búsqueda con una profundidad reducida
            if es_valido(nueva_ubicacion):
                if buscar_receta(nueva_ubicacion, profundidad_limite - 1):
                    return True
        # Si no se encuentra la receta en ninguna dirección desde esta ubicación
        return False

# Definimos la profundidad máxima de búsqueda
profundidad_maxima = 3

# Iniciamos la búsqueda desde la ubicación inicial con la profundidad máxima definida
if not buscar_receta(inicio, profundidad_maxima):
    print("No se encontró la receta en el libro de cocina con la profundidad máxima de búsqueda definida.")
