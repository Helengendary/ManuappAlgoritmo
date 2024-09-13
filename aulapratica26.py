# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/aulapratica26.c

soma = 0
tam = 5
for i in range(tam):
    horas = float(input(f"Informe as horas trabalhadas no dia: {i+1}:"))
    soma += horas
resp = (soma)/tam
print(f"\nA média de horas trabalhadas é de: {resp} horas por dia .\n")