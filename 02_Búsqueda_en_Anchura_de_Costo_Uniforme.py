# IvanL - Búsqueda en Anchura para encontrar el camino más corto en un laberinto

# Definimos el laberinto como una matriz donde 0 representa un camino libre y 1 representa una pared
laberinto = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Posición inicial y final en el laberinto
inicio = (0, 0)
final = (4, 4)

# Movimientos posibles: arriba, abajo, izquierda, derecha
movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Función para verificar si una posición es válida en el laberinto
def es_valido(posicion):
    x, y = posicion
    if 0 <= x < len(laberinto) and 0 <= y < len(laberinto[0]) and laberinto[x][y] == 0:
        return True
    return False

# Función para encontrar el camino más corto usando búsqueda en anchura
def buscar_camino():
    # Cola para almacenar los nodos a explorar
    cola = [(inicio, [inicio])]
    # Conjunto para almacenar las posiciones visitadas
    visitados = set()
    
    # Mientras haya nodos en la cola
    while cola:
        # Sacamos el primer nodo de la cola
        posicion_actual, camino = cola.pop(0)
        # Si llegamos al destino, retornamos el camino
        if posicion_actual == final:
            return camino
        # Marcamos la posición actual como visitada
        visitados.add(posicion_actual)
        # Exploramos los movimientos posibles desde la posición actual
        for movimiento in movimientos:
            nueva_posicion = (posicion_actual[0] + movimiento[0], posicion_actual[1] + movimiento[1])
            # Verificamos si la nueva posición es válida y no ha sido visitada
            if es_valido(nueva_posicion) and nueva_posicion not in visitados:
                # Agregamos la nueva posición a la cola junto con el camino hasta ese punto
                nueva_camino = list(camino)
                nueva_camino.append(nueva_posicion)
                cola.append((nueva_posicion, nueva_camino))
    
    # Si no se encuentra un camino válido
    return None

# Función para imprimir el laberinto con el camino encontrado
def imprimir_laberinto(camino):
    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            if (i, j) == inicio:
                print("S", end=" ")
            elif (i, j) == final:
                print("E", end=" ")
            elif (i, j) in camino:
                print("*", end=" ")
            else:
                print(laberinto[i][j], end=" ")
        print()

# Buscamos el camino más corto
camino_corto = buscar_camino()

# Si se encuentra un camino, lo imprimimos
if camino_corto:
    print("Se encontró un camino:")
    imprimir_laberinto(camino_corto)
else:
    print("No se encontró un camino válido.")
