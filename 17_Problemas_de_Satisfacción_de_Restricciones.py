# IvanL - Satisfacción de Restricciones para asignar asientos en un avión

# Definimos los asientos del avión y las restricciones de asientos cercanos para pasajeros que viajan juntos
asientos = {
    1: ["A", "B", "C", "D"],
    2: ["A", "B", "C", "D"],
    3: ["A", "B", "C", "D"],
    4: ["A", "B", "C", "D"]
}

# Definimos las restricciones para pasajeros que viajan juntos y desean sentarse uno al lado del otro
restricciones = {
    "Juan": ["A", "B"],   # Juan quiere sentarse en los asientos A o B
    "María": ["C", "D"],  # María quiere sentarse en los asientos C o D
    "Carlos": ["B", "C"], # Carlos quiere sentarse en los asientos B o C
    "Laura": ["A", "D"]   # Laura quiere sentarse en los asientos A o D
}

# Función para verificar si una asignación de asientos cumple con todas las restricciones
def verificar_asignacion(asignacion, restricciones):
    for pasajero, asiento in asignacion.items():
        if asiento not in restricciones[pasajero]:
            return False
    return True

# Función para asignar los asientos a los pasajeros satisfaciendo todas las restricciones
def asignar_asientos(asientos, restricciones):
    asignacion = {}
    for fila, lista_asientos in asientos.items():
        for letra in lista_asientos:
            asignacion_posible = {pasajero: letra for pasajero in restricciones if letra in restricciones[pasajero]}
            if verificar_asignacion(asignacion_posible, restricciones):
                asignacion.update(asignacion_posible)
                return asignacion
    return None

# Asignamos los asientos a los pasajeros satisfaciendo todas las restricciones
asignacion_final = asignar_asientos(asientos, restricciones)

# Mostramos la asignación final de asientos
if asignacion_final:
    print("Asientos asignados satisfactoriamente:")
    for pasajero, asiento in asignacion_final.items():
        print(pasajero, "se sentará en el asiento", asiento)
else:
    print("No se pudo satisfacer todas las restricciones de asientos.")
