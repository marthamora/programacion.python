#MARTHA ELENA NIEVES MORA
#LABORATORIO 3B
#EJERCICIO 5b



import matplotlib.pyplot as plt
import numpy as np
import math

x=np.linspace(0,2*math.pi,100)
r=2-2*np.sin(x)+np.sin(x)*(np.sqrt(np.absolute(np.cos(x))))/(np.sin(x)+1.4)
y=r*np.cos(x)
z=r*np.sin(x)
plt.plot(y,z, linewidth=10, color='b', label='HEART')
plt.legend()
plt.title('ejercicio 5.b')
plt.xlabel('tiempo')
plt.ylabel('cm')
plt.fill_between(y,z,color='r')
plt.grid(True)
plt.show()
