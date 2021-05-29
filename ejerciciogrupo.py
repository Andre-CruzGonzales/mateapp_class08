import matplotlib.pyplot as plt
import numpy as np

x=[5,10,15,20,25,30,35,40,45,50,]
y=[9,5,6,3,9,5,1,8,4,2]


plt.scatter(x,y, c="blue", alpha=0.9)
plt.xlabel("METROS DE DISTANCIA")
plt.ylabel("ZONAS AFECTADAS")
plt.legend("DISTANCIA")
plt.show()


