"""
NOMBRE:Fernando Hernandez Vazquez
ID:1719210003
DATE:11/06/2019
GROUP:TIC22
DESCRIPTION:Metodos
"""
#Caso1
def add(number1,number2):
	result=number1+number2
	return result
n1=5
n2=6
r=add(n1,n2)
print("Add",r)

#Caso2
def add(number1,number2):
	result=number1+number2
	print("ADD",result)
n1=5
n2=6
r=add(n1,n2)
print("Add",r)
print("Add",add(n1,n2))
add(n1,n2)