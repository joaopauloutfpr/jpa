'''
1) Crie uma função que receba um dicionário com dados de funcionários (nome e salário)
Seu programa deverá verificar quais funcionários tem salário menor que um valor
informado por parâmetro.
Devem ser exibidos todos os funcionários (Nome e Salário), bem como
os funcionários com salário menores ou iguais ao parâmetro informado

'''

sample_dict = {
    'emp1':
        {'name': 'Jhon', 'salary': 7500},
    'emp2':
        {'name': 'Emma', 'salary': 80},
    'emp3':
        {'name': 'Brad', 'salary': 500}
}
menor = 10000
empregado = '1'

for ec, ev in sample_dict.items():
    print(f'Funcionário: {ev["name"]} | Salário: {ev["salary"]}')
    if ev["salary"] < menor:
        menor = ev["salary"]
        emp = ev["name"]

print(f"O funcionário {emp} tem o menor salário, no valor de {menor}")


'''    for v in ev['salary'].items():
#        print(v['salary'])
        if v < menor:
            menor = v['salary']
            emp = v['name']

#sample_dict['emp3']['salary'] = 8012
#print(sample_dict)
'''