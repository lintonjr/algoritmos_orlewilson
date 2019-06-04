from random import randint
result = []
while len(result) != 6:
    r = randint(0, 50)
    if r not in result:
        result.append(r)
print(result)
