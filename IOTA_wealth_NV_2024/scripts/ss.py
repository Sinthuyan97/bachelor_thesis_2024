import pandas as pd

# Correct path to the mapping file
mapping_file = '/Users/sinth/OneDrive/Desktop/IOTA_DATASET/IOTA_wealth_NV_2024/IOTA_wealth_NV_2024/data/iota_h0_h1_address_ids.csv'
mapping_df = pd.read_csv(mapping_file)

# Address you want to check
address = '22a98444cebb7b6938f5bb44bf3df90fcd2af3a7d2c7c55347a251a228c85e46'
if address in mapping_df['address'].values:
    print("Address is correctly mapped.")
    address_id = mapping_df.loc[mapping_df['address'] == address, 'address_id'].iloc[0]
    print("Address ID:", address_id)
else:
    print("Address mapping error: Address not found in the mapping file.")

# Assuming you have a transaction file where addresses have been replaced with IDs (adjust path and filename as necessary)
transaction_file = '/Users/sinth/OneDrive/Desktop/IOTA_DATASET/iota_tx_data/IOTA_1year_tx_data.csv'
transactions_df = pd.read_csv(transaction_file)

# Verify transactions involving the address ID
involved_transactions = transactions_df[(transactions_df['input_addresses_x'].astype(str) == str(address_id)) |
                                        (transactions_df['output_addresses_y'].astype(str) == str(address_id))]

if not involved_transactions.empty:
    print(f"Found {len(involved_transactions)} transactions involving the address ID.")
    print(involved_transactions.head())
else:
    print("No transactions found for the address ID. Possible processing error.")