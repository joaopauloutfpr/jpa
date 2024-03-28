import psycopg2
#liberar conexão de todos, editar pg_hba.conf PostgreSQL
#host all all 0.0.0.0/0 md5
class Conexao():
    def __init__(self, host = "localhost", db = "corridas",
                 user = "postgres", password="postgres"):
        self.host = host
        self.db = db
        self.usuario = user
        self.senha = password

    def conectar(self):
        try:
            self.conexao = psycopg2.connect(host=self.host,
                                            database=self.db,
                                            user=self.usuario,
                                            password=self.senha)
            self.cursor = self.conexao.cursor()
            print("Conectado ao PostgreSQL")

        except Exception as e:
            print("Erro de conexao")
            print(e)

    def desconectar(self):
        self.conexao.close()
        print("Desconectado do PostgreSQL")

    def executaDDL(self, sql):
        self.conectar()
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.desconectar()
        return resultado

    def executaDML(self, sql):
        try:
            self.conectar()
            self.cursor.execute(sql)
            self.conexao.commit()
            self.desconectar()
        except Exception as e:
            print("Erro ", e)