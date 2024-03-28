import time
import google

#digita no campo
#grava no arquivo txt
#lê do arquivo TXT

import tkinter
from tkinter import *


def gravar(logfile='arq.txt'):
    texto_digitado = texto1.get(1.0, END)
    print("Texto digitado = ", texto_digitado)
    naoExiste = 0
    total = 1

    #verifica se o texto não existe
    with open(logfile, "r") as file:
        linhas = file.readlines()
        qtdeLinhas = len(linhas)
        print("qtde de linhas =", qtdeLinhas)
        if qtdeLinhas == 0:
            with open(logfile, "w") as file:
                file.write(texto_digitado)
        else:
            file.seek(0,0)
            while total<=qtdeLinhas:
                #linha = file.readline().strip()
                for linha in file:
                    print("LINHA LIDA: ", linha)
                    if linha == texto_digitado:
                        naoExiste+=1
                        print("nao existe = ",naoExiste)
                    total += 1

    file.close()
    print('chegou aqui')

    #grava o texto no arquiv
    if naoExiste==0:
        with open(logfile, "w") as file:
            file.write('\n'+texto_digitado)
    file.close()
'''    with open(logfile, "a") as file:
        linhas = file.readlines()
        qtdeLinhas = len(linhas)
        while total<qtdeLinhas:
            linha = file.readline().strip()
            if linha == texto_digitado:
                naoExiste+=1
    if naoExiste == 0:
        file.write(texto_digitado)
    file.close()
'''
def verificarPlagio():
    texto_digitado = texto1.get(1.0, end='1.c')
    print(texto_digitado)
    try:
        from googlesearch import search
    except ImportError:
        print("Módulo GOOGLE não encontrado")
    query = texto_digitado

    for j in search(query, tld="co.in", num=5, stop=5, pause=2):
        print(j)


janela = Tk()
janela.title("Acender e apagar LED com botão")
janela.geometry("500x600")

frame = Frame(master=janela)
frame.pack()


texto1 = tkinter.Text(frame,
                   height = 10,
                   width = 40)
texto1.pack()

texto2 = tkinter.Text(frame,
                   height = 10,
                   width = 40)
texto2.pack()

botao = Button(master= frame, text="Gravar", command=gravar)
botao.pack()
botao2 = Button(master= frame, text="Verificar", command=verificarPlagio)
botao2.pack()

if __name__ == '__main__':
    janela.mainloop()
