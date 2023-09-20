import sqlite3 as conector

def cria_banco():
    try:
         print("abrindo conexão")
         conexao = conector.connect("meu_banco.db")
         cursor = conexao.cursor()
         sql = """CREATE TABLE cad_alunos
         (
            matricula INTEGER primary key AUTOINCREMENT,
          nome TEXT,
          data_nasc DATE,
          altura FLOAT,
          notas FLOAT,
          email TEXT
          );"""

         cursor.execute(sql)
         cursor.fetchall()
         conexao.commit()
         print('conexao encerrada')
    except Exception as err:
        print('erro encontrado na execucao da criacao do banco  cad_alunos ' +err)
    finally:
        if(conexao):
            conexao.close()
            cursor.close()

def cria_banco_emails():
    try:
        con = conector.connect('emails.db')
        cur = con.cursor()

        sql = 'create table if not exists emails (id integer primary key AUTOINCREMENT, nome varchar(100),email varchar (100))'
        cur.execute(sql)
        sql = 'insert into emails values (null,?,?)'

        recset = [('jane','jane@gmail.com')]
        for rec in recset:
            cur.execute(sql,rec)
        con.commit()
        cur.execute('select * from emails')
        recset = cur.fetchall()

        for rec in recset:
            print('%d: %s(%s)' % rec)
        con.close()
    except Exception as err:
        print("erro na criacao do banco emails " +err)
    finally:
        if(con):
            con.close()
            cur.close()

