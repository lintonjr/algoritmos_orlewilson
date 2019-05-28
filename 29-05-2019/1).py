# Matéria: Algoritmos
# Professor: Orlewilson
# Alunos: Linton Junior 182120246, Caio Cezar, Paulo Ricardo

n = int(input("Digite um número"))

if n <= 0:
    print("fim")
else:
    c1 = 1
    S = 0
    c2 = 1
    P = 0
    if c2 <= c1:
        R = c1 % c2
        if R == 0:
            P = P + 1
        else:
            c2 = c2 + 1
    elif P <= 2:
        S = S + c1
    else:
        c1 = c1 + 1
        if c1 > n:
            print("Fim")
        else:
            c2 = 1
            P = 0
