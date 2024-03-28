estados = {
    'estado1':{
        'uf':'Paraná',
        'sigla':'PR'},
    'estado2':{
        'uf':'São Paulo',
        'sigla':'SP'},
    'estado3':{
        'uf':'Santa Catarina',
        'sigla':'SC'},
    'estado4':{
        'uf':'Minas Gerais',
        'sigla':'MG'},
}

estados['estado5'] = {'uf':'Bahia','sigla':'BA'}

for chave in estados.keys():
    print(chave)
    for chaveInterna, valorInterno in estados[chave].items():
        print(chaveInterna, valorInterno)
    print()

