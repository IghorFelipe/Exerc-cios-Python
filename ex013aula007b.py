#Faça um programa onde ele ira calcular o preço de um produto com 10% de desconto, caso comprado a vista
# e 5% de aumento comprado a prazo.

produto = float(input('Digite o preço do pruduto R$'))
avista = produto - (10 / 100 * produto)
aprazo = produto + (5 / 100 * produto)

print('O preço do produto é {}, com o pagamento a vista irá ficar {}. já a prazo ira ficar {}'.format(produto, avista, aprazo))