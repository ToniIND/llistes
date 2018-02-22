#Coding: UTF8

limit=input("Indicam el numero de paraules que tindra la llista: ")

while limit<0:

    limit=("Ha de ser major a 0: ")

llista=[]

for i in range (1,limit+1):

    paraula=raw_input("Digam el valor "+str(i)+":")

    llista += [paraula]

print llista

buscar=raw_input("Indica el nom que vols buscar: ")
substituir=raw_input("Indica la paraula que vols canviar: ")

for i in range (len(llista)):

    if llista[i]==buscar:

        llista[i]=substituir

print llista
