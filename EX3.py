

class estagiarios:
    def __init__(self, codigo, nome, ano, sal, sal_anual) :
        self.codigo = codigo
        self.nome = nome
        self.ano = ano
        self.sal = sal
        self.sal_anual = sal_anual
        
    def __repr__(self):
     return str(self.__dict__)
	
listaEstagiarios = []
cont = 0
qtos = 0
anual = 0
i = 0
listasal = []

quanti = int(input('Quantos estagiarios deseja inseriri: '))

for i in range(quanti):
    
    cod = int(input("QUAL O CODIGO DO ESTAGIARIO: "))

    name = input("QUAL O NOME DO ESTAGIARIO: ")
    
    ano = int(input("QUAL O ANO DE NASCIMENTO DO ESTAGIARIO: "))
    
    for i in range(12):
            salario = float(input(f"QUAL O {i+1}º SALARIO DO ESTAGIARIO:\n")) 
            anual += salario
            listasal.append(salario)
            
    listaEstagiarios.append(estagiarios(cod, name, ano, salario, anual)) 
    qtos+=1

print(f"{qtos}º estagiario\n")
        

for i in range(quanti):
    print("____________________________________________________")
    print("Codigo: ", listaEstagiarios[i].codigo)
    print("Nome: ", listaEstagiarios[i].nome)
    print("Ano: ", listaEstagiarios[i].ano)
    print("Salario Anual: ", listaEstagiarios[i].sal_anual)
    print("____________________________________________________")