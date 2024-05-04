# IvanL - Búsqueda Bidireccional para encontrar un amigo en una multitud

# Definimos la multitud como una lista de personas donde cada persona tiene una ubicación (x, y)
multitud = [
    {"nombre": "Juan", "ubicacion": (0, 0)},
    {"nombre": "Maria", "ubicacion": (1, 2)},
    {"nombre": "Pedro", "ubicacion": (2, 3)},
    {"nombre": "Ana", "ubicacion": (3, 4)},
    {"nombre": "Luis", "ubicacion": (4, 5)}
]

# Definimos la ubicación inicial y final para la búsqueda bidireccional
ubicacion_inicial = (0, 0)
ubicacion_final = (4, 5)

# Función para verificar si dos ubicaciones son adyacentes
def son_adyacentes(ubicacion1, ubicacion2):
    return abs(ubicacion1[0] - ubicacion2[0]) + abs(ubicacion1[1] - ubicacion2[1]) == 1

# Función para encontrar el amigo usando búsqueda bidireccional
def buscar_amigo():
    # Inicializamos las listas de exploración desde la ubicación inicial y final
    exploracion_inicio = [ubicacion_inicial]
    exploracion_final = [ubicacion_final]
    # Inicializamos los conjuntos de nodos visitados desde la ubicación inicial y final
    visitados_inicio = {ubicacion_inicial}
    visitados_final = {ubicacion_final}
    
    # Mientras haya nodos por explorar en ambas direcciones
    while exploracion_inicio and exploracion_final:
        # Verificamos si hay intersección entre los nodos visitados en ambas direcciones
        interseccion = visitados_inicio.intersection(visitados_final)
        if interseccion:
            # Si hay intersección, retornamos el punto de encuentro
            punto_encuentro = interseccion.pop()
            return punto_encuentro
        
        # Expandimos un paso en la dirección desde la ubicación inicial
        nuevos_nodos_inicio = []
        for ubicacion in exploracion_inicio:
            for vecino in obtener_vecinos(ubicacion):
                if vecino not in visitados_inicio:
                    nuevos_nodos_inicio.append(vecino)
                    visitados_inicio.add(vecino)
        exploracion_inicio = nuevos_nodos_inicio
        
        # Expandimos un paso en la dirección desde la ubicación final
        nuevos_nodos_final = []
        for ubicacion in exploracion_final:
            for vecino in obtener_vecinos(ubicacion):
                if vecino not in visitados_final:
                    nuevos_nodos_final.append(vecino)
                    visitados_final.add(vecino)
        exploracion_final = nuevos_nodos_final
        
    # Si no se encuentra el amigo en la multitud
    return None

# Función para obtener los vecinos de una ubicación
def obtener_vecinos(ubicacion):
    vecinos = []
    for persona in multitud:
        if son_adyacentes(persona["ubicacion"], ubicacion):
            vecinos.append(persona["ubicacion"])
    return vecinos

# Realizamos la búsqueda del amigo
ubicacion_amigo = buscar_amigo()

# Si se encuentra al amigo, mostramos su ubicación
if ubicacion_amigo:
    for persona in multitud:
        if persona["ubicacion"] == ubicacion_amigo:
            print("¡Encontramos a nuestro amigo", persona["nombre"], "en la ubicación:", ubicacion_amigo, "!")
else:
    print("No encontramos a nuestro amigo en la multitud.")
