#faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
#cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
angulo = float(input('Qual o angulo? '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tan = tan(radians(angulo))
print('O seno de {} é {:.2f},o cosseno é {:.2f}, e a tangente é {:.2f}'.format(angulo, seno, cosseno, tan))

#sem importar as biliotecas especificas

'''import math
angulo = float(input('DIgite o valor do angulo: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O valor do seno do angulo {} é {:.2f}, do cosseno é {:.2f}. e da tangente é {:.2f}'.format(angulo, sen, cos, tan))'''
