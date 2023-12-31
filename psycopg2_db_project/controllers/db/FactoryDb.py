import psycopg2



class DbFactory:


    def __init__(self):
        pass



    def get_connection():

        conn = psycopg2.connect(database="db", user="postgres", password="postgres", host="localhost", port="5441")

        return conn


    def close_connection(conn):

        conn.close()


    def create_tables_bd():

        try:

            conn = DbFactory.get_connection()

            cursor = conn.cursor()

            cursor.execute("""CREATE TABLE IF NOT EXISTS tb_produto (

                   codigo serial PRIMARY KEY,

                   descricao varchar(100) NOT NULL,

                   preco float NOT NULL,

                   data_criacao timestamp NOT NULL

                   );""")
                   

            cursor.execute("""CREATE TABLE IF NOT EXISTS tb_tipo_produto(

                 codigo serial PRIMARY KEY,

                 descricao varchar(100),

                 CONSTRAINT  fk_tb_produto FOREIGN KEY (codigo) REFERENCES tb_produto(codigo)

                 );""")


            conn.commit()

        except Exception as e:
            print(e)

        finally:

            cursor.close()

            DbFactory.close_connection(conn)    

    #talvez tenha havido um erro nao sei da onde tirei a tb_produto *-*
    def create_alunos_tb():
        conn = DbFactory.get_connection()
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS tb_aluno(
                
                codigo serial PRIMARY KEY,
    
                nome_aluno varchar(100) NOT NULL,
    
                nota1 float NOT NULL,
    
                nota2 float NOT NULL,
    
                media float NOT NULL,
    
                situacao varchar(12) NOT NULL
    
                );""")
        conn.commit()
        cursor.close()
        DbFactory.close_connection(conn)
