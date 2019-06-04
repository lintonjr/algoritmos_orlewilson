def InverteCadeia(text):
    stringSemEspacos = text.replace(' ', '')
    stringTodaMinuscula = stringSemEspacos.lower()
    stringInvertida = stringTodaMinuscula[::-1]
    if stringInvertida == stringTodaMinuscula:
        print("SIM")
    else:
        print("NAO")


InverteCadeia(input('Digite um texto '))
