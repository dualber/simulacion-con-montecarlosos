from random import random

# Valores iniciales de las clases sociales
clase_alta = 300000
clase_media = 700000
clase_baja = 1000000

# Probabilidad de que el comercio con Senegal sea bueno
probabilidad_bueno = 0.45

# Impuestos por cambiar de clase
impuesto_baja_media = 500
impuesto_media_alta = 800

# Función para predecir si el comercio con Senegal será bueno o malo
def predecir_año():
    if random() < probabilidad_bueno:
        return 'bueno'
    else:
        return 'malo'

# Función para simular un año y calcular la recaudación de impuestos
def simular_año():
    global clase_alta, clase_media, clase_baja
    comercio = predecir_año()
    if comercio == 'bueno':
        clase_alta += 0.6 * clase_media
        clase_media *= 0.4
        impuestos_recaudados = 0.6 * clase_baja * impuesto_baja_media + 0.6 * clase_media * impuesto_media_alta
        clase_media += 0.6 * clase_baja
        clase_baja *= 0.4
    else:
        clase_baja += 0.5 * clase_media
        clase_media *= 0.5
        impuestos_recaudados = 0.5 * clase_media * impuesto_baja_media
        clase_media += 0.5 * clase_alta
        clase_alta *= 0.5
    return impuestos_recaudados

# Función para simular 20 años y calcular la recaudación total de impuestos
def simular_20_años():
    recaudacion_total = 0
    for _ in range(20):
        recaudacion_total += simular_año()
    return recaudacion_total

# Simulación de 20 años y cálculo de la recaudación total
recaudacion_total = simular_20_años()
print(f"La recaudación total de impuestos después de 20 años sería de ${recaudacion_total:,.2f}")
