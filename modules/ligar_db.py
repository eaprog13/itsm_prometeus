import psycopg

def get_connection():
    return psycopg.connect(
        host="localhost",
        dbname="itsm_prometeus",
        user="postgres",
        password="postgres"
    )