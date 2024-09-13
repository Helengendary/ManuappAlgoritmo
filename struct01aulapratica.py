# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C_v2/blob/master/struct01aulapratica.c

class ficha_aluno:
    def __init__(self, codigo, nome, telefone, mail) :
        self.codigo = codigo
        self.nome = nome
        self.telefone = telefone
        self.mail = mail
        
    def __repr__(self):
     return str(self.__dict__)


codigo = int(input("\nInforme o codigo:"))

nome = input("\nInforme o nome:")

telefone = int(input("\nInforme o telefone:"))

email = input("\nInforme o Mail:")

aluno = ficha_aluno(codigo, nome, telefone, email)

print("\n****************************************************")
print("****************************************************")
print("****************************************************\n")

print(f"{aluno.codigo}")
print(f"{aluno.nome}")
print(f"{aluno.telefone}")
print(f"{aluno.mail}")
	