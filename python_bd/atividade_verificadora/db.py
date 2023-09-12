import sqlite3 as conector
#cria as duas tabelas necessarias ja na instanciacao
class DbUtils:
    pass


      def criarTabelas():
        conexao = conector.connect('escola.db')
        cursor = conexao.cursor()
        #tabela alunos
        sql = '''CREATE TABLE if not exists tbaluno (
            matricula INTEGER NOT NULL,
            nome TEXT NOT NULL,
            curso TEXT NOT NULL,
            PRIMARY KEY (matricula)
            );'''
        cursor.execute(sql)
        #tabela nota
        sql = '''CREATE TABLE if not exists tbnota (
            item INTEGER PRIMARY KEY AUTOINCREMENT,
            valor FLOAT NOT NULL,
            matricula INTEGER NOT NULL,
            FOREIGN KEY (matricula) REFERENCES tbaluno(matricula)
            );'''
        conexao.commit()
        cursor.close()
        conexao.close()

