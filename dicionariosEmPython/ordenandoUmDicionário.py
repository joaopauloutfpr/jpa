from operator import itemgetter

d1 = {'JP' : 6.8,
      'Ana' : 7.9,
      'Maria' : 8.4,
      'Pedro' : 8.4}

lista = list()

lista = sorted(d1.items(),key=itemgetter(1),reverse=True)
print(d1)
print(lista)