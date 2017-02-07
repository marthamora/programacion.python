#MARTHA ELENA NIEVES MORA

#LABORATORIO 3B

#EJERCICIO 1a



import matplotlib.pyplot as plt

import numpy as np



x=np.linspace(-6,2,100)

y=5-4*x-x**2

plt.plot(x,y, linewidth=3, color='r')

plt.legend()
plt.title('ejercicio 1a')

plt.xlabel('tiempo')

plt.ylabel('cm')

plt.grid(True)

plt.show()



