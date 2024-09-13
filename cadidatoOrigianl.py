# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/candidato.c

pres = 0
gov = 0

print("_______________________________________________")
print("__________________ELEIÇÕES_____________________")
print("_______________________________________________\n")


while True:
    pres = int(input("INSIRA O NÚMERO DO SEU CANDIDATO A PRESIDÊNCIA:"))
    print("_______________________________________________\n")
    
    match(pres):
        case 19:
            print("Alvari Dias(Podemos):19 ")
            break
        
        case 51:
            print("Cabo Daciolo(Patriota):51 ")
            break
        
        case 12:
            print("Ciro Gomes(PDT):12 ")
            break
        
        case 27:
            print("Eymael(CD):27 ")
            break
        
        case 13:
            print("Fernando Haddad(deuPTnobrasil):13 ")
            break
        
        case 45:
            print("Geraldo tavivo?(PSDB):45 ")
            break
        
        case 50:
            print("Guilherme Anarquia(Psol):50 ")
            break
        
        case 15:
            print("Henrique Meirelles(MDB):15 ")
            break
        
        case 17:
            print("Jair quefasebrasil(PSL):17 ")
            break
        
        case 30:
            print("João Amo�do(Novo):30 ")
            break
        
        case 54:
            print("João Vicente Goulart(PPL):54 ")
            break
        
        case 18:
            print("Marina Silva(Rede):18 ")
            break
        
        case 16:
            print("Vera Lúcia(PSTU):16 \n")	
            break

        case _:
            print("_____________Candidato Inválido________________ \n")	


print("_______________________________________________\n\n")

while True:
    gov = int(input("INSIRA O NúMERO DO SEU CANDIDATO A GOVERNADOR:"))
    print("_______________________________________________\n\n")
    match(gov):
        case 11:
            print("Cida Borghetti (Progressista) - 11 \n")
            break
        
        case 13:
            print("Doutor Rosinha (PT) - 13  \n")
            break
        
        case 28:
            print("Geon�sio Marinho (PRTB) - 28 \n")
            break
        
        case 15:
            print("Jo�o Arruda (MDB) - 15 \n")
            break
        
        case 18:
            print("Jorge Bernardi (Rede) - 18 \n")
            break
        
        case 17:
            print("Ogier Buchi (PSL) - 17 \n")
            break
        
        case 29:
            print("Priscila Ebara (PCO) - 29 \n")
            break
        
        case 16:
            print("Professor Ivan Bernardo (PSTU) - 16  \n")
            break
        
        case 50:
            print("Professor Piva (PSOL) - 50 \n")
            break
        
        case 55:
            print("Ratinho Junior (PSD) - 55 \n")
            break

        case _:
            print("_____________Candidato Inválido________________ \n")	