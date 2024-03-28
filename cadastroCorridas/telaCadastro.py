import sys
import psycopg2
from conexaoBD import *
import smtplib
import random
import win32com.client as win32

from cadastroCorridas import *

from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow, QWidget

class carregaTela(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        super().setupUi(self)
        self.pushButton.clicked.connect(self.gravaDados)

    def mensagemSalva(self):
        msg = QMessageBox()
        msg.setText("Dados gravados com sucesso.")
        msg.setDefaultButton(QMessageBox.Ok)
        msg.exec_()

    def mensagemEmail(self):
        msg = QMessageBox()
        msg.setText("E-mail enviado com sucesso.")
        msg.setDefaultButton(QMessageBox.Ok)
        msg.exec_()

    def gravaDados(self):
        conecta = Conexao()
        #conecta.conectar()
        id = random.randint(1,200000)
        nome = self.nome.text()
        cidade = self.cidade.text()
        dataprova = self.dataprova.text()
        datalimite = self.datalimite.text()
        valor = self.valorinscricao.text()
        link = self.link.text()

        sql = f"insert into corridasativas values(nextval('numero'),'{nome}','{cidade}','{dataprova}','{datalimite}','{valor}','{link}')"
        conecta.executaDML(sql)
        self.mensagemSalva()
        #self.enviaEmail()


    def consultaDados(self):
        conecta = Conexao()
        #conecta.conectar()
        sql = "select * from clientePy"

        resultado = conecta.executaDDL(sql)
        for linha in resultado:
            self.relatorio.append(linha[0])

    def enviaEmail(self):
        conecta = Conexao()
        #conecta.conectar()
        sql = "select * from corridasativas where datalimiteinscricao>=now()"
        resultado = conecta.executaDDL(sql)
        for linha in resultado:
            print(linha[0])

        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.To = 'appcorridas22@gmail.com'
        mail.Subject = 'Contatos cadastrados na Base JP'
        mail.HTMLBody = f'''
        <p>Prezados,</p>

        <p>Seguem os contatos cadastrados no BD.</p>

        <p>Usuários</p>
        {resultado.to_html()}
        <p>Qualquer dúvida estou à disposição.</p>

        <p>Att.,</p>
        <p>Joao Paulo</p>
        '''

        mail.Send()
        self.mensagemEmail()

if __name__ == "__main__":
    qt = QApplication(sys.argv)
    carregar = carregaTela()
    carregar.show()
    qt.exec_()