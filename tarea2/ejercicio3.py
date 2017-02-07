#martha elena Nieves Mora
#laboratorio2


import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

def obtener_triangulo(P):
    m = P * 0.5
    n = P * 0.5 + np.array([0.5, 0])
    k = P * 0.5 + np.array([0.25, np.sqrt(3)/4])
    return np.array([m,n,k])

triangle = np.array([[0, 0],
              [1, 0],
              [0.5, np.sqrt(3)/2]])

etapa = 5
for e in range(etapa):
    triangle = get_triangle(triangle)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111, aspect='equal')
for t in triangle.reshape(3**etapa,3,2):
    ax1.add_patch(mpatches.Polygon(t, fc="y"))

plt.show()





