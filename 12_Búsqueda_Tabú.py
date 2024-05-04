# IvanL - Búsqueda Informada con Búsqueda Tabú para encontrar la mejor ruta en una ciudad congestionada

# Definimos la ciudad como un grafo donde cada nodo representa una intersección y las aristas representan calles
# Cada arista tiene un costo asociado que representa la congestión del tráfico
ciudad = {
    "A": {"B": 2, "C": 3},
    "B": {"A": 2, "C": 1, "D": 4},
    "C": {"A": 3, "B": 1, "D": 2, "E": 3},
    "D": {"B": 4, "C": 2, "E": 2, "F": 3},
    "E": {"C": 3, "D": 2, "F": 1},
    "F": {"D": 3, "E": 1}
}

# Función para calcular el costo total de una ruta en la ciudad
def calcular_costo_total(ruta):
    costo_total = 0
    for i in range(len(ruta) - 1):
        if ruta[i] in ciudad and ruta[i + 1] in ciudad[ruta[i]]:
            costo_total += ciudad[ruta[i]][ruta[i + 1]]
        else:
            return float('inf')  # Retornar infinito si no hay conexión válida
    return costo_total

# Función para generar vecinos de una ruta intercambiando dos nodos adyacentes
def generar_vecinos(ruta):
    vecinos = []
    for i in range(len(ruta) - 1):
        vecino = ruta[:]
        vecino[i], vecino[i + 1] = vecino[i + 1], vecino[i]
        vecinos.append(vecino)
    return vecinos

# Función para encontrar la mejor ruta usando búsqueda tabú
def encontrar_mejor_ruta(ciudad, inicio, destino, iteraciones_tabu):
    # Inicializamos la ruta inicial y el mejor costo
    mejor_ruta = [inicio, destino]
    mejor_costo = calcular_costo_total(mejor_ruta)
    ruta_actual = mejor_ruta[:]
    
    # Iteramos para explorar vecinos y mejorar la ruta
    iteraciones = 0
    while iteraciones < iteraciones_tabu:
        vecinos = generar_vecinos(ruta_actual)
        mejor_vecino = None
        mejor_costo_vecino = float('inf')
        
        # Evaluamos los vecinos y seleccionamos el mejor vecino
        for vecino in vecinos:
            costo_vecino = calcular_costo_total(vecino)
            if costo_vecino < mejor_costo_vecino and vecino not in ruta_tabu:
                mejor_vecino = vecino
                mejor_costo_vecino = costo_vecino
        
        # Actualizamos la mejor ruta si encontramos un vecino mejor
        if mejor_costo_vecino < mejor_costo:
            mejor_ruta = mejor_vecino
            mejor_costo = mejor_costo_vecino
            ruta_actual = mejor_vecino[:]
        
        # Actualizamos la lista tabú
        ruta_tabu.append(mejor_vecino)
        
        # Incrementamos el contador de iteraciones
        iteraciones += 1
    
    return mejor_ruta

# Definimos la ubicación inicial y final en la ciudad
inicio = "A"
destino = "F"
# Definimos el número máximo de iteraciones tabú
iteraciones_tabu = 5
# Inicializamos la lista tabú
ruta_tabu = []

# Encontramos la mejor ruta usando búsqueda tabú
mejor_ruta = encontrar_mejor_ruta(ciudad, inicio, destino, iteraciones_tabu)

# Mostramos la mejor ruta encontrada
if mejor_ruta:
    print("La mejor ruta encontrada de", inicio, "a", destino, "es:", mejor_ruta)
else:
    print("No se encontró una ruta válida de", inicio, "a", destino)
