'''
Crie um programa no qual 5 jogadores joguem um dado
e tenham resultados aleatórios. Guarde esses
resultados em um dicionário. No final, coloque esse
dicionário em ordem, sabendo que o vencedor tirou
o maior número no dado.

Saída:

VALORES SORTEADOS:
  O jogador 1 tirou 6
  O jogador 2 tirou 3
  O jogador 3 tirou 5
  O jogador 4 tirou 4

RANKING DOS JOGADORES:
  1º lugar: jogador1 com 6
  2º lugar: jogador3 com 5
  3º lugar: jogador4 com 4
  4º lugar: jogador2 com 3
'''
from random import randint
from time import sleep

#função que permite ordenar valores em uma lista
from operator import itemgetter
sorted()
jogadas = {'jogador1':randint(1,6),
           'jogador2':randint(1,6),
           'jogador3':randint(1,6),
           'jogador4':randint(1,6),
           }

ranking = list()

print("VALORES SORTEADOS")
for k,v in jogadas.items():
    print(f'O {k} tirou {v}')
    sleep(1)

#O resultado ficará como uma lista, não como um dic
#itemgetter(1) indica que estou trabalhando com o segundo elemento
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print(ranking)

#enumerate retorna uma tupla com o contador e o valor
for k, v in enumerate(ranking):
    print(f'{k+1}º lugar: {v[0]} com o valor {v[1]}')
