def binary(n1):
    i = 1
    lista = []
    while i <= 8:
        n2 = (n1 % 2)
        lista.append(n2)
        n1 = n1 // 2
        i += 1
    print(lista[::-1])


binary("Banana")
