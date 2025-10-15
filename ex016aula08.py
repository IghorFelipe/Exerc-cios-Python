#crie um programa que eia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

import math
valor = float(input('Digite um valor: '))
print('O valor digitado foi {:.3f}, e sua porção inteira é {}'.format(valor, math.trunc(valor)))

