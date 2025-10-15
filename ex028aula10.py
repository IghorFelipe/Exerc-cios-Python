#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
#tentar descobrir qual foi o número escolhido pelo computador

import random
random = random.randint(0, 5)
nu = (int(input('Digite o número que eu pensei: ')))
if nu == random:
    print('VENCEU!')
else:
    print('PERDEU!')
