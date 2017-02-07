#MARTHA ELENA NIEVES MORA
#LABORATORIO 3B
#EJERCICIO 6



import matplotlib.pyplot as plt
import numpy as np
import math

x=np.linspace(0,2*math.pi,150)
r=-250*np.sin(5*x)*np.cos(4*x)
t=x+np.sin(r/100)
y=320+r*np.cos(t)
z=-240-r*np.sin(t)
plt.plot(y,z, linewidth=4, color='b', label='grafica')
plt.legend()
plt.title('ejercicio 6')
plt.xlabel('tiempo')
plt.ylabel('cm')
plt.fill_between(y,z,color='r')
plt.axis('equal')
plt.axis('off')
plt.grid(True)
plt.show()
