n1 = int(input("Digite o número inicial: "))
n2 = int(input("Digite o número final: "))
x = 0
notas = 0
soma = 0
par = impar = div3 = div7 = 0
while n1 <= n2:
    notas = n1
    soma += notas
    x += 1

    if n1 % 2 == 0:
        par += 1
    else:
        impar += 1
    if not n1 % 3:
        div3 += 1
    elif not n1 % 7:
        div7 += 1

    ip = soma / x
    n1 += 1
x = 0
print(
    f"Você digitou {par} pares, {impar} ímpares, {div3} numeros com possibilidade de dividir por 3, {div7} com possibilidade de dividir por 7 e a média é {ip}")
