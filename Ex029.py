velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 60:
    multa = (velocidade-60) * 8
    print('Multado!! Você excedeu o Limite da via que é 60km/h')
    print('Sua multa transito e de R$ {:.2f}'.format(multa))
else: #não e preciso Usar o Else somente para colocar essa menagem NESSE CASO!!!!
    print('Sua velocidade esta dentro do limite!')
print('Tenha um bom dia! Dirija com cuidado')
