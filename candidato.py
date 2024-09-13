
	
presidente = []
governador = []


for i in range(15):
    presidente.append(0)
    if i<12:
        governador.append(0)

inicio = input("\nDigite S para votar, ou N para sair.")

while inicio != 'N' and inicio != 'n':
    if inicio == 'S' or inicio == 's':
        
        voto = int(input("\nInforme seu voto para a presidência: "))

        while True:
            match voto:
                case 0:
                    presidente[0] = presidente[0] + 1
                    print("\nVocê votou branco.")
                    break
                case 1:
                    presidente[1] = presidente[1] + 1
                    print("\nVocê votou em Alvaro Dias (Podemos).")
                    break
                case 2:
                    presidente[2] = presidente[2] + 1
                    print("\nVocê votou em Cabo Daciolo (Patriota).")
                    break
                case 3:
                    presidente[3] = presidente[3] + 1
                    print("\nVocê votou em Ciro Gomes (PDT).")
                    break
                case 4:
                    presidente[4] = presidente[4] + 1
                    print("\nVocê votou em Eymael (DC).")
                    break
                case 5:
                    presidente[5] = presidente[5] + 1
                    print("\nVocê votou Fernando Haddad (PT).")
                    break
                case 6:
                    presidente[6] = presidente[6] + 1
                    print("\nVocê votou em Geraldo Alckmin (PSDB).")
                    break
                case 7:
                    presidente[7] = presidente[7] + 1
                    print("\nVocê votou em Guilherme Boulos (PSOL).")
                    break
                case 8:
                    presidente[8] = presidente[8] + 1
                    print("\nVocê votou em Henrique Meirelles (MDB).")
                    break
                case 9:
                    presidente[9] = presidente[9] + 1
                    print("\nVocê votou em Jair Bolsonaro (PSL).")
                    break
                case 10:
                    presidente[10] = presidente[10] + 1
                    print("\nVocê votou em João Amoedo (Novo).")
                    break
                case 11:
                    presidente[11] = presidente[11] + 1
                    print("\nVocê votou em João Vicente Goulart (PPL).")
                    break
                case 12:
                    presidente[12] = presidente[12] + 1
                    print("\nVocê votou em Marina Silva (REDE).")
                    break
                case 13:
                    presidente[13] = presidente[13] + 1
                    print("\nVocê votou em Vera Lúcia (PSTU).")
                    break
                case 14:
                    presidente[14] = presidente[14] + 1
                    print("\nVocê votou nulo.")
                    break
                case _:
                    print("\nNúmero invalido.")
                

        voto = int(input("\nInforme seu voto para governador(a): "))
            
        while True:
            match (voto):
                case 0:
                    governador[0] = governador[0] + 1
                    print("\nVocê votou branco.")
                    break
                case 1:
                    governador[1] = governador[1] + 1
                    print("\nVocê votou em Cida Borghetti (Progressista).")
                    break
                case 2:
                    governador[2] = governador[2] + 1
                    print("\nVocê votou em Doutor Rosinha (PT).")
                    break
                case 3:
                    governador[3] = governador[3] + 1
                    print("\nVocê votou em Geonísio Marinho (PRTB).")
                    break
                case 4:
                    governador[4] = governador[4] + 1
                    print("\nVocê votou em João Arruda (MDB).")
                    break
                case 5:
                    governador[5] = governador[5] + 1
                    print("\nVocê votou Jorge Bernardi (REDE).")
                    break 
                case 6:
                    governador[6] = governador[6] + 1
                    print("\nVocê votou em Ogier Buchi (PSL).")
                    break
                case 7:
                    governador[7] = governador[7] + 1
                    print("\nVocê votou em Priscila Ebara (PCO).")
                    break
                case 8:
                    governador[8] = governador[8] + 1
                    print("\nVocê votou em Professor Ivan Bernardo (PSTU).")
                    break
                case 9:
                    governador[9] = governador[9] + 1
                    print("\nVocê votou em Professor Piva (PSOL).")
                    break
                case 10:
                    governador[10] = governador[10] + 1
                    print("\nVocê votou em Ratinho Junior (PSD).")
                    break
                case 11:
                    governador[11] = governador[11] + 1
                    print("\nVocê votou nulo.")
                    break
                case _:
                    print("\nNúmero invalido.")
                    

        inicio = input("\nDigite 'S' para votar ou 'N' para sair e exibir os resultados.")

    else:
        inicio = input("\nDigite 'S' para votar ou 'N' para sair e exibir os resultados.")



print("\n\nContagem de votos para a presidência:")
print("\n     - Alvaro Dias (Podemos): ", presidente[1])
print("\n     - Cabo Daciolo (Patriota): ", presidente[2])
print("\n     - Ciro Gomes (PDT): ", presidente[3])
print("\n     - Eymael(DC): ", presidente[4])
print("\n     - Fernando Haddad (PT): ", presidente[5])
print("\n     - Geraldo Alckmin (PSDB): ", presidente[6])
print("\n     - Guilherme Boulos (PSOL): ", presidente[7])
print("\n     - Henrique Meirelles (MDB): ", presidente[8])
print("\n     - Jair Bolsonaro (PSL): ", presidente[9])
print("\n     - João Amoêdo (Novo): ", presidente[10])
print("\n     - João Vicente Goulart (PPL): ", presidente[11])
print("\n     - Marina Silva (Rede): ", presidente[12])
print("\n     - Vera Lúcia (PSTU): ", presidente[13])
print("\n")
print("\n     - Votos Brancos: ", presidente[0])
print("\n     - Votos Nulos: ", presidente[14])

max = 0
empate = 0
cont=0

while cont<15:         
    if presidente[cont] > presidente[max]:
        max = cont
    
    else:
        if presidente[cont] == presidente[max]:
            empate = cont
    cont+=1

    
if max > empate:
    match (max):
        case 1:
            print("\n\nO próximo presidente da república será Alvaro Dias (Podemos), com  votos.", presidente[1])
            
        case 2:
            print("\n\nO próximo presidente da república será Cabo Daciolo (Patriota), com  votos.", presidente[2])
            
        case 3:
            print("\n\nO próximo presidente da república será Ciro Gomes (PDT), com  votos.", presidente[3])
            
        case 4:
            print("\n\nO próximo presidente da república será Eymael (DC), com  votos.", presidente[4])
            
        case 5:
            print("\n\nVocê votou Fernando Haddad (PT), com  votos.", presidente[5])
            
        case 6:
            print("\n\nO próximo presidente da república será Geraldo Alckmin (PSDB), com  votos.", presidente[6])
            
        case 7:
            print("\n\nO próximo presidente da república será Guilherme Boulos (PSOL), com  votos.", presidente[7])
            
        case 8:
            print("\n\nO próximo presidente da república será Henrique Meirelles (MDB), com  votos.", presidente[8])
            
        case 9:
            print("\n\nO próximo presidente da república será Jair Bolsonaro (PSL), com  votos.", presidente[9])
            
        case 10:
            print("\n\nO próximo presidente da república será João Amoedo (Novo), com  votos.", presidente[10])
            
        case 11:
            print("\n\nO próximo presidente da república será João Vicente Goulart (PPL), com  votos.", presidente[11])
            
        case 12:
            print("\n\nA próxima presidenta da república será Marina Silva (REDE), com  votos.", presidente[12])
            
        case 13:
            print("\n\nA próxima presidenta da república será Vera Lúcia (PSTU), com  votos.", presidente[13])
            
else:
    if (max == empate):
        print("Empate! precisamos de um segundo turno")