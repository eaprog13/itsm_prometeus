import os

import psycopg

# As credenciais vêm de variáveis de ambiente — nunca ficam no código.
# Sem ITSM_DB_PASSWORD, o psycopg usa o PGPASSWORD ou o ficheiro pgpass.
def get_connection():
    return psycopg.connect(
        host=os.environ.get("ITSM_DB_HOST", "localhost"),
        dbname=os.environ.get("ITSM_DB_NAME", "itsm_prometeus"),
        user=os.environ.get("ITSM_DB_USER", "postgres"),
        password=os.environ.get("ITSM_DB_PASSWORD"),
    )
