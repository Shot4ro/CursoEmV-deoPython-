produto = float(input('Qual o valor do produto? R$'))
desconto = produto - (produto*5/100)
print('O prodruto que custava R${:.2f}, agora com o desconto de 5% esta saindo por R${:.2f}'.format(produto,desconto))
