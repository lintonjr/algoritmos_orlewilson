# Matéria: Algoritmos
# Professor: Orlewilson
# Alunos: Linton Junior 182120246, Caio Cezar, Paulo Ricardo

num = int(input('Digite um número: '))

if int(num) == 0:
    print("O número é 0")
elif int(num) % 2 == 0:
    print(f"O numero {num} e par")
else:
    print(f"O numero {num} e impar")
