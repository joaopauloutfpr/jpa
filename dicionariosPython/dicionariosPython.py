'''pessoas = {
    "pessoa1":{
        'nome':'Vovó Juju',
        'endereço':'Rua dos Abacates',
        'telefone': '(42) 4444-4444',
        'sexo':'F',
        'idade':80,
    },
    "pessoa2":{
        'nome':'Harry Potter',
        'endereço':'Rua dos Alfeneiros',
        'telefone': '(41) 5555-0000',
        'sexo':'M',
        'idade':17,
    },
}'''
pessoa = {}
pessoa = {
    'nome':'Joao',
    'idade':20,
}
pessoa['endereco'] = 'Rua Y'
'''for chave in pessoa.keys():
    print(pessoa[chave])

for valor in pessoa.values():
    print(valor)
'''
pessoa['nome'] = 'Ana Maria Braga'
pessoa.update({"idade":60})
for chave, valor in pessoa.items():
    print(chave,valor)


lista = []
lista.append('Joao')
lista.append(1289)
lista.append('19/10/1987')
