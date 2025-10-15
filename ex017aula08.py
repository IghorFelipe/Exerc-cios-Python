#Faça um progama que leia o comprimento do cateto  oposto e do cateto adjacente de um triângulo retângulo,
#calcule e mostre o comprimento da hipotenusa.

from math import hypot
cateto1 = float(input('Qual o comprimento do cateto oposto? '))
cateto2 = float(input('Qual o comprimento do cateto adjacente? '))
hipot = hypot(cateto1, cateto2)
print('O comprimento da hipotenusa é {:.2f}'.format(hipot))

#matematicamente

'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('O valor da hipotenusa é {:.2f}'.format(hi))'''