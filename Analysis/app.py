from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/explorer/v2/ledger/richest-addresses', methods=['GET'])
def get_richest_addresses():
    ledger_index = request.args.get('ledgerIndex', default=0, type=int)
    top = request.args.get('top', default=10, type=int)
    # Dummy data for demonstration
    addresses = [{'address': f'address_{i}', 'balance': 1000 - i} for i in range(top)]
    return jsonify({'ledgerIndex': ledger_index, 'top': addresses})

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)