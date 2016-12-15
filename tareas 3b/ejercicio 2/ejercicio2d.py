#MARTHA ELENA NIEVES MORA
#LABORATORIO 3B
#EJERCICIO 2c



import matplotlib.pyplot as plt
import numpy as np
import math

x=np.linspace(0,2*math.pi,110)

y=(1+2*np.sin(x))*np.cos(x)
z=(1+2*np.sin(x))+np.sin(x)
plt.plot(x,y, linewidth=4, color='b', label='f(x)=(1+2*np.sin(x))*np.cos(x)')
plt.plot(x,z, linewidth=6, color='r', label='g(x)=(1+2*np.sin(x))+np.sin(x)')
plt.legend()
plt.title('ejercicio 2.d')
plt.xlabel('tiempo')
plt.ylabel('cm')
plt.grid(True)
plt.show()
