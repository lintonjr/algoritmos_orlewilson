<a href="https://github.com/lintonjr/algoritmos_orlewilson">
    <img src="https://d3pwz8qrais8b7.cloudfront.net/portal-wyden/public/custom-uploads/wyden-footer.png" alt="Aimeos logo" title="Trabalho de Algoritmos" align="right" height="60" />
</a>

# Trabalho de Algoritmos - Prof. Orlewilson

Trabalho de [Algoritmos](https://github.com/lintonjr/algoritmos_orlewilson) da disciplina lecionada pelo Professor Orlewilson na FMF.

[![Algoritmos Demo](http://oi66.tinypic.com/10da1lg.jpg)](http://oi66.tinypic.com/10da1lg.jpg)

## Conteúdo

- [22/05/2019](#Parte-1)
  - [Questão 1](#Questão-1)
  - [Questão 2](#Questão-2)
  - [Questão 3](#Questão-3)
- [29/05/2019](#Parte-2)
  - [Parte 2 Questão 1](#Parte-2-Questão-1)
  - [Parte 2 Questão 2](#Parte-2-Questão-2)
  - [Parte 2 Questão 3](#Parte-2-Questão-3)
- [License](#license)
- [Links](#links) -->

## Parte 1

Questões a serem entregues e defendidas **Data: 22/05/2019 - Adiada**.

### Questão 1

- Elabore um fluxograma e desenvolva em linguagem C ou Python em cada item a seguir: (Questões de A à L)

**a)** Ler quatro notas, calcular a média aritmética e imprimir o resultado.

**b)** Ler um número inteiro e imprimir seu sucessor e seu antecessor.

**c)** Ler dois valores para as variáveis A e B, efetuar a troca dos valores de forma que a
variável A passe a ter o valor da variável B e que a variável B passe a ter o valor da
variável A. Imprimir os valores trocados.

**d)** Ler um número entre 0 e 60 e mostrar o seu sucessor, sabendo que o sucessor de 60
é 0.

**e)** Ler uma temperatura em Fahrenheit e a apresente convertida em graus Celsius. A
fórmula de conversão é C = (F – 32) \* (5/9), na qual F é a temperatura em Fahrenheit
e C é a temperatura em Celsius.

**f)** Ler um número do tipo real e imprimir o resultado do quadrado desse número.

**g)** Ler um número do tipo real e imprimir a quinta parte deste número.

**h)** Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido
proporcionalmente ao valor que cada deu para a realização da aposta. Faça um
programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima
quanto cada um ganharia do prêmio com base no valor investido.

**i)** As lojas de um shopping center estão concedendo 10% de desconto no preço de
qualquer produto. A partir do valor fornecido, calcule e exiba o preço atual e o preço
com o desconto.

**j)** Ler os valores de COMPRIMENTO, LARGURA e ALTURA e apresentar o valor do volume
de uma caixa retangular. Utilize para o cálculo a fórmula VOLUME = COMPRIMENTO \*
LARGURA \* ALTURA.

**k)** Calcule quantas notas de 50, 10 e 1 são necessárias para pagar uma conta cujo valor é
fornecido pelo usuário.

**l)** O número 3025 possui uma característica interessante, sendo a seguinte: 30 + 25 = 55
e 552 = 3025. Elabore um algoritmo que verifique se um número inteiro de quatro
algarismos (digitado) tem essa propriedade ou não.

### Questão 2

- Sabendo que `A=5, B=4 e C=3 e D=6`, informe se as expressões abaixo são verdadeiras ou
  falsas.

  ```
  I. (A > C) e (C <= D).

  II. (A+B) > 10 ou (A+B) = (C+D).

  III. (A>=C) e (D >= C).

  (A) F, F e F.

  (B) V, F e V.

  (C) V, V e V.

  (D) F, F e V.

  (E) V, V e F.
  ```

### Questão 3

- Considere as seguintes atribuições: `R = 2, S = 5, T = -1, X = 3, Y = 1 e Z = 0`. Resolva as
  expressões abaixo:

  ```
  • A <- (Z >= 5) or (T > Z) and (X – Y + R > 3 * Z)

  • B <- (T + 3 >= 4) and not (3 * R/2 < S * 3)

  • C <- (X == 2) or (Y == 1) AND ((Z == 0) OR (R > 3)) AND (S < 10)

  • D <- (R <> S) OR NOT (R < X) AND (4327 * X * S * Z == 0)
  ```

## Parte 2

**SE-ENTÃO**

### Parte 2 Questão 1

Considere o fluxograma a seguir:
[![Questão 1 - Parte 2](http://oi63.tinypic.com/2e6a3xk.jpg)](http://oi63.tinypic.com/2e6a3xk.jpg)
**(A)** Identifique as estruturas de programação nela contidas.

**(B)** Para que serve esse fluxograma? Simule-o para os seguintes valores de N: 1, 2, 3 e 7.

**(C)** Elabore o algoritmo correspondente em pseudocódigo, linguagem C e linguagem
Python.

### Parte 2 Questão 2

Elabore um fluxograma e desenvolva em linguagem C ou Python em cada item a seguir: (Itens de A a I)

a) Exibir o triângulo de Pascal, conforme indicado a seguir:

```
1

1 1

1 2 1

1 3 3 1

1 4 6 4 1

...
```

b) Verificar se um número fornecido pelo usuário é par ou ímpar. Para isso, apresente
uma mensagem mostrando o número digital e o resultado do teste.

c) Melhorar o algoritmo do item anterior verificando se o número inserido pelo usuário
é zero, par ou ímpar.

d) De acordo com um valor fornecido pelo usuário, verifique se ele é múltiplo de 3, ou
múltiplo de 7. Apresente uma mensagem mostrando o número e o resultado do teste.

e) Uma loja de departamentos está oferecendo diferentes formas de pagamento,
conforme as opções listadas a seguir. Leia o valor total de uma compra e calcule o valor
do pagamento final de acordo com a opção escolhida. Se a escolha for pagamento
parcelado, calcule também o valor da parcela. Ao fim, apresente o valor total e o valor
das parcelas.

```
• Pagamento à visa – conceder desconto de 5%;

• Pagamento em 3 parcelas – o valor não sofre alteração;

• Pagamento em 5 parcelas – acréscimo de 2%;

• Pagamento em 10 parcelas – acréscimo de 8%
```

f) Receber três valores digitados A, B e C e informe se estes podem ser os lados de um
triângulo. O ABC é triângulo `se A < B + C e B < A + C e C < A + B`.

g) Permitir a entrada de uma cadeia de caracteres S, e então escreva as possíveis
rotações à esquerda dessa cadeia. Por exemplo, se for digitada a cadeia `“Banana”`,
deverá ser exibida a sequência de palavras, nesta ordem: `“Banana”`, `“ananaB”`,
`“nanaBa”`, `“anaBan”`, `“aBanan”`, `“Banana”`.

h) Calcular e mostrar a tabuada de um número informado pelo usuário.

i) Ler a idade de um nadador e mostrar sua categoria, usando as regras a seguir:
| **Categoria** | **Idade** |
| ------------- | ------------- |
| Infantil | 5 a 7 |
| Juvenil | 8 a 10 |
| Adolescente | 11 a 15 |
| Adolescente | 11 a 15 |
| Adulto | 16 a 30 |
| Sênior | Acima de 30 |

### Parte 2 Questão 3

[FCC – 2012 – TST – Técnico Judiciário] Fornecidos os dados das candidatas ao time de
basquete: altura, peso e idade e as restrições abaixo:

**Altura:** de 1.70 a 1.85 m

**Peso:** de 48 a 60 kg

**Idade:** de 15 a 20 anos

**O trecho de algoritmo, em pseudocódigo, que verifica corretamente se os dados se enquadram nas restrições fornecidas é:**
**(A)** `se (1.70 < altura < 1.85) e (48kg < peso< 60kg) e (15 anos < idade < 20 anos) então imprima(“Candidato aprovado”) senão imprima (“Candidato reprovado”)`

**(B)** `se ((altura>=1.70 ou altura <= 185) e (peso >=48 ou peso <= 60) e idade (idade >=15 ou idade <=20)) então imprima (“Candidato aprovado”) senão imprima (“Candidato reprovado”)`
**(C)** `se ((altura >=1.70 e altura <= 1.85) e (peso >= 48 e peso <= 60) e (idade >=15 e idade <=20)) então imprima(“Candidata aprovada”) senão imprima(“Candidata reprovada”)`
**(D)** `se ( 170 ≤ altura ≤ 1.85 ) e (48 ≤ peso ≤ 60) e (15 ≤ idade ≤ 20) então imprima (“ Candidata aprovada”) senão imprima (“Candidata reprovada”)`
**(E)** `se ((altura >= 1.70 e altura <= 1.85) ou (peso>=48 e peso <=60) ou (idade >= 15 e idade <=20)) então imprima (“Candidata aprovada”) senão imprima (“Candidata reprovada”)`

<!-- ## Page setup

The page setup for an Aimeos web shop is easy if you import the [standard page tree for TYPO3 8.7/9.5](https://aimeos.org/docs/TYPO3/Install_Aimeos/Setup_pages#Download) into your TYPO3 installation.

### Go to the import view

- In Web::Page, root page (the one with the globe)
- Right click on the globe
- Move the cursor to "Branch actions"
- In the sub-menu, click on "Import from .t3d"

![Go to the import view](https://aimeos.org/docs/images/Aimeos-typo3-pages-menu.png)

### Upload the page tree file

- In the page import dialog
- Select the "Upload" tab (2nd one)
- Click on the "Select" dialog
- Choose the file you've downloaded
- Press the "Upload files" button

![Upload the page tree file](https://aimeos.org/docs/images/Aimeos-typo3-pages-upload.png)

### Import the uploaded page tree file

- In Import / Export view
- Select the uploaded file from the drop-down menu
- Click on the "Preview" button
- The pages that will be imported are shown below
- Click on the "Import" button that has appeared
- Confirm to import the pages

![Import the uploaded page tree file](https://aimeos.org/docs/images/Aimeos-typo3-pages-import.png)

Now you have a new page "Shop" in your page tree including all required sub-pages.

## License

The Aimeos TYPO3 extension is licensed under the terms of the GPL Open Source
license and is available for free.

## Links

- [Web site](https://aimeos.org/integrations/typo3-shop-extension/)
- [Documentation](https://aimeos.org/docs/TYPO3)
- [Forum](https://aimeos.org/help/typo3-extension-f16/)
- [Issue tracker](https://github.com/aimeos/aimeos-typo3/issues)
- [Source code](https://github.com/aimeos/aimeos-typo3) -->
