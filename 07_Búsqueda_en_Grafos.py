# IvanL - Búsqueda en Grafos para encontrar el camino más corto entre dos ciudades

# Definimos el mapa de ciudades y las conexiones entre ellas como un diccionario de diccionarios
mapa_ciudades = {
    "A": {"B": 1, "C": 3},
    "B": {"A": 1, "C": 1, "D": 2},
    "C": {"A": 3, "B": 1, "D": 1, "E": 4},
    "D": {"B": 2, "C": 1, "E": 1, "F": 2},
    "E": {"C": 4, "D": 1, "F": 3},
    "F": {"D": 2, "E": 3}
}

# Función para encontrar el camino más corto entre dos ciudades usando búsqueda en grafos
def buscar_camino(ciudad_inicio, ciudad_fin):
    # Inicializamos la cola de nodos a explorar con la ciudad inicial
    cola = [(ciudad_inicio, [ciudad_inicio])]
    # Lista para almacenar los nodos visitados
    visitados = []

    # Mientras haya nodos por explorar en la cola
    while cola:
        # Sacamos el primer nodo de la cola
        (ciudad_actual, camino) = cola.pop(0)
        # Si llegamos a la ciudad final, retornamos el camino
        if ciudad_actual == ciudad_fin:
            return camino
        # Si la ciudad actual no ha sido visitada
        if ciudad_actual not in visitados:
            # Agregamos la ciudad actual a la lista de visitados
            visitados.append(ciudad_actual)
            # Exploramos las ciudades vecinas
            for vecino, distancia in mapa_ciudades[ciudad_actual].items():
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                # Agregamos el vecino a la cola junto con el nuevo camino
                cola.append((vecino, nuevo_camino))
                # Ordenamos la cola por la distancia total del camino
                cola.sort(key=lambda x: calcular_distancia(x[1]))

# Función para calcular la distancia total de un camino
def calcular_distancia(camino):
    distancia_total = 0
    for i in range(len(camino) - 1):
        distancia_total += mapa_ciudades[camino[i]][camino[i + 1]]
    return distancia_total

# Realizamos la búsqueda del camino más corto entre dos ciudades
ciudad_inicio = "A"
ciudad_fin = "F"
camino_mas_corto = buscar_camino(ciudad_inicio, ciudad_fin)

# Si se encuentra un camino, lo mostramos
if camino_mas_corto:
    print("El camino más corto desde", ciudad_inicio, "hasta", ciudad_fin, "es:", camino_mas_corto)
else:
    print("No se encontró un camino válido desde", ciudad_inicio, "hasta", ciudad_fin)
