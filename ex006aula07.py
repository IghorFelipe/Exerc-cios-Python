#Crie um algoritmo que leia um número e mostre o seu dobro
#triplo e raiz quadrada

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
raiz = n ** (1/2)
print('Dobro: {}\n Triplo: {}\n Raiz Quadrada: {:.2f}\n'.format(d, t, raiz))