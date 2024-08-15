import requests
import csv

# URL to fetch data
url = "https://chronicle.stardust-mainnet.iotaledger.net/api/explorer/v2/ledger/richest-addresses?ledger_index=1002459&top=100"

# Send HTTP GET request to the API endpoint
response = requests.get(url)
response.raise_for_status()  # Raises an exception for HTTP errors

# Parse JSON response
data = response.json()

# Define the CSV file path
csv_file_path = 'richest_addresses.csv'

# Create or open the CSV file
with open(csv_file_path, 'w', newline='') as csvfile:
    # Create a CSV writer object
    fieldnames = ['address', 'balance']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write each address and balance to the CSV
    for item in data['top']:
        writer.writerow({'address': item['address'], 'balance': item['balance']})

print(f"CSV file '{csv_file_path}' has been created successfully.")