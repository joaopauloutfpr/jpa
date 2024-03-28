from tkinter import *

def metodo():
    global i
    i+=1
    texto.configure(text=str(i))

i = 0

janela = Tk()
janela.title("Esse é um título")
janela.geometry("500x300")
janela.resizable(width=False,height=False)
janela.configure(bg="cyan")

botao = Button(janela)
botao.configure(text="Clique aqui", command=metodo)
botao.grid(row=0,column=0)


texto = Label(janela)
texto.configure(text="Texto")
texto.grid(row=1,column=0)
janela.mainloop()