# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/trabalho_i.c

i = 0
a = 0
b = 0
c = 0

a = int(input(f"INFORME O VALOR DE a :"))	

b = int(input(f"INFORME O VALOR DE b :"))	

c = int(input(f"INFORME O VALOR DE c :"))

i = int(input(f"DIGITE O VALOR DE i :"))

print(f"__________________________________\n\n")	

while i > 0:
    if i == 1:
            if a < b and a < c and b < c:
                print(f"a = {a}")
                print(f"b = {b}")
                print(f"c = {c}\n")
            
            else :
                if a < b and a < c and c < b:
                    print(f"a = {a}")
                    print(f"c = {c}")
                    print(f"d = {b}\n")	
                
                else:
                    if b < a and b < c and a < c:
                        print(f"b = {b}")
                        print(f"a = {a}")
                        print(f"c = {c}\n")
        
                    else: 
                        if b < a and b < c and c < a:
                            print(f"b = {b}")
                            print(f"c ={c}")
                            print(f"a = {a}\n")
                        
                        else :
                            if c < a and c < b and a < b:
                                print(f"c = {c}")
                                print(f"a = {a}")
                                print(f"b = {b}\n")
                            
                            else:
                                if c < a and c < b and b < a:
                                    print(f"c = {c}")
                                    print(f"b = {b}")
                                    print(f"a = {a}\n")	
    else: 
            if i == 2: 
                if a > b and a > c and b > c:
                    print(f"a = {a}")
                    print(f"b = {b}")
                    print(f"c = {c}\n")
                
                else :
                    if a > b and a > c and c > b:
                        print(f"a = {a}")
                        print(f"c = {c}")
                        print(f"d = {b}\n")	
                    
                
                    else :
                        if b > a and b > c and a >c:
                            print(f"b = {b}")
                            print(f"a = {a}")
                            print(f"c = {c}\n")
                        
                        else : 
                            if b > a and b > c and c > a:
                                print(f"b = {b}")
                                print(f"c = {c}")
                                print(f"a = {a}\n")
                            
                        
                    
                            else :
                                if c > a and c > b and a > b:
                                    print(f"c = {c}")
                                    print(f"a = {a}")
                                    print(f"b = {b}\n")
                                
                                else :
                                    if c > a and c > b and b > a:
                                        print(f"c = {c}")
                                        print(f"b = {b}")
                                        print(f"a = {a}\n")	

            
            else:
                if a > b and a > c and b > c:
                    print(f"b = {b}")
                    print(f"a = {a}")
                    print(f"c = {c}\n")
                
                else :
                    if a > b and a > c and c > b:
                        print(f"c = {c}")
                        print(f"a = {a}")
                        print(f"d = {b}\n")	
                    
                    else :
                        if b > a and b > c and a >c:
                            print(f"a = {a}")
                            print(f"b = {b}")
                            print(f"c = {c}\n")
                        
                        else : 
                            if b > a and b > c and c > a:
                                print(f"c = {c}")
                                print(f"b = {b}")	
                                print(f"a = {a}\n")
                            
                            else :
                                if c > a and c > b and a > b:
                                    print(f"a = {a}")
                                    print(f"c = {c}")								
                                    print(f"b = {b}\n")
                                
                                else :
                                    if c > a and c > b and b > a:
                                        print(f"b = {b}")
                                        print(f"c = {c}")
                                        print(f"a = {a}\n")	

    print("__________________________________\n\n")
    print("digite 1 ou 2 ou 3 para i, ou 0 para sair.\n\n")
    i = int(input("DIGITE O VALOR DE i :\n"))	
    print("\n")	