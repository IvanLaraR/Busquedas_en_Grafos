
from collections import deque

def buscar_en_anchura(grafo, inicio, meta):
    # Una cola para manejar los nodos pendientes de revisar
    cola = deque([[inicio]])
    
    # Un conjunto para evitar revisitar nodos
    visitados = set()
    
    while cola:
        # Tomamos el primer camino en la cola
        camino = cola.popleft()
        # El último nodo en el camino actual
        nodo = camino[-1]
        
        if nodo in visitados:
            continue
        
        # Marcar como visitado
        visitados.add(nodo)
        
        # Verificar si es el nodo que buscamos
        if nodo == meta:
            return camino
        
        # Agregar todos los vecinos no visitados al final del camino y encolar
        for vecino in grafo.get(nodo, []):
            nuevo_camino = list(camino)
            nuevo_camino.append(vecino)
            cola.append(nuevo_camino)
    
    # Si la cola se vacía, significa que no hay camino
    return None

# Ejemplo de un grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Intento de encontrar un camino de A a F
camino = buscar_en_anchura(grafo, 'A', 'F')
if camino:
    print("Camino encontrado:", ' -> '.join(camino))
else:
    print("No hay camino.")
