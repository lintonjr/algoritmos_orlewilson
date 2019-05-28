# Matéria: Algoritmos
# Professor: Orlewilson
# Alunos: Linton Junior 182120246, Caio Cezar, Paulo Ricardo

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
idade = float(input("Digite sua idade: "))

if altura >= 1.70 and altura <= 1.85 and peso >= 48 and peso <= 60 and idade >= 15 and idade <= 20:
    print("Cadidato Aprovado")
else:
    print("Candidato Reprovado")
