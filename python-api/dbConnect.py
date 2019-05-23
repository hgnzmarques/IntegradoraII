import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user = "admin",
                                  password = "teste",
                                  host = "3.92.211.255",
                                  port = "5432",
                                  database = "INTEGRADORA")
    cursor = connection.cursor()
    cursor.execute("SELECT count(utm_campaign), utm_campaign FROM contributions WHERE utm_campaign is not null GROUP BY utm_campaign ORDER BY count(utm_campaign) DESC")
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

#Select payment methods and the aproval %
#select payment_method from contributions limit 10;

#Seleciona todos os valores das vakinhas por purpose(tipo de vakinha), e pode ser usado para fazer o gráfico da mediana dos valores
#SELECT ct.value as valor from contributions ct INNER JOIN vakinhas vk ON ct.vakinha_id = vk.id WHERE vk.purpose = (SELECT purpose FROM vakinhas WHERE id = "id da vakinha selecionada") limit 10

#Seleciona uma Tupla sendo (count de quanto aparece, nome do tipo), procurando quais as "redes sociais" que foram usadas para informar a vakinha
#SELECT count(utm_campaign), utm_campaign FROM contributions WHERE utm_campaign is not null GROUP BY utm_campaign ORDER BY count(utm_campaign) DESC