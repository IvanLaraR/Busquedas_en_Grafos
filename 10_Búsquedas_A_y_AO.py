# IvanL - Búsqueda Informada con Algoritmos A* y AO* para encontrar la ruta más corta en un mapa

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

# Función de distancia Manhattan como heurística para A* y AO*
def distancia_manhattan(pos_actual, pos_final):
    x1, y1 = pos_actual
    x2, y2 = pos_final
    return abs(x2 - x1) + abs(y2 - y1)

# Función para encontrar la ruta más corta usando A*
def encontrar_ruta_a_estrella(mapa, inicio, final):
    # Inicializamos la lista de nodos a explorar con la ubicación inicial
    nodos_a_explorar = [(inicio, [inicio], 0)]
    
    # Mientras haya nodos a explorar
    while nodos_a_explorar:
        # Ordenamos los nodos por la suma de la distancia real y la heurística
        nodos_a_explorar.sort(key=lambda x: x[2] + distancia_manhattan(x[0], final))
        # Sacamos el nodo con la menor suma
        (pos_actual, ruta_actual, _) = nodos_a_explorar.pop(0)
        
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
                # Calculamos la distancia recorrida
                distancia_recorrida = len(nueva_ruta) - 1
                # Agregamos el nodo a explorar junto con la distancia recorrida
                nodos_a_explorar.append((nueva_pos, nueva_ruta, distancia_recorrida))
                # Marcamos la posición como visitada
                mapa[nueva_pos[0]][nueva_pos[1]] = 1

# Encontramos la ruta más corta usando A*
ruta_mas_corta_a_estrella = encontrar_ruta_a_estrella(mapa, inicio, final)

# Si se encuentra una ruta, la mostramos
if ruta_mas_corta_a_estrella:
    print("Ruta más corta encontrada usando A*:", ruta_mas_corta_a_estrella)
else:
    print("No se encontró una ruta válida usando A*.")
