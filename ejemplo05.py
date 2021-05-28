'''
los datos dados en el csv, representa el numero de cambios de aceite al año y costo
de la reparacion (en miles de soles), de una muestra de 20 autos de una cierta marca y modelo
a. realiza la grafica de dispersion
'''
import csv
import matplotlib.pyplot as plt
import numpy as np

costo=[]#variable dependiente y
cambio_aceite=[] #variable independiente x

with open("datos.csv", encoding='utf-8',newline='') as f:
    #reader = csv.reader(f)
    reader = enumerate(csv.reader(f))
    
    for i, row in reader:
        if i>0:
            try:
                costo.append(int(row[0]))
                cambio_aceite.append(int(row[1]))
            except Exception:
                print(Exception)

#plt.scatter(cambio_aceite,costo,c="g",alpha=0.5,marker=r'$\clubsuit$',label="luck",s=100)
plt.scatter(cambio_aceite,costo,c="g",alpha=0.5,s=100)

plt.xlabel("Cambio de Aceite")
plt.ylabel("Costo")

plt.show()