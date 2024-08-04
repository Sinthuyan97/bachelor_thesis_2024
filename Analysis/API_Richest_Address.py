import requests

url = "http://127.0.0.1:8000/api/explorer/v2/ledger/richest-addresses"

params = {
    "ledgerIndex": 1005429,
    "top": 100
}

headers = {
    'Accept': 'application/json'
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    richest_addresses = response.json()
    if 'top' in richest_addresses and isinstance(richest_addresses['top'], list):
        for address_info in richest_addresses['top']:
            if 'address' in address_info and 'balance' in address_info:
                pubKeyHash = address_info['address'].get('pubKeyHash', 'N/A')
                balance = address_info.get('balance', 'N/A')
                print(f"Address: {pubKeyHash}, Balance: {balance}")
            else:
                print("Address info structure is unexpected:", address_info)
    else:
        print("Unexpected 'top' structure in the response:", richest_addresses)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}, Response: {response.text}")