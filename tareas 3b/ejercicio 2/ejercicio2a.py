#MARTHA ELENA NIEVES MORA
#LABORATORIO 3B
#EJERCICIO 2a

import matplotlib.pyplot as plt
import numpy as np
import math



x=np.linspace(0,4*math.pi,100)

y=np.cos(2*x)+np.sin(3*x)
z=-2*np.sin(2*x)+3*np.cos(3*x)
plt.plot(x,y, linewidth=4, color='b', label='f(x)=np.cos(2*x)+np.sin(3*x)')
plt.plot(x,z, linewidth=6, color='r', label='g(x)=2*np.sin(2*x)+3*np.cos(3*x)')
plt.legend()
plt.title('ejercicio 2.a')
plt.xlabel('tiempo')
plt.ylabel('cm')
plt.grid(True)
plt.show()
