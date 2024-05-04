# IvanL - Búsqueda Informada con Búsqueda Online para encontrar la mejor oferta en línea de productos electrónicos

# Definimos los productos electrónicos disponibles en diferentes tiendas en línea
productos = {
    "Laptop": {"Amazon": 1000, "eBay": 950, "BestBuy": 1050},
    "Teléfono": {"Amazon": 800, "eBay": 750, "BestBuy": 820},
    "Tableta": {"Amazon": 500, "eBay": 480, "BestBuy": 520}
}

# Función para encontrar la mejor oferta en línea para un producto específico
def encontrar_mejor_oferta(productos, producto):
    mejor_oferta = None
    mejor_precio = float('inf')
    for tienda, precio in productos[producto].items():
        if precio < mejor_precio:
            mejor_precio = precio
            mejor_oferta = tienda
    return mejor_oferta, mejor_precio

# Definimos el producto para el que queremos encontrar la mejor oferta
producto_deseado = "Laptop"

# Encontramos la mejor oferta en línea para el producto deseado
mejor_tienda, mejor_precio = encontrar_mejor_oferta(productos, producto_deseado)

# Mostramos la mejor oferta encontrada
print("La mejor oferta en línea para", producto_deseado, "es en", mejor_tienda, "por", mejor_precio, "dólares.")
