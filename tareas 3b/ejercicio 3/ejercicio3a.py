#MARTHA ELENA NIEVES MORA
#LABORATORIO 3B
#EJERCICIO 3a



import matplotlib.pyplot as plt
import numpy as np
import math

x=np.linspace(0,2*math.pi,99)

y=np.cos(x)**3
z=np.sin(x)**3
plt.plot(x,y, linewidth=4, color='b', label='f(x)=np.cos(x)**3')
plt.plot(x,z, linewidth=6, color='r', label='g(x)=np.sin(x)**3')
plt.legend()
plt.title('ejercicio 3.a')
plt.xlabel('tiempo')
plt.ylabel('cm')
plt.grid(True)
plt.show()
