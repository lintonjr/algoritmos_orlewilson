alfabeto = ('abcdefghijklmnopqrstuvxywz')
for vogal in 'aeiou':
    print(vogal, end=' ')
print('\n')

pessoas = [['Ana', 52], ['Carlos', 60], ['João', 40],
           ['Maria', 72], ['Letícia', 85], ['Raimundo', 90], ['Andreia', 55],
           ['Mara', 40], ['Joana', 61], ['Heitor', 95]]
n = 0
while n < 10:
    print(pessoas[n][1])
    n += 1

meses = ('Não é um mês', 'Janeiro', 'Fevereiro', 'Março',
         'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
         'Outubro', 'Novembro', 'Dezembro')

while True:
    num = int(input('Digite um número entre 1 e 12: '))
    if 1 <= num <= 12:
        break
    print('Tente Novamente. \n', end='')
print(f"Você digitou o número {meses[num]}")
