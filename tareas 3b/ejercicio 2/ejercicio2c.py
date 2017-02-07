#MARTHA ELENA NIEVES MORA
#LABORATORIO 3B
#EJERCICIO 2c



import matplotlib.pyplot as plt
import numpy as np
import math

x=np.linspace(0,2*math.pi,90)

y=np.sin(3*x)*np.cos(2*x)
z=1/2*np.cos(x)+5/2*np.cos(5*x)
plt.plot(x,y, linewidth=4, color='b', label='f(x)=np.sin(3*x)*np.cos(2*x)')
plt.plot(x,z, linewidth=6, color='r', label='g(x)=1/2*np.cos(x)+5/2*np.cos(5*x)')
plt.legend()
plt.title('ejercicio 2.c')
plt.xlabel('tiempo')
plt.ylabel('cm')
plt.grid(True)
plt.show()
