# 1. Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números
# maiores que 0.

#decidi implementar interação com usuário para adicionar uma camada de complexidade a mais


from time import sleep
count = 0
num  = int(input('Digite um número acima de 0 e te mostrarei os 5 primeiros múltiplos de 3 desse número: '))

while num  <= 0:
    print('Por favor,digite somente número acima de 0.')
    num = int(input('digite novamente: '))
    if num > 0 :   
        print('prosseguindo...') 
        sleep(2)
        break

while count <5:
    if num % 3 == 0:
        print(f'O número {num} é múltiplo de 3.')
        count += 1
    sleep(1)
    num+=1
    
# 2. Faça um programa que utilize o comando while para mostrar na tela uma contagem regressiva, iniciando
# em 10 e terminando em 0. Mostre também uma mensagem “FIM!” após a contagem.

from time import sleep
num = 11
while num < 12:
    num-=1
    if num == 0:
        break
    sleep(1)
    print(num)
print('FIM')

# 3. Faça um programa que declare um inteiro, inicialize-o com 0, incremente-o de 1000 em 1000, imprimindo
# seu valor na tela, até que seu valor seja 100000 (cem mil).


#feito utilizando while com interação com usuário
count = 0
num  = int(input('Digite um número inteiro: '))
if num < 0:
    while num <0:
        num = int(input('Digite SOMENTE um número INTEIRO: '))
        if num > 0:
            break
while num >0:
    count += 1000
    print(count)
    if count == 100000:
        break


#feito utilizando for sem interação com usuário

for i in range(0,100001,1000):
    print(i)
