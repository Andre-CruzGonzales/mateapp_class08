import numpy as np
import matplotlib.pyplot as plt
x = np.random.randint(1,100, size=20)
#print(x)
y = np.random.randint(50,280, size=20)
plt.scatter(x,y)
plt.show()