# IvanL - Búsqueda Informada con Búsqueda de Haz Local para encontrar el mejor lugar para estacionarse en un centro comercial

# Definimos el centro comercial como un mapa de espacios de estacionamiento
# Cada espacio tiene una calificación que representa la conveniencia del lugar (mayor es mejor)
centro_comercial = {
    "A": 8, "B": 5, "C": 7, "D": 6, "E": 9,  # Piso 1
    "F": 7, "G": 6, "H": 4, "I": 8, "J": 5   # Piso 2
}

# Función para encontrar el mejor espacio de estacionamiento usando Búsqueda de Haz Local
def encontrar_mejor_estacionamiento(centro_comercial, piso, numero_haces, ancho_haz):
    # Seleccionamos los espacios de estacionamiento del piso especificado
    espacios_piso = {k: v for k, v in centro_comercial.items() if k[0] == piso}
    # Ordenamos los espacios de estacionamiento por calificación de manera descendente
    espacios_ordenados = sorted(espacios_piso.items(), key=lambda x: x[1], reverse=True)
    
    # Inicializamos la lista de candidatos con los primeros espacios de estacionamiento
    candidatos = espacios_ordenados[:numero_haces * ancho_haz]
    
    # Iteramos hasta encontrar el mejor espacio de estacionamiento
    while True:
        mejor_espacio = max(candidatos, key=lambda x: x[1])
        # Si el mejor espacio de estacionamiento es el más cercano al centro, lo seleccionamos
        if mejor_espacio[0] == piso + str(ancho_haz // 2 + 1):
            return mejor_espacio[0]
        else:
            # Expandimos el conjunto de candidatos
            indice_mejor_espacio = espacios_ordenados.index(mejor_espacio)
            nuevos_candidatos = espacios_ordenados[max(0, indice_mejor_espacio - ancho_haz):indice_mejor_espacio + ancho_haz]
            # Actualizamos la lista de candidatos
            candidatos = [x for x in nuevos_candidatos if x[0][0] == piso]

# Especificamos el piso donde deseamos estacionarnos
piso_deseado = "B"
# Especificamos el número de haces que exploraremos
numero_haces = 3
# Especificamos el ancho de cada haz
ancho_haz = 3

# Encontramos el mejor espacio de estacionamiento en el piso deseado usando Búsqueda de Haz Local
mejor_estacionamiento = encontrar_mejor_estacionamiento(centro_comercial, piso_deseado, numero_haces, ancho_haz)

# Mostramos el mejor espacio de estacionamiento encontrado
print("El mejor espacio de estacionamiento en el piso", piso_deseado, "es:", mejor_estacionamiento)
