'''
O código abaixo, verifica se um 
ano é bissexto
'''

ano = int(input("informe o ano: "))

if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
    print("Ano é bissexto")
else:
    print("Ano não é bissexto")
