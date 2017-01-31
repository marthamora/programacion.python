
def leer(archivo):
    m=open(archivo, "r")
    prog=m.readline()
    N=input("Ingrese el numero de lineas que quiere leer ")
    while N<0:
        print"No existen lineas negativas"
        N=input("error ingrese otro valor ")
    n=range(0,N)
    for i in n:
        print ""
        print prog
        prog=m.readline()

funcion=raw_input('Ingrese texto ')
archivo=funcion+".txt"
leer(archivo)
