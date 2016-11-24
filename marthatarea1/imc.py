
#Martha elena nieves Mora
#24112016
#laboratorio1
print "ingresa tu peso"
p=float(raw_input())
print "ingresa tu altura"
a=float(raw_input())

def imc(peso,altura):
    return peso/altura*altura
def clasificacion(imc):
    if imc<16.0:
        print "delgades severa",clasificacion
    elif imc in range(16.0,16.99):
    print "delgadez moderada",clasificacion
    elif imc in range(17.o,18.49):
    print "delgadez leve"clasificacion
    elif imc in range(18.5,24.99):
        print "normal",clasificacion
    elif imc<=25:
        print "sobrepeso",clasificacion
    elif imc<=30:
        print "obesidad",clasificacion
    elif imc<=40
        print "obesidad morbida",clasificacion
print clasificacion

    
