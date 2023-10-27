from controllers.db.FactoryDb import DbFactory
class SchoolController:
    def __init__(self):
        pass


    def getAllData(self):
        conn = DbFactory.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tb_aluno")
        rows = cursor.fetchall()
        return rows


    def insert(self,aluno):
        conn = DbFactory.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tb_aluno(nome_aluno,nota1,nota2,media,situacao) VALUES(%s,%s,%s,%s,%s)",(aluno.getNomeAluno(),aluno.getNota1(),aluno.getNota2(),aluno.getMedia(),aluno.getSituacao()))
        conn.commit()
        cursor.close()
        conn.close()