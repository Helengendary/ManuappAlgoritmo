# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C_v2/blob/master/EX1.c

hora = 10.00
horaextra = 15.00

horas_normais = 0
horas_extras = 0
horasnorm_resul = 0
horasext_resul = 0
resul = 0
poup = 0

horas_normais = float(input("Informe o numero de horas normais trabalhadas no ano:\n"))

horas_extras = float(input("Informe o numero de horas extras trabalhadas no ano:\n"))

horasnorm_resul = horas_normais * hora
horasext_resul = horas_extras * horaextra
resul = horasnorm_resul + horasext_resul

poup = resul * 0.08

print("______________________________________________________")
print(f"Valor de horas normais: {horasnorm_resul} reais\n")
print(f"Valor de horas extras: {horasext_resul} reais\n")
print(f"Total de ganho no ano = {resul} reais\n")
print(f"Valor a guardar na poupança = {poup} reais\n")
print("______________________________________________________")