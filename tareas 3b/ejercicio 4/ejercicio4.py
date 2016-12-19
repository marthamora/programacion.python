#MARTHA ELENA NIEVES MORA
#LABORATORIO 3B
#EJERCICIO 4



import matplotlib.pyplot as plt
import numpy as np


x=np.arange(0.0,2,0.01)

y=np.sin(2*np.pi*x)
z=1.2*np.cos(4*np.pi*x)

plt.subplot(3,1,1)
plt.fill_between(x,0,y)
plt.ylabel('between y and 0')

plt.subplot(3,1,2)
plt.fill_between(x,y,1)
plt.ylabel('between y and z')

plt.subplot(3,1,3)
plt.fill_between(x,y,z)
plt.ylabel('between y and z')
plt.xlabel('x')

plt.show()

