'''
O código visita a página corridasbr e 
retorna as próximas corridas de Ponta Grossa
'''

import requests
from bs4 import BeautifulSoup

# URL da página
url = "http://www.corridasbr.com.br/PR/por_cidade.asp?cidade=Ponta%20Grossa"
# url = "http://www.corridasbr.com.br/PR/por_cidade.asp?cidade=Carambe%ED"

# Faz a requisição para obter o conteúdo da página
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Obtém o conteúdo HTML da página
    html = response.text

    # Parseia o HTML com BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar todas as tabelas na página
    tabelas = soup.find_all('table')

    # Itera sobre as tabelas e verifica se a coluna 'data' está presente nos cabeçalhos
    for i, tabela in enumerate(tabelas):
        # Encontrar os cabeçalhos da tabela
        cabecalhos = tabela.find_all('td')
        # print(cabecalhos)

        # Verificar se 'data' está presente nos cabeçalhos
        if any('data' in cabecalho.text.lower() for cabecalho in cabecalhos):
            print(f"Tabela {i + 1}:")
            linhas = tabela.find_all('tr')
            for linha in linhas:
                colunas = linha.find_all(['tr', 'td'])
                for coluna in colunas:
                    print(coluna.text.strip(), end='  ')
                print()
            print("\n" + "=" * 50 + "\n")

else:
    print(
        f"Erro ao acessar a página. Código de status: {response.status_code}")
