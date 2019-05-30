import psycopg2
from psycopg2 import Error
from dataclasses import dataclass, field


DB_CONFIG = dict(
    user="admin",
    password="teste",
    host="3.88.132.194",
    port="5432",
    database="INTEGRADORA",
)


@dataclass
class Vakinha:
    _id: int
    title: str
    value: int


def run_query(query_string: str):
    try:
        with psycopg2.connect(**DB_CONFIG) as connection:
            cursor = connection.cursor()
            cursor.execute(query_string)
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    return cursor


def get_vakinhas_and_their_accumulated_money():
    query = (
        "select id, title, valor from vakinhas v "
        "left join(select sum(value)valor,vakinha_id from contributions "
        "group by vakinha_id) as c on c.vakinha_id = v.id "
        "where cast(ending_date as date) >= cast(now() as date) "
        "order by valor asc limit(4)"
    )
    cursor = run_query(query)
    vakinhas = [Vakinha(*row) for row in cursor]
    return vakinhas


if __name__ == "__main__":
    vacosas = get_vakinhas_and_their_accumulated_money()
    print(vacosas)



#Select payment methods and the aproval %
#select payment_method from contributions limit 10;

#Seleciona todos os valores das vakinhas por purpose(tipo de vakinha), e pode ser usado para fazer o gráfico da mediana dos valores
#SELECT ct.value as valor from contributions ct INNER JOIN vakinhas vk ON ct.vakinha_id = vk.id WHERE vk.purpose = (SELECT purpose FROM vakinhas WHERE id = "id da vakinha selecionada") limit 10

#Seleciona uma Tupla sendo (count de quanto aparece, nome do tipo), procurando quais as "redes sociais" que foram usadas para informar a vakinha
#select count(tipo)cnt, case when tipo is null then 'TOTAL' else tipo end TIPO from( SELECT case when utm_campaign in('whatsapp','facebook','twitter','mail') then utm_campaign else 'Outros' end tipo FROM contributions WHERE utm_campaign is not null)x GROUP BY rollup(x.tipo) ORDER BY cnt DESC

#
#
#select id, title, valor from vakinhas v
#outer apply(select sum(value) valor from contributions c where c.vakinha_id = v.id)c
# where cast(ending_date as date) >= cast(getdate() as date) order by valor asc limit(4)

