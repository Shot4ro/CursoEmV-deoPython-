nome = str(input('Digite seu nome: ')).upper().strip()
print('No seu nome aparece a letra "A": {}'.format(nome.count('A')))
print('A primira letra A apareceu na posição {}'.format(nome.find('A')+1))
print('A Ultima letra "A" apareceu: {}'.format(nome.rfind('A')+1))
