valor = int(input('Digite o valor da conta: R$'))
total = valor

if total >= 50:
    notas50 = int(total/50)
    total -= notas50 * 50
if total >= 10:
    notas10 = int(total/10)
    total -= notas10 * 10
if total >= 1:
    notas1 = int(total/1)
    total -= notas1 * 1
print(f'Para pagar o valor de {valor} é necessário {notas50} de R$50, {notas10} de R$10 e {notas1} de R$1')
