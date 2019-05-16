import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user = "admin",
                                  password = "teste",
                                  host = "54.224.150.49",
                                  port = "5432",
                                  database = "INTEGRADORA")
    cursor = connection.cursor()
    cursor.execute("select birth from users limit 10;")
    record = cursor.fetchall()
    print(record)
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
