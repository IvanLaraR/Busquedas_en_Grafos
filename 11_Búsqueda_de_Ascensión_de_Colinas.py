# IvanL - Búsqueda Informada con Búsqueda de Ascensión de Colinas para encontrar el mejor restaurante en la ciudad

# Definimos la lista de restaurantes y sus calificaciones como un diccionario
restaurantes = {
    "Pizza Hut": 4.5,
    "McDonald's": 3.8,
    "Burger King": 4.2,
    "Subway": 4.0
}

# Función para encontrar el restaurante con la calificación más alta usando búsqueda de ascensión de colinas
def encontrar_mejor_restaurante(restaurantes):
    # Inicializamos el mejor restaurante y su calificación
    mejor_restaurante = None
    mejor_calificacion = 0
    
    # Iteramos sobre todos los restaurantes
    for restaurante, calificacion in restaurantes.items():
        # Si la calificación del restaurante actual es mayor que la mejor calificación actual
        if calificacion > mejor_calificacion:
            # Actualizamos el mejor restaurante y su calificación
            mejor_restaurante = restaurante
            mejor_calificacion = calificacion
            
    return mejor_restaurante

# Encontramos el mejor restaurante
mejor_restaurante = encontrar_mejor_restaurante(restaurantes)

# Mostramos el resultado
if mejor_restaurante:
    print("El mejor restaurante de la ciudad es:", mejor_restaurante)
else:
    print("No se encontró un mejor restaurante en la ciudad.")
