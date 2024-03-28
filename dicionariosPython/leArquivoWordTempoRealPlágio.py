'''import win32com.client

# cria uma instância do aplicativo Word
word = win32com.client.Dispatch("Word.Application")

# obtém o documento ativo (que está aberto)
doc = word.ActiveDocument

# armazena os parágrafos já exibidos
paragrafos_exibidos = []


# exibe o conteúdo do documento continuamente
while doc.Application.ActiveDocument:
    for paragrafo in doc.Paragraphs:
        # verifica se o parágrafo já foi exibido antes
        if paragrafo.Range.Text not in paragrafos_exibidos:
            # exibe o parágrafo e adiciona na lista de parágrafos exibidos
            print(paragrafo.Range.Text)
            paragrafos_exibidos.append(paragrafo.Range.Text)

# fecha o aplicativo Word
word.Quit()'''
import win32com.client

# cria uma instância do aplicativo Word
word = win32com.client.Dispatch("Word.Application")

# obtém o documento ativo (que está aberto)
doc = word.ActiveDocument

# armazena as frases já exibidas
frases_exibidas = []

# exibe o conteúdo do documento continuamente
while doc.Application.ActiveDocument:
    for paragrafo in doc.Paragraphs:
        # divide o parágrafo em frases utilizando o ponto final como separador
        frases = paragrafo.Range.Text.split(". ")
        for frase in frases:
            # verifica se a frase já foi exibida antes
            if frase not in frases_exibidas:
                # exibe a frase e adiciona na lista de frases exibidas
                frases_exibidas.append(frase)
                print(frase)

# fecha o aplicativo Word
word.Quit()