#Martha Elena Nieves Mora

def concatenar(n,m):
    nvo=open(m,"a")
    for i in n:
        c=open(i,"r")
        for linea in c:
            nvo.write(linea+"\n")