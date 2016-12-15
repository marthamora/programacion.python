#MARTHA ELENA NIEVES MORA
#LABORATORIO 3B
#EJERCICIO 7a



import matplotlib.pyplot as plt
import numpy as np
import math

x=np.linspace(0,4*math.pi,0.04)
r=150+100*np.sin(4.5*x)
t=x-(np.cos(10*x))/(10)
y=320+r*np.cos(t)
z=-240-r*np.sin(t)
plt.plot(y,z, linewidth=4, color='b', label='grafica')
plt.legend()
plt.title('ejercicio 7a')
plt.xlabel('tiempo')
plt.ylabel('cm')
plt.fill_between(y,z,color='r')
plt.axis('equal')
plt.axis('off')
plt.grid(True)
plt.show()
