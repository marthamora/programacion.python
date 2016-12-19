#MARTHA ELENA NIEVES MORA
#LABORATORIO 3B
#EJERCICIO 3c



import matplotlib.pyplot as plt
import numpy as np
import math

x=np.linspace(0,2*math.pi,99)

y=np.sin(3*x)
z=np.sin(4*x)
plt.plot(x,y, linewidth=4, color='b', label='f(x)=np.sin(3*x)')
plt.plot(x,z, linewidth=6, color='r', label='g(x)=np.sin(4*x)')
plt.legend()
plt.title('ejercicio 3.c')
plt.xlabel('tiempo')
plt.ylabel('cm')
plt.grid(True)
plt.show()
