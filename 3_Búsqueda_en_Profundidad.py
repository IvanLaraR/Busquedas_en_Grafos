# IvanL - Búsqueda en Profundidad para encontrar el libro perdido en una biblioteca

# Definimos la biblioteca como una lista de estantes donde 0 representa un estante vacío y 1 representa un estante con libros
biblioteca = [
    [1, 1, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 1, 1, 1]
]

# Ubicación inicial donde empezamos a buscar
inicio = (0, 0)

# Función para verificar si una ubicación es válida en la biblioteca
def es_valido(ubicacion):
    fila, columna = ubicacion
    if 0 <= fila < len(biblioteca) and 0 <= columna < len(biblioteca[0]) and biblioteca[fila][columna] == 1:
        return True
    return False

# Función para encontrar el libro perdido usando búsqueda en profundidad
def buscar_libro(ubicacion):
    # Verificamos si la ubicación actual tiene el libro
    if biblioteca[ubicacion[0]][ubicacion[1]] == 1:
        print("¡Encontramos el libro en la ubicación:", ubicacion, "!")
        return True
    else:
        # Marcamos la ubicación actual como visitada
        biblioteca[ubicacion[0]][ubicacion[1]] = 0
        # Movimientos posibles: arriba, abajo, izquierda, derecha
        movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Exploramos los movimientos posibles
        for movimiento in movimientos:
            nueva_ubicacion = (ubicacion[0] + movimiento[0], ubicacion[1] + movimiento[1])
            # Si la nueva ubicación es válida, continuamos la búsqueda
            if es_valido(nueva_ubicacion):
                if buscar_libro(nueva_ubicacion):
                    return True
        # Si no se encuentra el libro en ninguna dirección desde esta ubicación
        return False

# Iniciamos la búsqueda desde la ubicación inicial
if not buscar_libro(inicio):
    print("No se encontró el libro en la biblioteca.")
    
