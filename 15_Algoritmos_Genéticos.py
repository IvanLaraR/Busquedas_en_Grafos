# IvanL - Búsqueda Informada con Algoritmos Genéticos para encontrar la mejor receta de pizza

# Definimos la población inicial como un conjunto de recetas de pizza representadas por ingredientes y cantidades
poblacion_inicial = [
    {"harina": 200, "agua": 100, "levadura": 10, "sal": 5, "tomate": 150, "queso": 200, "pepperoni": 100},
    {"harina": 220, "agua": 110, "levadura": 12, "sal": 6, "tomate": 170, "queso": 220, "jamón": 120},
    {"harina": 180, "agua": 90, "levadura": 8, "sal": 4, "tomate": 130, "queso": 180, "champiñones": 80},
    {"harina": 240, "agua": 120, "levadura": 15, "sal": 7, "tomate": 200, "queso": 250, "pimientos": 90}
]

# Función para calcular la aptitud de una receta de pizza basada en su sabor y textura
def calcular_aptitud(receta):
    sabor = sum(receta.values())  # La suma total de los ingredientes determina el sabor
    textura = len(receta)  # El número de ingredientes determina la textura
    return sabor + textura

# Función para seleccionar los padres más aptos para la reproducción
def seleccionar_padres(poblacion, num_padres):
    padres = []
    poblacion_ordenada = sorted(poblacion, key=lambda x: calcular_aptitud(x), reverse=True)
    for i in range(num_padres):
        padres.append(poblacion_ordenada[i])
    return padres

# Función para cruzar los genes de dos padres y generar descendencia
def cruzar(padre1, padre2):
    descendencia = {}
    genes_padre1 = list(padre1.keys())
    genes_padre2 = list(padre2.keys())
    genes_comunes = set(genes_padre1) & set(genes_padre2)
    genes_distintos = set(genes_padre1) ^ set(genes_padre2)
    for gen in genes_comunes:
        descendencia[gen] = (padre1[gen] + padre2[gen]) // 2
    for gen in genes_distintos:
        if gen in genes_padre1:
            descendencia[gen] = padre1[gen]
        else:
            descendencia[gen] = padre2[gen]
    return descendencia

# Función para mutar la descendencia introduciendo pequeñas variaciones en los genes
def mutar(descendencia, probabilidad_mutacion):
    import random
    for gen in descendencia:
        if random.random() < probabilidad_mutacion:
            descendencia[gen] += random.randint(-5, 5)  # Variación aleatoria entre -5 y 5
    return descendencia

# Definimos los parámetros del algoritmo genético
num_generaciones = 10
tamano_poblacion = 4
num_padres = 2
probabilidad_mutacion = 0.1

# Ejecutamos el algoritmo genético para encontrar la mejor receta de pizza
for generacion in range(num_generaciones):
    print("Generación", generacion + 1)
    poblacion_seleccionada = seleccionar_padres(poblacion_inicial, num_padres)
    nueva_generacion = []
    for _ in range(tamano_poblacion - num_padres):
        padre1 = poblacion_seleccionada[0]
        padre2 = poblacion_seleccionada[1]
        descendencia = cruzar(padre1, padre2)
        descendencia_mutada = mutar(descendencia, probabilidad_mutacion)
        nueva_generacion.append(descendencia_mutada)
    poblacion_inicial = poblacion_seleccionada + nueva_generacion

# Mostramos la mejor receta de pizza encontrada
mejor_receta = max(poblacion_inicial, key=lambda x: calcular_aptitud(x))
print("La mejor receta de pizza encontrada es:", mejor_receta)
