#Martha elena nieves Mora
#24112016
#laboratorio1


num=int(input("ingrese los segundos\n"))
dia=(int(num/86400.0))
hor=int((num-(dia*86400))/3600.0)
minu=int((num-((hor*3600.0)+(dia*86400)))/60)
seg=num-((dia*86400)+(hor*3600)+(minu*60))
print(str(dia)+"d "+str(hor)+"h "+str(minu)+"m "+str(seg)+"s")
