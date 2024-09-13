# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C_v2/blob/master/trabalhostructIPTU.c

class imovel_dados:
    def __init__(self, numcad, valorIPTU, mesesatrasado, valorMulta) :
        self.numcad = numcad
        self.valorIPTU = valorIPTU
        self.mesesatrasado = mesesatrasado
        self.valorMulta = valorMulta
        
    def __repr__(self):
     return str(self.__dict__)


listaimoveis = []

cont = 0
calculos = 0

quantidade = int(input('Quantos imóveis deseja cadastrar: '))
print()

for i in range(quantidade):
        
    print('------------------------------------------------------------------------------')   
    print(f'IMÓVEL {i+1}')     
    cadastro = int(input(f"\nINFOME O NUMERO DE CADASTRO({cont+1}º imovel):\n"))

    iptu = float(input("\nINFOME O VALOR DO IPTU:\n"))

    meseAtraso = int(input("\nINFOME QUANTOS MESES ATRASADO:\n"))
    
    multis = 50.00 * meseAtraso
    
    calculos+=1
    
    listaimoveis.append(imovel_dados(cadastro, iptu, meseAtraso, multis))

for i in range(len(listaimoveis)):
    dicionario = listaimoveis[i]
    print()
    print()
    print(f"IMÓVEL {i+1}")
    print(f"CADASTRO: {dicionario.numcad}\nVALOR IPTU: {dicionario.valorIPTU}\nMESES EM ATRASO: {dicionario.mesesatrasado}\nMULTA: {dicionario.valorMulta}\n\n")


print(f"Numero de imoveis calculados: {calculos} imovéis.\n")
