# IvanL: Código de satisfacción de restricciones con búsqueda local: mínimos-conflictos en Python para resolver un Sudoku.

import random

def resolver_sudoku(sudoku):
    """
    IvanL: Función para resolver un Sudoku utilizando búsqueda local: mínimos-conflictos.

    Args:
    - sudoku: Lista de listas que representa el tablero de Sudoku.

    Returns:
    - Tablero de Sudoku resuelto, o None si no se puede resolver.
    """
    for _ in range(1000):  # IvanL: Intenta resolver el Sudoku hasta 1000 veces.
        if verificar_sudoku(sudoku):
            return sudoku  # IvanL: Devuelve el Sudoku resuelto si es válido.

        # IvanL: Encuentra la casilla con más conflictos.
        fila, columna = encontrar_casilla_conflictiva(sudoku)

        # IvanL: Encuentra el valor que minimiza los conflictos en la casilla.
        valor_min_conflictos = encontrar_valor_min_conflictos(sudoku, fila, columna)

        # IvanL: Coloca el valor que minimiza los conflictos en la casilla.
        sudoku[fila][columna] = valor_min_conflictos

    return None  # IvanL: Devuelve None si no se puede resolver el Sudoku.

def verificar_sudoku(sudoku):
    """
    IvanL: Verifica si un Sudoku está completo y es válido.

    Args:
    - sudoku: Lista de listas que representa el tablero de Sudoku.

    Returns:
    - True si el Sudoku es válido, False si no.
    """
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0 or not es_valido(sudoku, i, j):
                return False
    return True  # IvanL: Devuelve True si el Sudoku es válido.

def es_valido(sudoku, fila, columna):
    """
    IvanL: Verifica si un valor en una casilla de Sudoku es válido.

    Args:
    - sudoku: Lista de listas que representa el tablero de Sudoku.
    - fila: Índice de fila de la casilla.
    - columna: Índice de columna de la casilla.

    Returns:
    - True si el valor es válido en la casilla, False si no.
    """
    valor = sudoku[fila][columna]

    # IvanL: Verifica la fila y la columna.
    for i in range(9):
        if i != columna and sudoku[fila][i] == valor:
            return False
        if i != fila and sudoku[i][columna] == valor:
            return False

    # IvanL: Verifica el cuadrante 3x3.
    start_row, start_col = 3 * (fila // 3), 3 * (columna // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if i != fila and j != columna and sudoku[i][j] == valor:
                return False

    return True  # IvanL: Devuelve True si el valor es válido.

def encontrar_casilla_conflictiva(sudoku):
    """
    IvanL: Encuentra la casilla con más conflictos en el Sudoku.

    Args:
    - sudoku: Lista de listas que representa el tablero de Sudoku.

    Returns:
    - Índices de fila y columna de la casilla con más conflictos.
    """
    max_conflictos = 0
    fila_conflictiva = 0
    columna_conflictiva = 0

    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                conflictos = contar_conflictos(sudoku, i, j)
                if conflictos > max_conflictos:
                    max_conflictos = conflictos
                    fila_conflictiva = i
                    columna_conflictiva = j

    return fila_conflictiva, columna_conflictiva

def contar_conflictos(sudoku, fila, columna):
    """
    IvanL: Cuenta la cantidad de conflictos en una casilla de Sudoku.

    Args:
    - sudoku: Lista de listas que representa el tablero de Sudoku.
    - fila: Índice de fila de la casilla.
    - columna: Índice de columna de la casilla.

    Returns:
    - Cantidad de conflictos en la casilla.
    """
    conflictos = 0
    valor = sudoku[fila][columna]

    # IvanL: Cuenta los conflictos en la fila y la columna.
    for i in range(9):
        if i != columna and sudoku[fila][i] == valor:
            conflictos += 1
        if i != fila and sudoku[i][columna] == valor:
            conflictos += 1

    # IvanL: Cuenta los conflictos en el cuadrante 3x3.
    start_row, start_col = 3 * (fila // 3), 3 * (columna // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if i != fila and j != columna and sudoku[i][j] == valor:
                conflictos += 1

    return conflictos

def encontrar_valor_min_conflictos(sudoku, fila, columna):
    """
    IvanL: Encuentra el valor que minimiza los conflictos en una casilla de Sudoku.

    Args:
    - sudoku: Lista de listas que representa el tablero de Sudoku.
    - fila: Índice de fila de la casilla.
    - columna: Índice de columna de la casilla.

    Returns:
    - Valor que minimiza los conflictos en la casilla.
    """
    valores_disponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(valores_disponibles)  # IvanL: Mezcla los valores disponibles para evitar sesgos.

    min_conflictos = 9
    valor_min_conflictos = 0

    for valor in valores_disponibles:
        sudoku[fila][columna] = valor
        conflictos = contar_conflictos(sudoku, fila, columna)
        if conflictos < min_conflictos:
            min_conflictos = conflictos
            valor_min_conflictos = valor

    return valor_min_conflictos

# IvanL: Ejemplo de uso del algoritmo para resolver un Sudoku.
sudoku_a_resolver = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

sudoku_resuelto = resolver_sudoku(sudoku_a_resolver)

if sudoku_resuelto:
    print("Sudoku resuelto:")
    for fila in sudoku_resuelto:
        print(fila)
else:
    print("No se pudo resolver el Sudoku.")
