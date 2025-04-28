dias = int(input('Quantos dias voce ficou com o carro alugado: '))
km = float(input('Quantos Km voce andou com o carro? '))
total = (dias*60)+(km*0.15)
print('O total a pagar pela locação e de R${:.2f}'.format(total))


