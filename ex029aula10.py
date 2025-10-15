#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar 7 reais por cada km acima do limite.

v = float(input('Digite a velocidade do carro: '))
if v>80:
    m = (v - 80)*7
    print('Voce foi multado, e o valor da multa é R${}'.format(m))
else:
    print('--FIM--')