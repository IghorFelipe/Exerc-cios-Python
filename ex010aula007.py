#Crie um programa que leia quanto dinheiro a pessoa tem na carteira
#e mostre quantos Dólares ela pode comprar

dc = float(input('Quanto você tem na carteira? '))
c = dc / 3.27
print('Você pode comprar: {:.3f}'.format(c))