#Faça um algoritmo que laia o salário de um funcionário
#e mostre seu novo salário, com 15% de aumento.

sal = float(input('Qual seu salário? '))
aumento = (15 / 100) * sal
print('Seu novo salário é: {}'.format(aumento + sal))