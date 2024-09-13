# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/iflista6.c



id = int(input("QUAL NUMERO DA IDENTIFICAÇÃO DO ALUNO:"))
tam = 3
soma=0
notas = []
conceito = ''

for i in range(tam):
    nota = float(input(f"QUAL A {i+1} NOTA:"))
    soma+=nota
    notas.append(nota)

media = (soma)/tam

if media >= 90:
    conceito = 'A'
else:
    if media >=75:
        conceito = 'B'
    else:
        if media >=60:
            conceito = 'C'
        else:
            if media>=40:
                conceito = 'D'
            else:
                conceito = 'E'

if conceito in 'ABC':
    print(f"APROVADO conceito:%c \n COM O ID: {id}\n COM A MEDIA: {media}\n",)
    print("COM AS NOTAS: ", end='')
    for i in range(len(notas)):
        print(f" {notas[i]} ", end='')
else:
    print(f"REPROVADO \n COM O ID: {id}\n COM A MEDIA: {media}")
    print(" COM AS NOTAS: ", end='')
    for i in range(len(notas)):
        print(f" {notas[i]} ", end='')
    
