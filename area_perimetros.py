"""
NOMBRE:Fernando Hernandez Vazquez
ID:1719210003
DATE:11/06/2019
GROUP:TIC22
DESCRIPTION:perimetros y areas
"""
try:
	#Area circulo
	print("Area circulo")
	def acirculo(radio):
		pi=3.1416
		area=pi*(radio**2)
		print ("acirculo",area)
	radio=int(input("radio"))
	acirculo(radio)
	
	#Area Cuadrado
	print("Area cuadrado")
	def acuadrado(lado):
		area=lado*lado
		print ("acuadrado",area)
	lado=int(input("lado"))
	acuadrado(lado)

	#Area Triangulo
	print("Area Triangulo")
	def atriangulo(base,altura):
		area=base*altura/2
		print ("atriangulo",area)
	base=int(input("base"))
	altura=int(input("altura"))
	atriangulo(base,altura)

	#Area Trapecio
	print("Area Trapecio")
	def atrapecio(base_mayor,base_menor,altura):
		area=(base_mayor+base_menor)*altura/2
		print ("atrapecio",area)
	base_mayor=int(input("base_mayor"))
	base_menor=int(input("base_menor"))
	altura=int(input("altura"))
	atrapecio(base_mayor,base_menor,altura)

	#PERIMETROS

	#Perimetro Circulo
	print("Perimetro circulo")
	def pcirculo(radio):
		pi=3.1416
		perimetro=2*(pi*radio)
		print ("pcirculo",perimetro)
	radio=int(input("radio"))
	pcirculo(radio)

	#Perimetro Cuadrado
	print("Perimetro cuadrado")
	def pcuadrado(lado):
		area=lado*4
		print ("pcuadrado",area)
	lado=int(input("lado"))
	pcuadrado(lado)

	#Perimetro Triangulo Isoceles
	print("Perimetro Triangulo Isoceles")
	def ptriangulo(lado):
		area=lado*3
		print ("ptriangulo",area)
	lado=int(input("lado"))
	ptriangulo(lado)

	#Perimetro Trapecio Trapecio
	print("Perimetro Trapecio")
	def ptrapecio(base_mayor,base_menor,lado):
		perimetro=base_mayor+base_menor+2*(lado)
		print ("ptrapecio",perimetro)
	base_mayor=int(input("base_mayor"))
	base_menor=int(input("base_menor"))
	lado=int(input("lado"))
	ptrapecio(base_mayor,base_menor,lado)

except exception as e:
		print("error:"+str(e))
