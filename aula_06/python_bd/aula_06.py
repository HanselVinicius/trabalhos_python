import sqlite3 as conector


def criar_tabela():
    print('abrindo conexao')
    conexao = conector.connect('academia.db')
    cursor = conexao.cursor()
    sql = "create table if not exists cadastro(codigo integer primary key AUTOINCREMENT, nome text,idade integer);"
    cursor.execute(sql)
    sql = "insert into cadastro (codigo,nome,idade) values (null,?,?);"
    recset = [('vinicius','21')]
    for rec in recset:
            cursor.execute(sql,rec)
    conexao.commit()
    cursor.close()
    conexao.close()





def alterar_table():
    print("abrindo uma conexao de db")
    conexao = conector.connect("academia.db")
    cursor = conexao.cursor()
    sql = "ALTER TABLE cadastro add  limite REAL;"
    cursor.execute(sql)
    sql = "UPDATE cadastro SET limite = 1000;"
    cursor.execute(sql)
    conexao.commit()
    cursor.close()
    conexao.close()


def select_all():
    conexao = conector.connect("academia.db")
    cursor = conexao.cursor()
    sql = "SELECT * FROM cadastro;"
    cursor.execute(sql)
    recset =  cursor.fetchall()
    print(recset)
    for rec in recset:
            print('%d: %s(%d) %f ' % rec)
    cursor.close()
    conexao.close()


criar_tabela()
alterar_table()
select_all()