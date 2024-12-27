# 1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior.
maior = None
num1 = float(input('digite o primeiro número: '))
num2 = float(input('digite o segundo número: '))

if num1 > num2:
    maior = num1
    print(f'o maior número é {maior}. ')

elif num2 > num1:
    maior= num2
    print(f'o maior número é {maior}. ')


# 2. Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule
# a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o
# número é inválido.

from math import sqrt
num = int(input('digite um número: '))

if num >0:
    print(sqrt(num ))
elif num <0:
    print('número inválido.')

# 3. Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar.

num  = int(input('digite um número inteiro: '))
if num % 2 == 0:
    print(f'o número {num} é par.')
else:
    print(f'o número {num} é inpar')
