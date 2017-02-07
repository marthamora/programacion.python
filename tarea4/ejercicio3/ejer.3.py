#Nieves Mora Martha Elena

print "Numeraremos las lineas de su archivo"
n=raw_input("Nombre del archivo de entrada (con extension)")
m=raw_input("Nombre de su archivo de salida (con extension)")

def numerar(n,m):
    v=open(n,"r")
    lineas=[]
    lineas=v.readlines()
    nvo=open(m,"w+")
    for i in range(1,len(lineas)):
        nvo.write(str(i)+")"+lineas[i])
    print "El archivo esta listo en el direcotrio"

numerar(n,m)
v.close()
nvo.close()



