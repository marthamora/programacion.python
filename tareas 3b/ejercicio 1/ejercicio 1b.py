#MARTHA ELENA NIEVES MORA

#LABORATORIO 3B

#EJERCICIO 1b



import matplotlib.pyplot as plt

import numpy as np



x=np.linspace(-1,5,80)

y=5-2*x**2-8*x-11

plt.plot(x,y, linewidth=5, color='r')

plt.legend()

plt.title('ejercicio 1b')

plt.xlabel('tiempo')

plt.ylabel('cm')

plt.grid(True)

plt.show()
