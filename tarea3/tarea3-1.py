#martha elena nieves mora
#laboratorio 1 tarea 3
#29112016
import matplotlib.pyplot as m
import math
x=input("latitud")
x2=input("longitud")
y=input("latitud")
y2=input("longitud")
j=x,y
k=x2,y2

def distancia(j,k):
    x,y=j
    x=x*math.pi/180
    y=y*math.pi/180
    x2,y2=k
    x2=x2*math.pi/180
    y2=y2*math.pi/180
    d=637.01*math.acos(math.sin(x)*math.sin(x2)+math.cos(x2)*math.cos(x)*math.cos(y-y2))
    return d
print "la distancia en km es;", distancia(j,k)
