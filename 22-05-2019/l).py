num = int(input('Numero '))
p = int(num/100)
s = int(num % 100)
result = int((p+s)*(p+s))
if result == num:
    print(f'O número {num} tem a mesma propriedade de 3025')
else:
    print(f'O número {num} não tem a mesma propriedade que 3025')
