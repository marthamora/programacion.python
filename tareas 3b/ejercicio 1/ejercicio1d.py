#MARTHA ELENA NIEVES MORA
#LABORATORIO 3B
#EJERCICIO 1d



import matplotlib.pyplot as plt
import numpy as np
import math

x=np.linspace(0,24,100)
y=x*math.e**(-1*x)
plt.plot(x,y, linewidth=5, color='r')
plt.legend()
plt.title('ejercicio 1d')
plt.xlabel('tiempo')
plt.ylabel('cm')
plt.grid(True)
plt.show()
