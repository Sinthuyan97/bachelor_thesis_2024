import pandas as pd

# Load the negative balance addresses
negative_file = 'iota_tx_2024/iota_tx/negative_balance_addresses.csv'
negative_addresses_df = pd.read_csv(negative_file)

# Load the mapping data
mapping_file = 'IOTA_wealth_NV_2024/data/iota_h0_h1_address_ids.csv'  # Adjust path as necessary
mapping_df = pd.read_csv(mapping_file)

# Convert the mapping dataframe to a dictionary for faster access
address_id_map = mapping_df.set_index('address')['address_id'].to_dict()

# Check each negative balance address in the mapping and prepare the output
results = []
for index, row in negative_addresses_df.iterrows():
    address = row['address']
    balance = row['balances']
    if address in address_id_map:
        address_id = address_id_map[address]
        mapped_status = 1
    else:
        address_id = None
        mapped_status = 0

    results.append((address_id, address, mapped_status, balance))

# Convert results to DataFrame
results_df = pd.DataFrame(results, columns=['Address ID', 'Address', 'Mapping Status', 'Balance'])
results_df.to_csv('mapping_results.csv', index=False)
print("Results have been saved to 'mapping_results.csv'.")



results_df = pd.read_csv('mapping_results.csv')
# Use value_counts to count occurrences of each mapping status
status_counts = results_df['Mapping Status'].value_counts()
# The DataFrame might not include unmapped if all were mapped, setting default to prevent errors
mapped_count = status_counts.get(1, 0)
not_mapped_count = status_counts.get(0, 0)
# Print the results
print(f"Number of Mapped Addresses: {mapped_count}")
print(f"Number of Not Mapped Addresses: {not_mapped_count}")