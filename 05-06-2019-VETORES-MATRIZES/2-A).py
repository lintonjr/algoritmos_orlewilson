A = []
B = []

while True:
    A.append(int(input("Digite um valor para compor o conjunto A: ")))
    resp = str(input("Inserir mais? [S/N] "))
    if resp in 'Nn':
        break
while True:
    B.append(int(input("Digite um valor para compor o conjunto B: ")))
    resp = str(input("Inserir mais? [S/N] "))
    if resp in 'Nn':
        break

aux = B
B = A
A = aux

print(f"O valor trocado de A com B: A =  {A}, B = {B}")
