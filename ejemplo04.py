import numpy  as np
import matplotlib.pyplot as plt

x=np.random.randint(1,51,20)
y= np.random.randint(1,51,20)
x1=np.random.randint(1,51,20)
y1= np.random.randint(1,51,20)
x2=np.random.randint(1,51,20)
y2= np.random.randint(1,51,20)
colors=np.random.rand(20)
area=np.pi * (np.random.randint(1,25,20))**2

plt.scatter(x,y)

plt.scatter(x1,y1,s=area) #s nueva dispersion con diferente area de grafica.

plt.scatter(x2,y2,s=area,c=colors,alpha=0.5)

plt.show()