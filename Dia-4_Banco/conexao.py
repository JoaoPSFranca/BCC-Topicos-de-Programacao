from datetime import datetime
import mysql.connector # sudo pip install mysql-connector-python --break-system-packages

class ConexaoMySQL:
    def __init__(self, host, user, password, database, port):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.conexao = None

    def desconectar(self):
        if self.conexao and self.conexao.is_connected():
            self.conexao.close()
            print("Conexão com o banco de dados encerrada com sucesso.")
        else:
            print("Nenhuma conexão ativa para encerrar.")

    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
            if self.conexao.is_connected():
                print("Conexão com o banco de dados estabelecida com sucesso.")
        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")

    def ler_tabela(self, nome_tabela):
        if not self.conexao or not self.conexao.is_connected():
            print("Conexão com o banco de dados não está ativa.")
            return
        try:
            cursor = self.conexao.cursor()
            cursor.execute(f"SELECT * FROM {nome_tabela}")
            resultados = cursor.fetchall()
            return resultados

        except mysql.connector.Error as err:
            print(f"Erro ao ler a tabela '{nome_tabela}': {err}")

    def inserir_registro(self, nome_tabela, params):
        if not self.conexao or not self.conexao.is_connected():
            print("Conexão com o banco de dados não está ativa.")
            return
        try:
            cursor = self.conexao.cursor()
            placeholders = ', '.join(['%s'] * len(params))
            colunas = ', '.join(params.keys())
            valores = tuple(params.values())
            cursor.execute(f"INSERT INTO {nome_tabela} ({colunas}) VALUES ({placeholders})", valores)
            self.conexao.commit()
            print("Registro inserido com sucesso.")

        except mysql.connector.Error as err:
            print(f"Erro ao inserir o registro na tabela '{nome_tabela}': {err}")

    #Reformular
    def pesquisar_registro_por_data(self, nome_tabela, campo_data, data):
        if not self.conexao or not self.conexao.is_connected():
            print("Conexão com o banco de dados não está ativa.")
            return

        try:
            cursor = self.conexao.cursor()
            query = f"SELECT * FROM {nome_tabela} WHERE {campo_data} = %s"
            cursor.execute(query, (data,))
            resultados = cursor.fetchall()
            return resultados

        except mysql.connector.Error as err:
            print(f"Erro ao pesquisar registros na tabela '{nome_tabela}' pela data '{data}': {err}")

    def executar_query(self, nome_tabela, comando):
        if not self.conexao or not self.conexao.is_connected():
            print("Conexão com o banco de dados não está ativa.")
            return
        try:
            cursor = self.conexao.cursor()
            cursor.execute(comando)
            self.conexao.commit()
            print("Registro alterado com sucesso.")
        except mysql.connector.Error as err:
            print(f"Erro ao alterar o registro na tabela '{nome_tabela}': {err}")