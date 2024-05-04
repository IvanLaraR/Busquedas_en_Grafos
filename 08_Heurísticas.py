# IvanL - Búsqueda Informada con Heurísticas para encontrar la ruta más corta en un mapa

# Definimos el mapa como una cuadrícula donde 0 representa un espacio vacío y 1 representa un obstáculo
mapa = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Definimos la ubicación inicial y final en el mapa
inicio = (0, 0)
final = (4, 4)

# Función de distancia Manhattan como heurística
def distancia_manhattan(pos_actual, pos_final):
    x1, y1 = pos_actual
    x2, y2 = pos_final
    return abs(x2 - x1) + abs(y2 - y1)

# Función para encontrar la ruta más corta usando búsqueda informada con heurística
def encontrar_ruta(mapa, inicio, final):
    # Inicializamos la lista de nodos a explorar con la ubicación inicial
    nodos_a_explorar = [(inicio, [inicio])]
    
    # Mientras haya nodos a explorar
    while nodos_a_explorar:
        # Ordenamos los nodos por la suma de la distancia real y la heurística
        nodos_a_explorar.sort(key=lambda x: len(x[1]) + distancia_manhattan(x[0], final))
        # Sacamos el nodo con la menor suma
        (pos_actual, ruta_actual) = nodos_a_explorar.pop(0)
        
        # Si llegamos a la ubicación final, retornamos la ruta
        if pos_actual == final:
            return ruta_actual
        
        # Exploramos los movimientos posibles
        movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for movimiento in movimientos:
            nueva_pos = (pos_actual[0] + movimiento[0], pos_actual[1] + movimiento[1])
            if 0 <= nueva_pos[0] < len(mapa) and 0 <= nueva_pos[1] < len(mapa[0]) and mapa[nueva_pos[0]][nueva_pos[1]] == 0:
                nueva_ruta = list(ruta_actual)
                nueva_ruta.append(nueva_pos)
                nodos_a_explorar.append((nueva_pos, nueva_ruta))
                mapa[nueva_pos[0]][nueva_pos[1]] = 1  # Marcamos la posición como visitada

# Encontramos la ruta más corta
ruta_mas_corta = encontrar_ruta(mapa, inicio, final)

# Si se encuentra una ruta, la mostramos
if ruta_mas_corta:
    print("Ruta más corta encontrada:", ruta_mas_corta)
else:
    print("No se encontró una ruta válida.")
