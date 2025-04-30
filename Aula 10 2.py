#nome = str(input('Qual e seu nome? '))
#if nome == 'Celso':
    #print('Que nome lindo você tem!')
#else:
    #print('Seu nome e Normal')
#print('tenha um bom dia {}'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua media foi ruim! Estude mais!')
