import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Função para extrair dados das tabelas


def extrair_dados(url):
    dados = []

    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        tabelas = soup.find_all('table')

        for tabela in tabelas:
            cabecalhos = [cabecalho.text.strip()
                          for cabecalho in tabela.find_all('th')]
            if 'data' in cabecalhos:
                linhas = tabela.find_all('tr')
                for linha in linhas[1:]:  # Ignorando o cabeçalho
                    colunas = linha.find_all('td')
                    dados_linha = {}
                    for i, coluna in enumerate(colunas):
                        dados_linha[cabecalhos[i]] = coluna.text.strip()
                    dados.append(dados_linha)

    return dados

# Função para enviar e-mail


def enviar_email(resumo):
    # Configurações do servidor SMTP
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'joaopauloutfpr@gmail.com'
    smtp_password = 'sua_senha'

    # Configurações do e-mail
    from_email = 'seu_email@example.com'
    to_email = 'destinatario@example.com'
    subject = 'Resumo dos dados da página'

    # Construindo o e-mail
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Corpo do e-mail (resumo dos dados)
    body = ''
    for linha in resumo:
        for chave, valor in linha.items():
            body += f"{chave}: {valor}\n"
        body += '\n'
    msg.attach(MIMEText(body, 'plain'))

    # Enviando o e-mail
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(from_email, to_email, msg.as_string())


# URL da página
url = "http://www.corridasbr.com.br/PR/por_cidade.asp?cidade=Ponta%20Grossa"
# url = "http://www.corridasbr.com.br/PR/por_cidade.asp?cidade=Carambe%ED"

# Extrair dados da página
dados = extrair_dados(url)

# Enviar e-mail com o resumo dos dados
enviar_email(dados)
