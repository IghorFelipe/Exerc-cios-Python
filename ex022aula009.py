#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O NOME COM TODAS AS LETRAS MAIÚSCULAS
#O NOME COM TODAS AS MINÚSCULAS
#QUANTAS LETRAS AO TODO
#QUANTAS LETRAS TEM O PRIMEIRO NOME

nome = (input('Escreva seu nome: ').strip())
print(nome.upper())
print(nome.lower())
print(len(nome))
partes = nome.split()
nome1 = partes[0]
print(len(nome1))
sem = nome.replace(' ', '')
print(len(sem))

#teve bastante ajuda do chat GPT

''' Solução do curso em vídeo '''

'''nome = str(input('Digite seu nome completo: '));strip()
   print('Analisando seu nome...')
   print('Seu nome em maiúsculas é {}'.format(nome.upper()))
   print('Seu nome em minúsculas é {}'.format(nome.lower()))
   print('Seu nome tem ao todo {} letras'. format(len(nome) - nome.count(' ')))
   #print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))'''