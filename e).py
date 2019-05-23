f = int(input('Insira uma temperatura em Fahrenheit: '))
C = (f - 32) * (5/9)
C = round(C, 3)
print('A temperatura em Celsius é: ' + str(C))