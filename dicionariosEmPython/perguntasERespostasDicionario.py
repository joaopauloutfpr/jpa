perguntas = {
    'Pergunta 1':{
        'pergunta':'Quem descobriu o Brasil?',
        'respostas': {'a':'Cabral','b':'Cabreu','c':'Cabrol','d':'Cabrul'},
        'resposta_certa': 'a',
    },'Pergunta 2':{
        'pergunta':'Qual é o valor de 2 + 2?',
        'respostas': {'a':'2','b':'3','c':'4','d':'5'},
        'resposta_certa': 'c',
    },'Pergunta 3':{
        'pergunta':'Qual é a tradução de blue?',
        'respostas': {'a':'Marrom','b':'Azul','c':'Verde','d':'Amarelo'},
        'resposta_certa': 'b',
    },'Pergunta 4':{
        'pergunta':'Qual é o complemento da frase: "Quem tem boca, vaia ..."',
        'respostas': {'a':'Espanha','b':'Lisboa','c':'Tóquio','d':'Roma'},
        'resposta_certa': 'd',
    }
}

totaliza_certas = 0

for perguntasc, perguntasv in perguntas.items():
    print(f'{perguntasc}: {perguntasv["pergunta"]}')
    for i,v in perguntasv["respostas"].items():
        print(f'{i}) {v}')

    resposta_usuario = input("Registre sua resposta: ")
    if resposta_usuario == perguntasv["resposta_certa"]:
        print("VOCÊ ACERTOU!")
        totaliza_certas+=1
    else:
        print("VOCÊ ERROU!")
    print()

#recupera a quantidade de perguntas registradas
qtde_perguntas = len(perguntas)
aproveitamento = totaliza_certas/qtde_perguntas * 100
print()
print(f"Você acertou {totaliza_certas} respostas de {qtde_perguntas} perguntas.")
print(f"Seu aproveitamento foi de {aproveitamento}%")