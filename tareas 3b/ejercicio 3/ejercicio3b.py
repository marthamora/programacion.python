#MARTHA ELENA NIEVES MORA
#LABORATORIO 3B
#EJERCICIO 3b



import matplotlib.pyplot as plt
import numpy as np
import math

x=np.linspace(-2*math.pi,2*math.pi,120)

y=x+2*np.sin(2*x)
z=x+2*np.cos(5*x)
plt.plot(x,y, linewidth=4, color='b', label='x+2*np.sin(2*x)')
plt.plot(x,z, linewidth=6, color='r', label='g(x)=x+2*np.cos(5*x)')
plt.legend()
plt.title('ejercicio 3.b')
plt.xlabel('tiempo')
plt.ylabel('cm')
plt.grid(True)
plt.show()
