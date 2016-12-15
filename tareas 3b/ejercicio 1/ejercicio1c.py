#MARTHA ELENA NIEVES MORA
#LABORATORIO 3B
#EJERCICIO 1c


import matplotlib.pyplot as plt
import numpy as np
import math

x=np.linspace(-1,5,120)
y=x*math.e**(-2*x)
plt.plot(x,y, linewidth=5, color='r')
plt.legend()
plt.title('ejercicio 1c')
plt.xlabel('tiempo')
plt.ylabel('cm')
plt.grid(True)
plt.show()
