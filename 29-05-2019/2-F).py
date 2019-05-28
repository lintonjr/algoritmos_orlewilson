
a = int(input("Insira valor de A: "))
b = int(input("Insira valor de B: "))
c = int(input("Insira valor de C: "))

if a < (b + c) and b < (a + c) and c < (a + b):
    print(f'Os valores {a} e {b} e {c} podem ser os lados de um triângulo')
else:
    print(f'Os valores {a} e {b} e {c} não podem ser os lados de um triângulo')
