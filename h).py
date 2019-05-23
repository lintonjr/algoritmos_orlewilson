apostador1 = float(input('Valor do apostador 1: '))
apostador2 = float(input('Valor do apostador 2: '))
apostador3 = float(input('Valor do apostador 3: '))
valorPremio = float(input('Insira o valor do Premio: '))

prop_a1 = apostador1 / (apostador1 + apostador2 + apostador3)
prop_a2 = apostador2 / (apostador1 + apostador2 + apostador3)
prop_a3 = apostador3 / (apostador1 + apostador2 + apostador3)

premio1 = valorPremio * prop_a1
premio2 = valorPremio * prop_a2
premio3 = valorPremio * prop_a3

print('O Apostador 1 ganhou: ' + str(premio1) + ', o Apostador 2 ganhou: ' + str(premio2) + ' e o Apostador 3 ganhou: ' + str(premio3))
