#Faça um alfgoritmo que leia o preço de um produto e mostre
#seu novo preço, com 5% de desconto.

p = float(input('Qual o preço do produto: '))
d = (5 / 100) * p
print('O novo valor do produto com desconto é: {:.2f}'.format(p - d))