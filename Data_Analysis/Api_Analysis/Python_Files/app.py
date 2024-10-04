from flask import Flask, jsonify, request


app = Flask(__name__)


external_api_url = "http://127.0.0.1:8000/api/explorer/v2/ledger/richest-addresses"

@app.route('/api/explorer/v2/ledger/richest-addresses', methods=['GET'])
def richest_addresses():
    top = request.args.get('top', default=100, type=int)
    ledger_index = request.args.get('ledgerIndex', default=1005429, type=int)

    response_data = {
        'top': top,
        'ledgerIndex': ledger_index
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)