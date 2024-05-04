# IvanL: Código de satisfacción de restricciones con salto atrás dirigido por conflictos en Python para resolver un crucigrama.

def resolver_crucigrama(letras_disponibles, palabras, restricciones):
    """
    IvanL: Función para resolver un crucigrama utilizando salto atrás dirigido por conflictos.

    Args:
    - letras_disponibles: Lista de letras disponibles para completar el crucigrama.
    - palabras: Lista de palabras del crucigrama y sus posiciones.
    - restricciones: Diccionario que mapea letras a las restricciones de las palabras.

    Returns:
    - Lista de palabras completadas con sus posiciones, o None si no se puede resolver.
    """
    palabras_completadas = {}  # IvanL: Diccionario para almacenar las palabras completadas con sus posiciones.

    for palabra, posicion in palabras:
        if palabra not in palabras_completadas:
            palabras_completadas[palabra] = posicion

            # IvanL: Aplica la propagación de restricciones para eliminar platos prohibidos en otros días.
            for otra_palabra, otra_posicion in palabras:
                if otra_palabra != palabra and not es_compatible(palabra, posicion, otra_palabra, otra_posicion):
                    return None  # IvanL: Si se viola una restricción, no se puede planificar el menú.
    
    return palabras_completadas  # IvanL: Devuelve las palabras completadas con sus posiciones.

def es_compatible(palabra1, posicion1, palabra2, posicion2):
    """
    IvanL: Verifica si dos palabras son compatibles según sus posiciones.

    Args:
    - palabra1: Primera palabra a comparar.
    - posicion1: Posición de la primera palabra.
    - palabra2: Segunda palabra a comparar.
    - posicion2: Posición de la segunda palabra.

    Returns:
    - True si las palabras son compatibles, False si no.
    """
    for letra, index in zip(palabra1, posicion1):
        if letra in palabra2:
            if index != posicion2[palabra2.index(letra)]:
                return False
    return True  # IvanL: Si no se viola ninguna restricción, las palabras son compatibles.

# IvanL: Ejemplo de uso del algoritmo para resolver un crucigrama.
letras_disponibles = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
palabras_crucigrama = [('CARRO', (0, 0)), ('CASA', (0, 2)), ('CABEZA', (0, 4)), ('FARO', (2, 0)), ('FLOR', (2, 2))]
restricciones_letras = {'R': ['F'], 'L': ['A', 'F']}

resultado = resolver_crucigrama(letras_disponibles, palabras_crucigrama, restricciones_letras)
if resultado:
    print("Crucigrama resuelto:")
    for palabra, posicion in resultado.items():
        print(f"{palabra}: {posicion}")
else:
    print("No se puede resolver el crucigrama con las letras disponibles y las restricciones dadas.")
