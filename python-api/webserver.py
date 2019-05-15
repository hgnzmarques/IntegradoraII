from typing import List
from random import randrange

from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/vakinha-creation/payment-methods-success-rate/', methods=['GET'])
def payment_methods_success_rate():
    '''
    Get percentage of successful payments for each payment method.
    '''
    payment_method: List[str] = [
        'bitcoin', 'mastercard', 'visa', 'boleto', 'doc', 'ted',
    ]
    percentages: List[float] = [
        100.0, 16.0, 27.0, 71.0, 72.0, 89.0,
    ]
    return jsonify([payment_method, percentages])


@app.route('/vakinha-creation/contributions_per_value/', methods=['GET'])
def contributions_per_value():
    '''
    
    '''
    values: List[int] = [x for x in range(0, 100, 10)]
    number_of_contributions: List[int] = [randrange(0, 40) for _ in range(0, 100, 10)]
    return jsonify([values, number_of_contributions])


app.run(host='0.0.0.0', port=8999, debug=True)
