#cada índice é único, valor único sem repetição
#se repetir, fica valendo o último valor inserido
#para definir a chave, pode-se usar qualquer valor imutável str ou int
dicionario = {'indice1':'valor 1',
              'indice2':'valor 2',
              'indice3':'valor 3',
              'indice4':'valor 4',
              'indice5':'valor 5'}
print(dicionario)
#outra forma para adicionar uma nova chave/valor
#se usar o mesmo código abaixo, para um índice existente, ele atualiza o valor/substitui
dicionario['nova chave'] = 'valor nova chave'
print(dicionario)

#se usar o mesmo código abaixo, para um índice existente, ele atualiza o valor/substitui
dicionario['indice1'] = 'valor alterado'
print(dicionario)

#outra forma de atualizar/inserir um valor de índice
#a função update recebe um dicionário - par de chave e valor
dicionario.update({'indice2':'mudou com update'})
print(dicionario)

#para excluir uma chave, usa-se o comando del
print(dicionario)
del dicionario['indice1']
print("Apagou indice 1")
print(dicionario)

#para acessar um determinado valor, basta indicar o nome da chave

print(dicionario['indice2'])
#ao indicar um índice inexistente, um erro é lançado e o programa para de funcionar

#print(dicionario['indice'])

#para isso, é importante validar a existência do índice
#caso não exista, pode pedir para adicionar

if 'indice6' in dicionario:
    print(dicionario['indice6'])
#se não existir, cria a chave/valor
else:
    dicionario['indice6']='valor 6'

print(dicionario)

#outra forma de retornar um valor, é usar o método get do dicionario

print(dicionario.get('indice1'))
#caso não exista, retorna None, mas não para o código
#para não retornar None, pode-se validar a existencia antes de imprimir

if dicionario.get('indice1') is not None:
    print(dicionario.get('indice1'))

#visitando valores
print('indice2' in dicionario)
print('valor 3' in dicionario.values())

#retorna quantos pares existem
print(len(dicionario))
#iterando sobre dicionários -
#in dicionario, retorna os índices
print("iterando")
#.values, retorna os valores
for item in dicionario.values():
    print(item)

print("Retornando a dupla de informações")
#para retornar índice e valor
for item in dicionario.items():
    print(item[0], item[1])

#outra forma, é usar um par de valores no for
print()
for indice,valor in dicionario.items():
    print(indice, valor)

#o sinal de atribuição, não serve para copiar um dicionário
#ele referencia os mesmos valores
#Se fizer uma mudança no segundo, muda no primeiro tb

#para fazer uma cópia real, usa-se a biblioteca
#import copy
#dic2 = copy.deepcopy(dicionario)
