# IvanL: Código de Teoría de Juegos en Python para encontrar equilibrios y mecanismos en situaciones de toma de decisiones estratégicas.

def encontrar_equilibrio(mecanismo, estrategias_jugador1, estrategias_jugador2):
    """
    IvanL: Función para encontrar el equilibrio en un juego de dos jugadores.

    Args:
    - mecanismo: Función que define las reglas y la lógica del juego.
    - estrategias_jugador1: Lista de estrategias disponibles para el jugador 1.
    - estrategias_jugador2: Lista de estrategias disponibles para el jugador 2.

    Returns:
    - Equilibrio del juego.
    """
    for estrategia_jugador1 in estrategias_jugador1:
        for estrategia_jugador2 in estrategias_jugador2:
            if mecanismo(estrategia_jugador1, estrategia_jugador2):
                return estrategia_jugador1, estrategia_jugador2
    return None, None

def juego_simple(estrategia_jugador1, estrategia_jugador2):
    """
    IvanL: Función que define las reglas de un juego simple entre dos jugadores.

    Args:
    - estrategia_jugador1: Estrategia elegida por el jugador 1.
    - estrategia_jugador2: Estrategia elegida por el jugador 2.

    Returns:
    - True si las estrategias forman un equilibrio, False de lo contrario.
    """
    if estrategia_jugador1 == 'Cooperar' and estrategia_jugador2 == 'Cooperar':
        return True
    elif estrategia_jugador1 == 'Traicionar' and estrategia_jugador2 == 'Traicionar':
        return True
    else:
        return False

# IvanL: Ejemplo de uso del algoritmo para encontrar el equilibrio en un juego simple.
estrategias_jugador1 = ['Cooperar', 'Traicionar']  # IvanL: Estrategias disponibles para el jugador 1.
estrategias_jugador2 = ['Cooperar', 'Traicionar']  # IvanL: Estrategias disponibles para el jugador 2.

equilibrio_jugador1, equilibrio_jugador2 = encontrar_equilibrio(juego_simple, estrategias_jugador1, estrategias_jugador2)

if equilibrio_jugador1 is not None:
    print(f"Equilibrio encontrado: Jugador 1 elige {equilibrio_jugador1}, Jugador 2 elige {equilibrio_jugador2}")
else:
    print("No se encontró equilibrio en el juego.")
