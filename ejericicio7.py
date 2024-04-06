import random

# Variables globales
CRI = 6000  # Costo por cada revista comprada al inicio del mes
CRF = 4800  # Costo por cada revista comprada para finales de mes
VRR = 3600  # Valor de la revista retornada
VRV = 8000  # Valor de la revista vendida
TS = 30  # Tiempo de simulación en días

# Funciones

def demanda_10_dias():
    """Simula la demanda de revistas en los primeros 10 días del mes."""
    return random.choices([5, 6, 7, 8, 9, 10, 11], weights=[5, 5, 10, 15, 25, 25, 15])[0]

def demanda_20_dias():
    """Simula la demanda de revistas en los siguientes 20 días del mes."""
    return random.choices([4, 5, 6, 7, 8], weights=[15, 20, 30, 20, 15])[0]

def simulacion_primeros_10_dias(revistas_iniciales):
    """Simula las ventas y sobrantes en los primeros 10 días."""
    demanda = demanda_10_dias()
    if revistas_iniciales <= demanda:
        return revistas_iniciales * VRV - revistas_iniciales * CRI, 0
    else:
        return demanda * VRV - revistas_iniciales * CRI, (revistas_iniciales - demanda)

def simulacion_ultimos_20_dias(sobrantes):
    """Simula las ventas en los últimos 20 días usando las revistas sobrantes."""
    demanda = demanda_20_dias()
    if sobrantes >= demanda:
        return demanda * VRV - demanda * CRI, sobrantes - demanda
    else:
        revistas_comprar = demanda - sobrantes
        return (sobrantes + revistas_comprar) * VRV - revistas_comprar * CRF, 0

def simulacion_mes(revistas_iniciales):
    """Simula todo el mes y devuelve las ganancias totales."""
    ganancias_10_dias, sobrantes = simulacion_primeros_10_dias(revistas_iniciales)
    ganancias_20_dias, sobrantes = simulacion_ultimos_20_dias(sobrantes)
    devolucion = sobrantes * VRR if sobrantes != 0 else 0
    ganancias_totales = ganancias_10_dias + ganancias_20_dias + devolucion
    return revistas_iniciales, ganancias_totales

def tabla_simulaciones():
    """Imprime una tabla con los resultados de la simulación para diferentes cantidades iniciales de revistas."""
    print("X\tVentas/10dias($)\tSobrante(10dias)\tVentas/20dias($)\tDevolucion($)\tTotal")
    for revistas_iniciales in [5, 6, 7, 8, 9, 10, 11]:
        _, ganancias_totales = simulacion_mes(revistas_iniciales)
        print(f"{revistas_iniciales}\t{ganancias_totales}")

# Simulación y presentación de resultados
tabla_simulaciones()