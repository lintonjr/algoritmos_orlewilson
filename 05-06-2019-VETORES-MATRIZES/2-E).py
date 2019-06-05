artigo = [['Bolsa', 100, 10], ['Calçado', 150, 15],
          ['Roupa', 300, 5], ['Acessórios', 120, 8]]

n = 0
while n < 4:
    nome = artigo[n][0]
    valor = artigo[n][1]
    desconto = artigo[n][2]
    valorDesc = artigo[n][1] - (artigo[n][1]*artigo[n][2]/100)
    print(f"{nome} com {desconto}%, de R${valor} para R${valorDesc}")
    n += 1
