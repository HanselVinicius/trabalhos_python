import psycopg2


class DbFactory:

    def __init__(self):
        pass


    def get_connection():
        conn = psycopg2.connect(database="db", user="postgres", password="postgres", host="localhost", port="5441")
        return conn

    def close_connection(conn):
        conn.close()