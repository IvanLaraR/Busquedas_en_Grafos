# IvanL - Búsqueda Informada con Temple Simulado para encontrar la mejor ruta en una ciudad congestionada

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

# Función para generar un vecino intercambiando dos nodos aleatorios de la ruta
def generar_vecino_aleatorio(ruta):
    import random
    # Seleccionamos dos índices aleatorios distintos
    i, j = random.sample(range(len(ruta)), 2)
    # Intercambiamos los nodos en los índices seleccionados
    ruta[i], ruta[j] = ruta[j], ruta[i]
    return ruta

# Función para encontrar la mejor ruta usando Temple Simulado
def encontrar_mejor_ruta_temple_simulado(ciudad, ruta_inicial, temperatura_inicial, factor_enfriamiento, iteraciones_max):
    ruta_actual = ruta_inicial
    costo_actual = calcular_costo_total(ruta_actual)
    mejor_ruta = ruta_actual[:]
    mejor_costo = costo_actual
    temperatura_actual = temperatura_inicial
    
    for i in range(iteraciones_max):
        # Generamos un vecino aleatorio
        vecino = generar_vecino_aleatorio(ruta_actual[:])
        costo_vecino = calcular_costo_total(vecino)
        
        # Si el vecino es mejor o es aceptado según la probabilidad de Boltzmann
        if costo_vecino < costo_actual or random.random() < temperatura_actual / temperatura_inicial:
            ruta_actual = vecino[:]
            costo_actual = costo_vecino
            
            # Si el vecino es mejor que la mejor ruta encontrada hasta ahora
            if costo_actual < mejor_costo:
                mejor_ruta = ruta_actual[:]
                mejor_costo = costo_actual
        
        # Enfriamos la temperatura
        temperatura_actual *= factor_enfriamiento
    
    return mejor_ruta

# Definimos la ubicación inicial y final en la ciudad
inicio = "A"
destino = "F"
# Definimos los parámetros del Temple Simulado
temperatura_inicial = 100.0
factor_enfriamiento = 0.95
iteraciones_max = 1000
# Definimos una ruta inicial aleatoria
import random
ruta_inicial = list(ciudad.keys())
random.shuffle(ruta_inicial)

# Encontramos la mejor ruta usando Temple Simulado
mejor_ruta_temple_simulado = encontrar_mejor_ruta_temple_simulado(ciudad, ruta_inicial, temperatura_inicial, factor_enfriamiento, iteraciones_max)

# Mostramos la mejor ruta encontrada
if mejor_ruta_temple_simulado:
    print("La mejor ruta encontrada de", inicio, "a", destino, "usando Temple Simulado es:", mejor_ruta_temple_simulado)
else:
    print("No se encontró una ruta válida de", inicio, "a", destino, "usando Temple Simulado.")
