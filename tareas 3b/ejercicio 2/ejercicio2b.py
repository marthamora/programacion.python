#MARTHA ELENA NIEVES MORA
#LABORATORIO 3B
#EJERCICIO 2b


import matplotlib.pyplot as plt
import numpy as np
import math



x=np.linspace(0,2,120)

y=x*math.e**(-3*x)
z=math.e*(-3*x)
plt.plot(x,y, linewidth=4, color='b', label='f(x)=x*math.e**(-3*x)')
plt.plot(x,z, linewidth=6, color='r', label='g(x)=math.e*(-3*x)')
plt.legend()
plt.title('ejercicio 2.b')
plt.xlabel('tiempo')
plt.ylabel('cm')
plt.grid(True)
plt.show()
