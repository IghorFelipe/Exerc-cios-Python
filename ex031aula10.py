#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para de viagens de ate 200km e R$ 0,45 para viagens mais longas.

d = float(input('Digite a distância da viagem: '))
if d<=200:
    print('O valor a ser pago é R${:.2f}'.format(d * 0.50))
else:
    print('O valor a ser pago é R${:.2f}'.format(d * 0.45))