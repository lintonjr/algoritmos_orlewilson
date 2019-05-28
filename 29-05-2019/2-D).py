# Matéria: Algoritmos
# Professor: Orlewilson
# Alunos: Linton Junior 182120246, Caio Cezar, Paulo Ricardo

numero = int(input('Digite um inteiro: '))
if not (numero % 3):
    print(f"O número {numero} é múltiplo de 3")
elif not (numero % 7):
    print(f"O número {numero} é múltiplo de 7")
else:
    print(f"O número {numero} não é múltiplo de 3 e nem de 7")
