'''#dicionários dentro de dicionários
d1 = {
    'Cliente 1':{
        'Nome':'Joao',
        'Sobrenome':'Paulo',
        'Telefone':'123456',
        'Bairro':'Laranjeira'
    },
    'Cliente 2':{
        'Nome':'Simone',
        'Sobrenome':'Bello',
        'Telefone':'444444',
        'Bairro':'Abacateiro'
    },
    'Cliente 3':{
        'Nome':'Isabella',
        'Sobrenome':'Aires',
        'Telefone':'548756',
        'Bairro':'Jaboticabeira'
    },
    'Cliente 4':{
        'Nome':'Lívia',
        'Sobrenome':'Aires',
        'Telefone':'987456',
        'Bairro':'Limoeiro'
    },
}

#primeiro for trabalha com a parte externa
for indice,valor in d1.items():
    print(f'Exibindo {indice}')
    for indice,valor in valor.items():
        print(f'\t{indice} = {valor}')
'''

pessoa = dict({"nome": 'João', 'País': 'Brasil', 'Telefone': 123})
print(pessoa)

d = {}
d['joao'] = 20
d['maria'] = 30
d['pedro'] = 25

if 'pedro' in d.keys():
    print('Chave encontrada')
    del d['pedro']
else:
    print('Chave não encontrada')


#del d['Juca']