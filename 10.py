# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/10.c


class competidor:
    def __init__(self, codigo, age, height, weight) :
        self.codigo = codigo
        self.age = age
        self.height = height
        self.weight = weight
        
    def __repr__(self):
     return str(self.__dict__)


codigo = int(input("\nInforme o codigo:"))

age = int(input("\nInforme a idade:"))

altura = float(input("\nInforme a altura:"))

peso = float(input("\nInforme o peso:"))

comp = competidor(codigo, age, altura, peso)

print("\n****************************************************")
print("****************************************************")
print("****************************************************\n")

print(f"O competidor {comp.codigo} , tem {comp.age} anos, pesa {comp.weight} Kg e tem {comp.height} de altura. \n")
