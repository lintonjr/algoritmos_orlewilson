def Divisible(nC, nD):
    nO = nC
    if nC <= 0 or nD <= 0:
        return print(f"O número {nO} não é divisível por {nD}")
    while nC > 0:
        nC -= nD
        if nC == 0:
            return print(f"O número {nO} é divisível por {nD}")
    return print(f"O número {nO} não é divisível por {nD}")


num = int(input("Digite o número a ser divido: "))
div = int(input("Digite o divisor: "))
Divisible(num, div)
