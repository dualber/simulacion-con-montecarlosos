"""
    Gambia es un país africano en el cual viven aproximadamente 2 millones de habitantes de
los cuales el gobierno ha calificado las familias en 3 clases sociales dependiendo de su
situación económica (Baja, media y alta), por experiencia de años anteriores se sabe que si
el comercio con Senegal es bueno la probabilidad de pasar de una clase siguiente a otra en
un año es 0.6 y de mantenerse en alta es 1, además con esta característica no hay un
retroceso en las clases. Ahora bien, si el comercio con Senegal no es bueno la probabilidad
que una familia permanezca en clase baja es total, y pasar de una clase a una inferior es 0.5,
en esta situación no es posible avanzar a una clase superior.
El gobierno de Gambia está preocupado por esta situación debido a que, de los últimos 20
años, solo se ha tenido 9 años de bueno comercio con Senegal, dada esta situación los
dirigentes quieren saber:
A) ¿Cuánto recaudarían después de 20 años si colocan un impuesto de pasar de clase baja
a media de $500 USD y de media a alta de $800 USD? En el momento que le piden
realizar la simulación existe la siguiente configuración de las personas en las clases
sociales: 1’000.000 en clase baja; 700.000 en clase media y 300.000 en clase alta.
    """
    
from random import random

clase_alta = 300000
clase_media = 700000
clase_baja = 1000000


impuesto_baja_media = 0
impuesto_media_alta = 0

def predeciraño():
    
    
    año = random()
    if año < 0.45:
        return 1
    else:
        return 0

def recaudacionAnual():
    global clase_alta
    global clase_media
    global clase_baja
    global impuesto_baja_media 
    global impuesto_media_alta 
    for i in range(20):
        n=predeciraño()
        print(n)
        if(n == 1):
            clase_alta = clase_alta + 0.6*clase_media 
            impuesto_media_alta += (0.6*clase_media)*800
            clase_media =  clase_media*0.4
            impuesto_baja_media += (0.6*clase_baja)*500           
            clase_media = clase_media + 0.6*clase_baja 
            clase_baja = clase_baja - 0.6*clase_baja   
            
        
            print(f"impuestosMA:{impuesto_media_alta:,.2f}")
            print(f"impuestosBA:{impuesto_baja_media:,.2f}")
            
            print("clase baja",clase_baja)
            print("calse media",clase_media)
            print("clase alta",clase_alta)
            print("total clases",clase_baja+clase_media+clase_alta)
            #return impuesto_media_alta,impuesto_baja_media
        else:
            clase_baja = clase_baja + (0.5*clase_media)
            clase_media = clase_media - 0.5*clase_media
            clase_media = clase_media + 0.5*clase_alta
            clase_alta = clase_alta - 0.5*clase_alta     
            
            print("clase baja",clase_baja)
            print("calse media",clase_media)
            print("clase alta",clase_alta)
            print("total clases",clase_baja+clase_media+clase_alta)
    print(f"impuestoMATOTAL:{impuesto_media_alta:,.2f}")
    print(f"impuestoBMTOTAL:{impuesto_baja_media:,.2f}")
    print(f"impuestoTOTAL:{impuesto_baja_media+impuesto_media_alta:,.2f}")
    
                
recaudacionAnual()

    