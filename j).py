comprimento = float(input('Insira o valor do comprimento: '))
largura = float(input('Insira o valor do largura: '))
altura = float(input('Insira o valor do altura: '))

volume = round(comprimento * altura * largura, 2)
print('O volume é: ' + str(volume))