print("ingresa tu peso en Kg")
peso=input()
print("ingresa tu estatura en m")
altura=input()
result=peso/altura**2
print("IMC:",result)
if result>=0 and result <=15:
	print("desnutricion:",result)
elif result>=16 and result <=19:
	print("bajo peso:",result)
elif result>=20 and result <=23:
	print("normal:",result)
elif result>=24 and result <=28:
	print("Obesidad tipo 1:",result)
elif result>=29 and result <=36:
	print("Obesidad tipo 2:",result)
elif result>=40:
	print("Obesidad morbida")