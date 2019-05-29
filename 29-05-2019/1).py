# Matéria: Algoritmos
# Professor: Orlewilson
# Alunos: Linton Junior 182120246, Caio Cezar, Paulo Ricardo

N = int(input("Insira um número: "))
if N <= 0:
    print(f"Fim do programa!")
else:
    C1 = 1
    S = 0
    C2 = 1
    P = 0
    if C2 <= C1:
        R = C1 % C2
        if R == 0:
            P = P+1
            C2 = C2+1
        else:
            C2 = C2+1
    else:
        if P <= 2:
            S = S+1
            C1 = C1+1
        else:
            C1 = C1+1
        if C1 > N:
            print(f"O valor de S é: {S}")
        else:
            C2 = 1
            P = 0
