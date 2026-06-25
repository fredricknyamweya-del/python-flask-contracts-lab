#!/usr/bin/env python3

from flask import Flask, jsonify, make_response

contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a business"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}
]

customers = ["bob", "bill", "john", "sarah"]

app = Flask(__name__)

# Route: /contract/<id>
@app.route('/contract/<int:id>', methods=['GET'])
def get_contract(id):
    for contract in contracts:
        if contract["id"] == id:
            return jsonify(contract), 200
    return make_response(jsonify({"error": "Contract not found"}), 404)

# Route: /customer/<customer_name>
@app.route('/customer/<customer_name>', methods=['GET'])
def get_customer(customer_name):
    if customer_name.lower() in customers:
        return '', 204  # No Content, customer exists but info is sensitive
    return make_response(jsonify({"error": "Customer not found"}), 404)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
