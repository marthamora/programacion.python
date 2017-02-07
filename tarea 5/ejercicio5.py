#Nieves Mora Martha Elena

import csv
tp=open('Tablaperiodica.csv')
lns=csv.reader(tp,delimiter=';')
for line in lns:
    no_atom=line[0]
print no_atom