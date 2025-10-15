#um professor quer sortear um dos seus quatro aluno para apagar o quadro
#faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

'''import random
nome1 = str(input('Primeiro Aluno: '))
nome2 = str(input('Segundo Aluno: '))
nome3 = str(input('Terceiro Aluno: '))
nome4 = str(input('Quarto Aluno: '))
escolhido = random.choices(nome1, nome2, nome3, nome4)'''

#correção
import random
nome1 = str(input('Primeiro Aluno: '))
nome2 = str(input('Segundo Aluno: '))
nome3 = str(input('Terceiro Aluno: '))
nome4 = str(input('Quarto Aluno: '))
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))