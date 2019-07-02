"""
NOMBRE:Fernando Hernandez Vazquez
ID:1719210003
DATE:02/07/2019
GROUP:TIC22
DESCRIPTION:Clases
"""

class Person:
	name=""
	first_name=""
	email=""
	def __init__(self):
		pass
	def login(self):
		print("login")
	def dance(self):
		print("Dance")
jhon= Person()
jhon.name="jhon"
jhon.first_name="Carter"
jhon.email="jhon@earth"
jhon.login()
print(jhon.name)
dejah=Person()
dejah.name="Dejah"
print (dejah.name)
fer=Person()
fer.name="Fer"
print (fer.name)
#forma 2 de crear una clase
class Person2:
    def __init__(self,name,first_name):
        self.name=name
        self.first_name=first_name
dejha= Person2("Dejha","Toris")
print(dejha.name)
fer= Person2("Fer","Hernandez")
print(fer.name)
#ejercicio 3
class Singer:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def dance(self):
		print("Dance")
	def sing(self):
		print("Sing")
marc_anthony=Singer ("Marc Anthony","52") 
print ("Name",marc_anthony.name)
marc_anthony.sing()


