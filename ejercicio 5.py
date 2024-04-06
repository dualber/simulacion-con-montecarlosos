"""  
Un vendedor de tortas produce 50 tortas diarias a un costo de $1000/torta y las vende en un
centro comercial a un precio de $3000/torta. Las tortas que no vende las tiene que tirar al
final del día, sin embargo, el vendedor aún no tiene permiso del municipio para tirar el
producto en los basureros, por lo cual si llegan a descubrirlo tirando las tortas se le impondrá
una multa de $30,000.
La demanda de tortas tiene la siguiente distribución:
La probabilidad de que la policía descubra al vendedor tirando las tortas es del 25%. Con
base en la anterior información desarrolle un modelo de simulación para obtener la
siguiente información:a) Número medio de tortas no vendidas
b) Número medio de tortas que hay que botar
c) Utilidad media por día
d) Si el permiso para tirar las tortas al basurero cuesta $20,000 por semana, ¿conviene
conseguir el permiso o seguir tirando las tortas?
"""
from random import random

tortasDiarias = 50
precioTorta = 1000
ventaTorta = 3000
multa = 30000
permiso = 20000
dias=30
def demanda_diaria():
    D = random()
    if D < 0.1:
        return 10
    elif D < 0.30:
        return 20
    elif D < 0.60:
        return 25
    elif D < 0.80:
        return 30
    elif D < 0.90:
        return 50
    elif D < 0.96:
        return 70
    
    else:
        return 100

def utilidad_diaria():
    tortasNovendidas = 0
    demanda = demanda_diaria()
    print(demanda)
    if demanda <= tortasDiarias:
        utilidad = (demanda * ventaTorta) - (tortasDiarias * precioTorta) # 25*3000 - 50 * 1000 = 90000 - 50000 = 40000
        tortasNovendidas = tortasDiarias - demanda
        if(random() < 0.25):
          utilidad = (demanda * ventaTorta) - (tortasDiarias * precioTorta)-30000
          return utilidad,0,tortasNovendidas
        return utilidad,0,tortasNovendidas
    else:
        utilidad = (tortasDiarias * ventaTorta) - (tortasDiarias * precioTorta)# 50 * 3000 = 150000
        
    return utilidad,0,0

def utilidad_diariaConPermiso():
    tortasNovendidas = 0
    demanda = demanda_diaria()
    print(demanda)
    if demanda <= tortasDiarias:
        utilidad = (demanda * ventaTorta) - (tortasDiarias * precioTorta) # 25*3000 - 50 * 1000 = 90000 - 50000 = 40000
        tortasNovendidas = tortasDiarias - demanda
        return utilidad,0,tortasNovendidas
    else:
        utilidad = (tortasDiarias * ventaTorta) - (tortasDiarias * precioTorta)# 50 * 3000 = 150000
        
    return utilidad,0,0

utilidadMedia = 0
tortasNovendiadasTotal = 0
for i in range(dias):
    utilidad_dia,atrapado,tortasNovendiadas = utilidad_diaria()
    tortasNovendiadasTotal +=tortasNovendiadas 
    utilidadMedia += utilidad_dia

utilidadMediaC = 0
tortasNovendiadasTotalC = 0
for i in range(dias):
    utilidad_diaC,atrapadoC,tortasNoVendidasC = utilidad_diariaConPermiso()
    tortasNovendiadasTotalC +=tortasNoVendidasC 
    utilidadMediaC += utilidad_diaC   
    
print(f"utilidad media es {utilidadMedia}") #duda si hay que realizar la divicion entre el numero de dias
print(f"tortas no vendidas {int(tortasNovendiadasTotal/dias)}") 
print(f"utilidad media con permiso es {utilidadMediaC-80000}") #duda si hay que realizar la divicion entre el numero de dias
print(f"tortas no vendidas {int(tortasNovendiadasTotal/dias)}")
print(f"da igual si se compra el permiso o no {utilidadMediaC-80000 <= utilidadMedia}")


