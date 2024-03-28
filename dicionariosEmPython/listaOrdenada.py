from random import randint
from operator import itemgetter

lista = [['Joao', 1000], ['Ana', 2000], ['Beto', 1500]]
print(lista)
lista1 =sorted(lista, key=itemgetter(0))
print(lista1)