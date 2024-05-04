# IvanL - Búsqueda Informada con Búsqueda Voraz Primero el Mejor para encontrar el restaurante más cercano

# Definimos los restaurantes y sus ubicaciones como un diccionario
restaurantes = {
    "Pizza Hut": (2, 5),
    "McDonald's": (4, 3),
    "Burger King": (1, 2),
    "Subway": (3, 4)
}

# Ubicación inicial del usuario
ubicacion_usuario = (0, 0)

# Función para calcular la distancia Euclidiana entre dos ubicaciones
def calcular_distancia(ubicacion1, ubicacion2):
    x1, y1 = ubicacion1
    x2, y2 = ubicacion2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Función para encontrar el restaurante más cercano usando búsqueda voraz primero el mejor
def encontrar_restaurante_cercano(ubicacion_usuario, restaurantes):
    # Inicializamos el restaurante más cercano y su distancia
    restaurante_cercano = None
    distancia_minima = float('inf')  # Inicializamos la distancia mínima como infinito
    
    # Iteramos sobre todos los restaurantes
    for restaurante, ubicacion_restaurante in restaurantes.items():
        # Calculamos la distancia entre el usuario y el restaurante actual
        distancia = calcular_distancia(ubicacion_usuario, ubicacion_restaurante)
        # Si la distancia es menor que la distancia mínima actual
        if distancia < distancia_minima:
            # Actualizamos el restaurante más cercano y la distancia mínima
            restaurante_cercano = restaurante
            distancia_minima = distancia
            
    return restaurante_cercano

# Encontramos el restaurante más cercano
restaurante_cercano = encontrar_restaurante_cercano(ubicacion_usuario, restaurantes)

# Mostramos el resultado
if restaurante_cercano:
    print("El restaurante más cercano es:", restaurante_cercano)
else:
    print("No hay restaurantes cerca.")
