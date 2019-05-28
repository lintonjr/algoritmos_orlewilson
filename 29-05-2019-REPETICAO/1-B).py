def ehBissexto(ano):
    return ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0


for anoInformado in range(2004, 2098):
    resultado = ehBissexto(anoInformado)
    if resultado:
        print(f"Ano {anoInformado} é bissexto")
