from random import random

# Parámetros dados
costo_anual_por_auto = 11000000
costoDiarioXNAuto = 30000
costoDiarioAutoOcioso = 7500

def demandaDeAutos():
    D = random()
    if D < 0.1:
        return 0
    elif D < 0.2:
        return 1
    elif D < 0.45:
        return 2
    elif D < 0.75:
        return 3
    else:
        return 4

def demandaDiasAlquilados():
    D = random()
    if D < 0.4:
        return 1
    elif D < 0.75:
        return 2
    elif D < 0.90:
        return 3
    else:
        return 4

def autosDisponibles(vec):
    for x in vec:
        # Aquí puedes realizar alguna operación con cada elemento del vector
         x
        # Puedes agregar más lógica aquí según lo que desees hacer con cada valor de 'vec'
    return vec

# Inicialización de variables
vec =[1,2,3,4]
ganaciaAnual=0

for i in range(360):
    autos=autosDisponibles(vec)
    demanda=demandaDeAutos()
    ganancia = 0
    gananciaTotal = 0
    costosPorAusencia = 0
    costoFautos = 0
    #print(f"La demanda de autos es: {demanda}")
    #print(f"Los autos disponibles son: {autos}")
    if(autos>demanda):
        if(demanda==0):
            gananciaP=0 # si la demanda es cero la ganancia es cero
            costoFautos=costoDiarioAutoOcioso*autos
        else:   
            for i in range(demanda): #DEMANDA = 3 autos disponibles = 2 
                nDias=demandaDiasAlquilados()
                gananciaP=52000*nDias #la ganacia se multiplica por el numero de dias alquilados
                ganancia+=gananciaP
                #print(f"el auto {i} tiene una demanda de: {nDias} dias")
            costoFautos =(autos-demanda)*costoDiarioAutoOcioso  # el costo por autos ociosos se multiplica por el numero de autos ociosos
            
    else:
        for i in range(autos): #autos=2
            nDias=demandaDiasAlquilados()
            gananciaP=52000*nDias  #52000*3 
            ganancia+=gananciaP # 0+52000*3 = 156000 + 52000*2 = 260000
            #print(f"el auto {i} tiene una demanda de: {nDias} dias") #nDias numeros de dias que se alquila el auto
        costosPorAusencia=(demanda-autos)*costoDiarioXNAuto       
            
    gananciaTotal=ganancia-costosPorAusencia-costoFautos
    #print(f"Los costos por ausencia de autos son: {costosPorAusencia}")
    #print(f"La ganancia es: {ganancia}")
    #print(f"El costo por autos ociosos es: {costoFautos}")
    #print(f"La ganancia total es: {ganancia-costosPorAusencia-costoFautos}")
    ganaciaAnual+=gananciaTotal

print(f"La ganancia anual es: {ganaciaAnual}")