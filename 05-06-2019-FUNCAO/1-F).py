def soma_elementos(lista, n):
    l = lista
    n = n
    if len(l) < n:
        return print("Valor inválido")
    soma = 0
    for i in range(n):
        soma += l[i]

    return print(soma)


lista = []

while True:
    lista.append(int(input("Digite um valor para compor o conjunto: ")))
    resp = str(input("Inserir mais? [S/N] "))
    if resp in 'Nn':
        break
n = int(input("Digite o número de valores a somar: "))

soma_elementos(lista, n)
