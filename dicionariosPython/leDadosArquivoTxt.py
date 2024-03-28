import time

def verificarPlagio(texto_digitado):
    try:
        from googlesearch import search
    except ImportError:
        print("Módulo GOOGLE não encontrado")
    query = texto_digitado

    for j in search(query, tld="co.in", num=5, stop=5, pause=2):
        print(j)

def monitorar(logfile='arq.txt'):
    with open(logfile) as file:
        while True:
            linha = file.readline().strip()
            if linha:
                yield linha
                verificarPlagio(linha)
            else:
                time.sleep(.5)

if __name__ == '__main__':
    logfile = 'arq.txt'
    for item, linha in enumerate(monitorar(logfile)):
        print(item, linha)
        print('%s: %s' % (item, linha))
        print('{:6d}: {}'.format(item, linha))