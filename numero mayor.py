"""
NOMBRE:Fernando Hernandez Vazquez
ID:1719210003
DATE:11/06/2019
GROUP:TIC22
DESCRIPTION:imprime el numero mayor. Version 2
"""
process=1
while process==1:
	print ("ingresa un numero")
	n1=input()
	print ("ingresa un numero")
	n2=input()
	print ("ingresa un numero")
	n3=input()
	if n1>n2 and n1>n3:
		print ("el numero mayor es:"+str(n1))
	elif n2>n1 and n2>n3:
     		print ("el numero mayor es:"+str(n2))
	elif n3>n1 and n3>n2:
		print ("el numero mayor es:"+str(n3))
	else:
		print ("you need another process?")
	print ("you need another process?")
	process=input()