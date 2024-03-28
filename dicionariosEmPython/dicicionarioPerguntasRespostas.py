perguntas ={
    'Pergunta 1':{
        'pergunta': 'Quanto é 2+2?',
        'respostas':{'a':'1','b':'4','c':'2','d':'5'},
        'resposta_certa': 'b',
    },

    'Pergunta 2':{
        'pergunta': 'Quanto é 3*2?',
        'respostas':{'a':'6','b':'5','c':'7','d':'10'},
        'resposta_certa': 'a',
    },

}
print()
respostas_certas=0
#acessando as perguntas
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    #acessando as respostas
    print("Respostas:")
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input("Sua resposta: ")
    if resposta_usuario==pv['resposta_certa']:
        print("Você acertou!")
        respostas_certas+=1
    else:
        print("Você errou")
    print()

qtde_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtde_perguntas * 100
print(f'Você acertou {respostas_certas} respostas')
print(f'Sua porcentagem de acertos foi de {porcentagem_acerto}%')