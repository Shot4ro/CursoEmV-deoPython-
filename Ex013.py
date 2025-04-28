salário = float(input('Qual valor do salário de seu funcionario? R$'))
aumento = salário + (salário *15 / 100)
print('O salário de seu funcionario que antes era de R${:.2f} Agora com o aumento de 15% e de: R${:.2f}'.format(salário,aumento))

