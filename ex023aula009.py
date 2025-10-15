#FAÇA UM PROGARMA QUE LEIA UM NÚMERO DE 0 A 9999 e mostre na tela cada um dos dígitos separados.

n = (input('Digite um número: '))
print('A unidade é: {}\n A centena é: {}\n A dezena é: {}\n e a Milha é: {}'.format(n[3], n[2], n[1], n[0]))

#resolução

'''num = int(input('Informe um númer: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milha: {}'.format(num))'''
