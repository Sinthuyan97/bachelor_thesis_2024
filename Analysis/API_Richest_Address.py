import requests
import pandas as pd

# URL for the API endpoint
url = "http://127.0.0.1:8000/api/explorer/v2/ledger/richest-addresses?ledgerIndex=1005429"



payload={}
# Headers to accept JSON response
headers = {
    "Accept": "application/json"
}

# Make the GET request

response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)
# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print("Data fetched successfully:")
    print(data)  # Print the entire data for debugging

    # Extract 'top' data
    addresses = data.get('top', [])

    if not addresses:
        print("No addresses found in the response.")
    else:
        # Extract pubKeyHash and balance for each address
        extracted_data = []
        for item in addresses:
            print(f"Processing item: {item}")  # Debugging output
            address_info = item.get('address', [])
            balance = item.get('balance', '')
            print(f"Address info: {address_info}, Balance: {balance}")  # Debugging output
            if isinstance(address_info, list):
                for addr in address_info:
                    print(f"Processing addr: {addr}")  # Debugging output
                    if isinstance(addr, dict):
                        pubKeyHash = addr.get('pubKeyHash', '')
                        print(f"Extracted pubKeyHash: {pubKeyHash}")  # Debugging output
                        extracted_data.append({
                            'pubKeyHash': pubKeyHash,
                            'balance': balance
                        })

        if not extracted_data:
            print("No valid address data extracted.")
        else:
            # Print the extracted addresses to the console
            for entry in extracted_data:
                print(f"Address: {entry['pubKeyHash']}, Balance: {entry['balance']}")

            # Convert the data to a pandas DataFrame
            df = pd.DataFrame(extracted_data)

            # Save the DataFrame to a CSV file
            df.to_csv('richest_addresses.csv', index=False)
            print("Data saved to richest_addresses.csv")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")