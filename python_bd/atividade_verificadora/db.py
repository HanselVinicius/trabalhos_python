import sqlite3 as conector
#cria as duas tabelas necessarias ja na instanciacao
class DbUtils:
    pass


    def criarTabelas():
        conexao = conector.connect('escola.db')
        cursor = conexao.cursor()
        #tabela alunos
        sql = "create table if not exists Aluno(matricula integer primary key AUTOINCREMENT, nome text,curso text);"
        cursor.execute(sql)
        #tabela nota
        sql = "create table if not exists Nota(item integer primary key AUTOINCREMENT, valor real)"
        conexao.commit()
        cursor.close()
        conexao.close()


