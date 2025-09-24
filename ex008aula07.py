#Escreva um programa que leia um valor em metros e o
#exiba convertido em centímetros e milímetros

vm = float(input('Digite o valor da metragem: '))
cm = vm * 100
mm = vm * 1000
km = vm / 1000
hm = vm / 100
dam = vm / 10
print('Este valor equivale a {:.0f}cm\n {:.0f}mm\n {}km\n {}hm\n {}dam'.format(cm, mm, km, km, dam))