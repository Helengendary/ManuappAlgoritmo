# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/whilepratica06.c

idade = 0
conttotal = 0
contIA = 0
contIB = 0
contJA = 0
contJB = 0
contADUL = 0

idade = int(input("Qual a idade do nadador? \n"))

while idade > 0:
    if idade >=18:
        contADUL+=1
        conttotal+=1
        print("ADULTO")
  
    else:
        if idade >=5 and idade<=7:
            contIA+=1
            conttotal+=1
            print("infantil A")
      
        else:
            if idade>=8 and idade<=10:
                contIB+=1
                conttotal+=1
                print("infantil B")
            
            else:
                if idade>=11 and idade<=13:
                    contJA+=1
                    conttotal+=1
                    print("Juvenil A")
                    
                else:
                    if(idade>=14 and idade<=17):
                        contJB+=1
                        conttotal+=1
                        print("Juvenil B")
                        
    idade = int(input("Qual a idade do nadador?"))
    
print(f" Categoria infantil A sao: {contIA}")
print(f" Categoria infantil B sao: {contIB}")
print(f" Categoria juvenil A sao: {contJA}")
print(f" Categoria juvenil B sao: {contJB}")
print(f" Categoria Adultos sao: {contADUL}")

print(f"total: {conttotal}")