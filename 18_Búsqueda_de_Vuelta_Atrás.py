# IvanL: Código de satisfacción de restricciones con búsqueda de vuelta atrás en Python para resolver un sudoku.

def backtrack_sudoku(sudoku):
    """
    IvanL: Función para resolver un sudoku utilizando búsqueda de vuelta atrás.
    
    Args:
    - sudoku: Lista de listas que representa el tablero de sudoku.
    
    Returns:
    - True si se encontró una solución, False si no.
    """
    # IvanL: Encuentra la próxima casilla vacía.
    next_empty = find_empty(sudoku)
    if not next_empty:
        return True  # IvanL: Si no hay casillas vacías, se ha resuelto el sudoku.
    
    row, col = next_empty
    
    # IvanL: Intenta colocar números del 1 al 9 en la casilla vacía.
    for num in range(1, 10):
        if is_valid(sudoku, num, row, col):
            sudoku[row][col] = num  # IvanL: Si el número es válido, lo coloca en la casilla.
            
            # IvanL: Realiza una búsqueda recursiva para intentar resolver el sudoku.
            if backtrack_sudoku(sudoku):
                return True
            
            # IvanL: Si no puede resolver el sudoku con este número, retrocede y prueba otro.
            sudoku[row][col] = 0
    
    return False  # IvanL: Si no se puede encontrar ninguna solución, devuelve False.

def find_empty(sudoku):
    """
    IvanL: Encuentra la próxima casilla vacía en el sudoku.
    
    Args:
    - sudoku: Lista de listas que representa el tablero de sudoku.
    
    Returns:
    - Tupla (fila, columna) de la próxima casilla vacía o None si no hay ninguna.
    """
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return (i, j)
    return None

def is_valid(sudoku, num, row, col):
    """
    IvanL: Verifica si un número dado es válido para colocar en una casilla específica del sudoku.
    
    Args:
    - sudoku: Lista de listas que representa el tablero de sudoku.
    - num: Número que se desea colocar en la casilla.
    - row: Fila de la casilla.
    - col: Columna de la casilla.
    
    Returns:
    - True si el número es válido para colocar en la casilla, False si no.
    """
    # IvanL: Verifica la fila.
    if num in sudoku[row]:
        return False
    
    # IvanL: Verifica la columna.
    for i in range(9):
        if sudoku[i][col] == num:
            return False
    
    # IvanL: Verifica el cuadrante 3x3.
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if sudoku[i][j] == num:
                return False
    
    return True

# IvanL: Ejemplo de uso del algoritmo para resolver un sudoku.
sudoku_board = [
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

if backtrack_sudoku(sudoku_board):
    print("Solución encontrada:")
    for row in sudoku_board:
        print(row)
else:
    print("No se encontró solución para este sudoku.")
