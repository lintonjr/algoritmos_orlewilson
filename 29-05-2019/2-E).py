preco = float(input("Digite o valor da compra: "))
ctrl = int(input("""[1] Pagamento à visa – conceder desconto de 5%;
[2] Pagamento em 3 parcelas – o valor não sofre alteração;
[3] Pagamento em 5 parcelas – acréscimo de 2%;
[4] Pagamento em 10 parcelas – acréscimo de 8% """))

if ctrl == 1:
    novo = preco - (preco * 5 / 100)
    parcelas = 0
    print(f"\nO valor final ficará R${novo} à vista")
elif ctrl == 2:
    parcelas = 3
    novo = round(preco / parcelas, 2)
    print(
        f"\nO valor final ficará R${preco} em {parcelas} parcelas de R${novo}")
elif ctrl == 3:
    novo = preco + (preco * 2/100)
    parcelas = 5
    novoP = round(novo / parcelas, 2)
    print(
        f"\nO valor final ficará R${novo} em {parcelas} parcelas de R${novoP}")
elif ctrl == 4:
    novo = preco + (preco * 8/100)
    parcelas = 10
    novoP = round(novo / parcelas, 2)
    print(
        f"\nO valor final ficará R${novo} em {parcelas} parcelas de R${novoP}")
