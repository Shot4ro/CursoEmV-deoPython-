from random import randint #Consegue escolher numeros e outras coisas "randomicas"
from time import sleep #Esse comando faz com que consigha colocar delay nas mensagens
computador = randint(0, 5) #Comando de escolha aleatoria
print('=='*20)
print('Vou escolher um numero entre 0 e 5')
print('=='*20)
player = int(input('Qual numero eu pensei? '))
print('PROCESSANDO...')
sleep(3) #Ele vai congelar por 3 segundos e soltar o resultado
if player == computador: # O (  ==  ) significa player pensou = computador
    print('PARABENS! Você acertou!')
else:
    print('Você errou, tente de novo!O numero escolhido foi {}'.format(computador))