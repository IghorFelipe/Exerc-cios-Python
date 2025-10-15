#Crie um programa que leia o nome de uma pessoa e diga se ela tem "silva"  no nome

'''nome = str(input('Digite seu nome: ')).strip()
print('Seu nome tem silva? {}'.format(nome[0:].upper() == 'Silva'))'''

nome = str(input('Digite seu nome: '))
print('Seu nome tem silva? {}'.format('SILVA' in nome.upper()))

