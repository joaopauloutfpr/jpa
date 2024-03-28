'''
2) Crie uma função que receba um dicionário com dados de funcionários (nome e salário)
Seu programa deverá verificar quais funcionários tem salário menor que 3000
e dar um aumento de 10%.
No final, deve ser exibido o Nome e Salário iniciais de cada funcionário, os funcionários
que receberam o aumento (e o aumento realizado), bem como a impressão do dicionário
atualizado
'''

sample_dict = {
    'emp1':
        {'name': 'Jhon', 'salary': 7500},
    'emp2':
        {'name': 'Emma', 'salary': 81},
    'emp3':
        {'name': 'Brad', 'salary': 500}
}
print("LISTA DE FUNCIONÁRIOS")
for ec, ev in sample_dict.items():
    print(f'Funcionário: {ev["name"]} | Salário: {ev["salary"]}')
print()
print("REAJUSTES REALIZADOS")
for ec, ev in sample_dict.items():
    if ev["salary"] <= 1000:
        ev["salary"] = ev["salary"]*1.10
        print(f'Funcionário: {ev["name"]} | Salário: {ev["salary"]}')
print()
print("LISTA DE FUNCIONÁRIOS - ATUALIZAÇÃO DOS SALÁRIOS")
for ec, ev in sample_dict.items():
    print(f'Funcionário: {ev["name"]} | Salário: {ev["salary"]}')

#        menor = ev["salary"]
#        emp = ev["name"]

#print(f"O funcionário {emp} tem o menor salário, no valor de {menor}")