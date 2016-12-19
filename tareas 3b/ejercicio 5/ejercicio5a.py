#MARTHA ELENA NIEVES MORA
#LABORATORIO 3B
#EJERCICIO 5a



import matplotlib.pyplot as plt
import numpy as np
import math

k=np.linspace(0,2*math.pi,100)
r=2-2*np.sin(k)+np.sin(k)*(np.sqrt(np.absolute(np.cos(k))))/(np.sin(k)+1.4)
x=r*np.cos(k)
y=r*np.sin(k)
plt.plot(x,y, linewidth=10, color='b', label='HEART')
plt.legend()
plt.title('ejercicio 5.a')
plt.xlabel('tiempo')
plt.ylabel('cm')
plt.grid(True)
plt.show()
