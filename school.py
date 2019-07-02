"""
NOMBRE:Fernando Hernandez Vazquez
ID:1719210003
DATE:02/07/2019
GROUP:TIC22
DESCRIPTION:Clases
"""
class School:
    def __init__(self,name,teacher_name,id):
        self.name=name
        self.id=id
        self.teacher_name=teacher_name
hidalgo=School("Colegio")
print(hidalgo.name)
fer=School("Fer","Hernandez")
print(hidalgo.teacher_name)
