from random import randint
from operator import itemgetter

lista = [['joao',999,1000],['ana',222,2000],['beto',333,1500]]
dic1 = {'joao':111,
        'ana':1,
        'maria':241,
        'pedro':3,
        }
print(dic1)
lista1 = list(dic1.items())
print(lista1)
print(sorted(lista1,key=itemgetter(1)))
for k,v in enumerate(lista1):
    print(f'Nome: {v[0]} | Número: {v[1]}')


#print(lista)

#print(sorted(lista,key=itemgetter(0)))
