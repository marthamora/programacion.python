#Martha Elena Nieves Mora
#25112016
#laboratorio 1, tarea 2

x=input("valor cateto opuesto")
y=input("cateto adyacente")
import math
def hip(x,y):
    i=math.sqrt(x*x+y*y)
    return i
print "la hip es:", hip(x,y)
