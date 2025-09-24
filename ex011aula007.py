#Faça um programa que laia a largura e a altura de uma
#parede em metros, calcude a sua área e a quantidade de tinta
#necessária para pintá-la, sabendo que cada livro de tinta,
#pinta uma área de 2m2.

l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
area = l * a
qt = area / 2
print('A sua parede tem a dimensão de {}x{} e sua área é de {}m².\n'
      'Para pintar essa parede, você precisará de {:.1f}l'.format(l, a, area, qt))