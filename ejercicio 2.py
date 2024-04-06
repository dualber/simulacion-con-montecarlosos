"""Andrés cuenta con una tienda para mascotas en el cual tiene una linda iniciativa para
ayudar a los perros sin hogar, y es que por cada 10 kg que sus clientes compren de su
marca de croquetas para perros el donará 2kg a los perros que están en la calle. Su
máquina para producir puede configurarse diariamente para una cantidad específica,
cambiarla implica riesgos de averías y altos tiempos en mantenimiento, a su vez esta la
configuración de sus ventas diarias:
• Prob Vender 05 paquetes de 10kg croquetas al día es 0,25
• Prob Vender: 10 paquetes de 10kg croquetas al día es 0,15
• Prob Vender: 12 paquetes de 10kg croquetas es 0,35
• Prob Vender :15 paquetes de 10kg croquetas es 0,125
• Prob Vender: 20 paquetes de 10kg croquetas es 0,125
El costo para Andrés de 1kg de croquetas es de $800 y lo vende a $1500, a su vez se tiene
en cuenta que su producto es perecedero asi entonces existe la probabilidad de un 0,45 de
que si le queda.
A) Se pide determinar qué cantidad debe configurar la máquina para obtener una ganancia
ideal cumpliendo la iniciativa.
B) El piensa que, si aumenta la donación a 4kg por cada 10kg vendido, sus ventas aumentaran
en un 20%. Teniendo en cuenta que su supuesto fue real. Le recomendaría realizar esta
opción. (Suponer que la cantidad producida es lo obtenido en el punto a)"""

from random import random

# Datos
costo = 800
venta = 1500
donacion = 2
donacion_nueva = 4
prob_perecedero = 0.45
cantidadIdealAcomprar =0

# generar demanda 

def demanda_diaria():
    D = random()
    if D < 0.25:
      return 5
    elif D < 0.40:
     return 10
    elif D < 0.75:
     return 12
    elif D < 0.875:
     return 15
    else:
     return 20
   
#utilidad diaria 
def utilidad_diaria(x_paquetes): 

 costo = 800
 venta = 1500# paquete 8 demanda 10
 demanda = demanda_diaria()
#  print(demanda)
 if demanda<=x_paquetes:  
        
        utilidad = (demanda*10*venta)-((costo*x_paquetes*10)+(costo * demanda * 2)) #(5*10*1500)-(800*5*10) = 785000
       
        return utilidad
 else:
        donacion = demanda*2
        utilidad = (x_paquetes*10*venta)-(costo*x_paquetes*12)
        return utilidad

#print(utilidad_diaria(8))

def utilidad_mensual(x):
    utilidad = 0
    for i in range(30):
        utilidad += utilidad_diaria(x)
    return utilidad

def utilidad_anual(x):
    
    utilidad_anual = 0
    for i in range(12):
        utilidad_anual += utilidad_mensual(x)
    return utilidad_anual
    
    
valore = [5,10,12,15,20]
for i in valore:
    print(f"{i}: {utilidad_anual(i):,.2f}")
    
    
