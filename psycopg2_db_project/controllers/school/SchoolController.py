from controllers.db.FactoryDb import DbFactory
from model.aluno.Aluno import Aluno
from model.exceptions.DbException import DbException
class SchoolController:
    def __init__(self):
        pass


    def getAllData(self):
        try:
            conn = DbFactory.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tb_aluno")
            rows = cursor.fetchall()
            resultList = []
            for row in rows:
                resultList.append(Aluno(row[0],row[1],row[2],row[3]))
            return resultList
        except:
            cursor.close()
            conn.close()
            raise DbException(message="ERRO AO ACESSAR O BANCO DE DADOS")
        


    def insert(self,aluno):
        try:
            conn = DbFactory.get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tb_aluno(nome_aluno,nota1,nota2,media,situacao) VALUES(%s,%s,%s,%s,%s)",(aluno.getNomeAluno(),aluno.getNota1(),aluno.getNota2(),aluno.getMedia(),aluno.getSituacao()))
            conn.commit()
            cursor.close()
            conn.close()
        except:
            cursor.close()
            conn.close()
            raise DbException(message="ERRO AO ACESSAR O BANCO DE DADOS")    


    def getByid(self,id):
        try:
            conn = DbFactory.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tb_aluno WHERE codigo = %s",(id,))
            row = cursor.fetchone()
            aluno = Aluno(row[0],row[1],row[2],row[3])
            return aluno        
        except:
            cursor.close()
            conn.close()
            raise DbException(message="ERRO AO ACESSAR O BANCO DE DADOS")
    
    def update(self,aluno):
        try:
            conn = DbFactory.get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE tb_aluno SET nome_aluno = %s,nota1 = %s,nota2 = %s,media = %s,situacao = %s WHERE codigo = %s",(aluno.getNomeAluno(),aluno.getNota1(),aluno.getNota2(),aluno.getMedia(),aluno.getSituacao(),aluno.getId()))
            conn.commit()
            cursor.close()
            conn.close()
        except:
            cursor.close()
            conn.close()
            raise DbException(message="ERRO AO ACESSAR O BANCO DE DADOS")

    def delete(self,id):
        try:
            conn = DbFactory.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tb_aluno WHERE codigo = %s",(id,))
            conn.commit()
            cursor.close()
            conn.close()
        except:
            cursor.close()
            conn.close()
            raise DbException(message="ERRO AO ACESSAR O BANCO DE DADOS")   