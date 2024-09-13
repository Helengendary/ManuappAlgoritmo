
valor = 1
soma = 0

tam = 4

mat1 = [0] * tam
for i in range(len(mat1)):
    mat1[i] = [0] * tam

for i in range(tam):
    for j in range(tam):
        mat1[i][j] = valor
        valor = valor * 2

        soma = soma + mat1[i][j]


for i in range(tam):
    for j in range(tam):
        print(f"| {mat1[i][j]} |", end='')
    print("\n")


print(f"A soma da matriz = {soma}\n\n")
