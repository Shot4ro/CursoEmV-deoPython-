import math
n = int(input('Me diga um numero: '))
resultado = n % 2
if resultado == 0:
    print('O numero que voce escolheu e {} par'.format(n))
else:
    print('O numero que voce escolheu e {} impar'.format(n))
