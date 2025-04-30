print('++'*20)
print('Analisador de Triângulos')
print('++'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1:
    print('Os segmentos a cima PODEM formar triângulo')
else:
    print('Os seguimentos a cima NÃO podem formar triângulo')