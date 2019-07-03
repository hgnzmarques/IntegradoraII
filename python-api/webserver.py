from typing import List
from random import randrange
from dataclasses import dataclass, field, asdict

import psycopg2
from psycopg2 import Error
from flask import Flask, request, jsonify


app = Flask(__name__)


DB_CONFIG = dict(
    user="admin",
    password="teste",
    host="35.170.192.76",
    port="5432",
    database="INTEGRADORA",
)

@dataclass
class Vakinha:
    _id: int
    title: str
    value: float

    @classmethod
    def from_sql(cls, _id, title, value):
        return cls(_id, title, float(value))

# @dataclass
# class

# @app.route('/vakinha-creation/payment-methods-success-rate/', methods=['GET'])
# def payment_methods_success_rate():
#     '''
#     Get percentage of successful payments for each payment method.
#     '''
#     payment_method: List[str] = [
#         'bitcoin', 'mastercard', 'visa', 'boleto', 'doc', 'ted',
#     ]
#     percentages: List[float] = [
#         100.0, 16.0, 27.0, 71.0, 72.0, 89.0,
#     ]
#     return jsonify([payment_method, percentages])

# @app.route('/vakinha-creation/contributions_per_value/', methods=['GET'])
# def contributions_per_value():
#     values: List[int] = [x for x in range(0, 100, 10)]
#     number_of_contributions: List[int] = [randrange(0, 40) for _ in range(0, 100, 10)]
#     return jsonify([values, number_of_contributions])


def run_query(query_string: str):
    try:
        with psycopg2.connect(**DB_CONFIG) as connection:
            cursor = connection.cursor()
            cursor.execute(query_string)
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    return cursor

@app.route('/vakinha-lifetime/total_donated_per_vakinha_untill_now', methods=['GET'])
def get_total_donated_per_vakinha_untill_now():
    query = open("./queries/accumulated_vakinhas_money.sql").read()
    cursor = run_query(query)
    vakinhas = [
        asdict(Vakinha.from_sql(*row))
        for row in cursor
    ]
    return jsonify(vakinhas)

@app.route('/vakinha-lifetime/similar_vakinhas_to_the_user', methods=['GET'])
def similar_vakinhas_to_the_user():
    query = open("./queries/similar_vakinhas_to_the_user.sql").read()
    cursor = run_query(query)
    vakinhas = [
        asdict(Vakinha.from_sql(*row))
        for row in cursor
    ]
    return jsonify(vakinhas)

@app.route('/vakinha-lifetime/donation_methods_approval_rate', methods=['GET'])
def get_donation_methods_and_approval():
    query = open("queries/payment_methods_and_the_approval.sql").read()
    cursor = run_query(query)
    vakinhas = [
        asdict(Vakinha.from_sql(*row))
        for row in cursor
    ]
    return jsonify(vakinhas)

@app.route('/vakinha-lifetime/networks_used_to_find_u', methods=['GET'])
def get_social_networks_used_to_find_vakinha():
    query = open("queries/social_networks_used_to_find_vakinha.sql").read()
    cursor = run_query(query)
    vakinhas = [
        asdict(Vakinha.from_sql(*row))
        for row in cursor
    ]
    return jsonify(vakinhas)

@app.route('/vakinha-lifetime/price_by_pourpose', methods=['GET'])
def get_vakinhas_price_pourpose():
    query = open("queries/vakinha_price_by_pourpose.sql").read()
    cursor = run_query(query)
    vakinhas = [
        asdict(Vakinha.from_sql(*row))
        for row in cursor
    ]
    return jsonify(vakinhas)

app.run(host='0.0.0.0', port=8999, debug=True)
