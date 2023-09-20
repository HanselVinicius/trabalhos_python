import sqlite3 as conector
from aluno import Aluno
from nota import Nota 
#cria as duas tabelas necessarias ja na instanciacao
class DbUtils:

    def __init__(self):
        self._criarTabelas()

        

    def _criarTabelas(self):
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
            valor FLOAT,
            matricula INTEGER NOT NULL,
            FOREIGN KEY (matricula) REFERENCES tbaluno(matricula)
            );'''
        cursor.execute(sql) 
        conexao.commit()
        cursor.close()
        conexao.close()

    # 
    def insert_aluno(self,aluno,nota):
        conexao = conector.connect('escola.db')
        cursor = conexao.cursor()
        try:
            sql = '''INSERT INTO tbaluno (matricula, nome, curso)
                       VALUES (?, ?, ?)'''
            
            cursor.execute(sql, (aluno.matricula,aluno.nome,aluno.curso))
            sql = '''INSERT INTO tbnota (valor, matricula)
                      VALUES (?, ?)'''
            cursor.execute(sql, (nota.valor, aluno.matricula))
            conexao.commit()
            
        except conector.IntegrityError as e:
            conexao.rollback()
            print('JA POSSUI ESSE CADASTRO NO SISTEMA')
        finally:   
            cursor.close()
            conexao.close()     




    def select_alunos(self):
        conexao = conector.connect('escola.db')
        cursor = conexao.cursor()
        sql = "SELECT * FROM tbaluno"
        cursor.execute(sql)
        recset = cursor.fetchall()
        listaDeAlunos = []
        for aluno in recset:
            matricula, nome, curso = aluno
            listaDeAlunos.append(Aluno(matricula,nome,curso))
        cursor.close()
        conexao.close()
        return listaDeAlunos    


    def select_notas(self):
        conexao = conector.connect('escola.db')
        cursor = conexao.cursor()
        sql = "SELECT * FROM tbnota"
        cursor.execute(sql)
        recset = cursor.fetchall()
        listaDeNotas = []
        for nota in recset:
            item,valor,matricula = nota
            listaDeNotas.append(Nota(item,valor,matricula))
        cursor.close()
        conexao.close()
        return listaDeNotas   

    def updateAluno(self,newNome,newCurso,matriculaToUpdate):
        conexao = conector.connect('escola.db')
        cursor = conexao.cursor()
        try:
            sql = '''
                UPDATE tbaluno 
                SET nome = ?,
                    curso = ?
                WHERE matricula = ? 
            '''
            cursor.execute(sql,(newNome,newCurso,matriculaToUpdate))
            conexao.commit()
        except Exception as e :
            print('ERRO UPDATEALUNO', e)
        finally:
            cursor.close()
            conexao.close()    
        
    def updateNota(self,newValor,newItem,matriculaToUpdate):
        conexao = conector.connect('escola.db')
        cursor = conexao.cursor()
        try:
            sql = '''
                UPDATE tbnota
                SET item = ?,
                    valor = ?
                WHERE matricula = ? 
            '''
            cursor.execute(sql,(newItem,newValor,matriculaToUpdate))
            conexao.commit()
        except Exception as e :
            print('ERRO UPDATENOTA ', e)
        finally:
            cursor.close()
            conexao.close() 
    
            
            
        
