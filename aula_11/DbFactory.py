import psycopg2


class DbFactory:

    def __init__(self):
        pass
    
    @staticmethod
    def get_connection():
        conn = psycopg2.connect(database="db", user="postgres", password="postgres", host="localhost", port="5441")
        return conn

    # Criação da tabela
    @staticmethod
    def create_table_agenda():
        print("Criando tabela tb_agenda")
        try:
            conn = DbFactory.get_connection()
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS tb_agenda (id serial PRIMARY KEY, nome varchar(100) NOT NULL, telefone varchar(20) NOT NULL);")
            conn.commit()
        except Exception as e:
            print(e)
            