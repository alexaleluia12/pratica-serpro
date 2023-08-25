import os

import oracledb

DB_PASS = os.environ.get('NODE_ORACLEDB_PASSWORD')
DB_USER = os.environ.get('NODE_ORACLEDB_USER')
DB_CONN_STR = os.environ.get('NODE_ORACLEDB_CONNECTIONSTRING')


with oracledb.connect(user=DB_USER, password=DB_PASS, dsn=DB_CONN_STR) as connection:
    with connection.cursor() as cursor:
        sql = """SELECT * FROM no_example"""
        for r in cursor.execute(sql):
            print(r)
