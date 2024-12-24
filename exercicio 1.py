# 1. Faça um programa que leia um número inteiro e imprima-o.

num = int(input('digite um número inteiro: '))
print(num)

# -----------------------------------------------------------------------------------

# 2. Faça um programa que peça para o usuário digitar três valores inteiro e imprima a soma deles.
total = 0
for  i in range(0,3):
    num = int(input('digite um número:  '))
    if num >= 0:
        total += num

print(total)

# -------------------------------------------------------------------------------------

# 3. Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos.
total = 0
for i in range(0,3):
    num = int(input('digite um valor:'))
    quadrado = num ** 2
    total += quadrado  
print(total)
