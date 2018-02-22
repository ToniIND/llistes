#Coding: UTF8

limit=input("Indicam el numero de paraules que tindra la llista: ")

while limit<=0:

    limit=input("Ha de ser major a 0: ")

llista=[]

for i in range (1,limit+1):

    paraula=raw_input("Digam el valor "+str(i)+":")

    llista += [paraula]

print llista

eliminar=raw_input("Quants valors vols eliminar?: ")

for i in range (1,elminar):
	rem=raw_input("Indica el valor a eliminar "+str(i)+":")

llista2=[]

for i in llista:

	if i!=eliminar:
		llista2.append(i)

print llista

print llista2

