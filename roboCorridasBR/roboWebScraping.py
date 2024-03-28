import requests
from bs4 import BeautifulSoup

# URL da página
url = "http://www.corridasbr.com.br/PR/por_cidade.asp?cidade=Ponta%20Grossa"

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

    # Itera sobre as tabelas e imprime seus conteúdos
    for i, tabela in enumerate(tabelas):
        print(f"Tabela {i + 1}:")
        linhas = tabela.find_all('tr')
        for linha in linhas:
            colunas = linha.find_all(['th', 'td'])
            for coluna in colunas:
                print(coluna.text.strip(), end='\t')
            print()
        print("\n" + "="*50 + "\n")

else:
    print(f"Erro ao acessar a página. Código de status: {response.status_code}")
