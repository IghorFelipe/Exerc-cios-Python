#faça um progama que leia o nome completo de uma pessoa, mostrando em seguina o primeiro e o último
#nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()
dividido =  nome.split()
print('Seu nome primeiro nome é {}'.format(dividido[0]))
print('Seu último nome é {}'.format(dividido[-1]))
