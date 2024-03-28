'''from operator import itemgetter

dic = {
    "cliente1":{
        "nome":"Ana",
        "sobrenome":"Ferreira",
        "altura": 1.78
    },
    "cliente3":{
        "nome":"Pedro",
        "sobrenome":"Pedreira",
        "altura": 1.67,
    },
    "cliente2":{
        "nome":"Beatriz",
        "sobrenome":"Madureira",
        "altura": 1.50
    },
}

dic.update({"cliente3":{"nome": "Juca","sobrenome":"Bala"}})
print(dic)

for valor, altura in sorted(dic.items(), key=itemgetter(0)):
    print(valor, altura)

for chave in dic.keys():
    print("")
    print(chave)
    for c1,valor in dic[chave].items():

        print(c1,valor)'''

filmes = {
    "nome": "Star Wars",
    "ano": 1977,
    "diretor": "Geoge Lucas"
}

filmes.values()
filmes.keys()
filmes.items()
locadora=[]
print(locadora[0]["ano"])
print(locadora[1]["titulo"])

pessoa = {"nome":"joao", "telefone": 123, "idade": 22}
print(pessoa["nome"])
print(pessoa["telefone"])
d={}


carros = {}
modelos_disp = []
for quantidade in range (0,3):
    carros['modelo'] = input("Informe o modelo do carro: ")
    carros['marca'] = input("Informe a marca do carro: ")
    carros['ano'] = int(input("Informe o ano do carro: "))
    modelos_disp.append(carros.copy())

for e in carros:
    for chave, valor in carros.items():
        print(f"{chave} = {valor}")
        




brasil = []
estado1 = {'uf':'Paraná', 'sigla': 'PR'}
estado2 = {'uf':'Santa Catarina', 'sigla': 'SC'}
estado3 = {'uf':'Rio Grande do Sul', 'sigla': 'RS'}
brasil.append(estado1)
brasil.append(estado2)
brasil.append(estado3)
print(brasil)
print(brasil[0]['uf'])
print(brasil[3]['sigla'])

for k in d.values():
    print(k)


from operator import itemgetter

contato = {"Beatriz": 1.77,
            "Maria Helena": 1.70,
            "Cecília": 1.67,
            "Daniela": 1.70}
for nome, altura in sorted(contato.items(), key=itemgetter(1)):
    print(f"{nome} --> {altura:.2f}m")

