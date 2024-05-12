import pandas as pd

def csv_to_json_like(csv_file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Convert the DataFrame to a JSON-like format (list of dictionaries)
    json_like_data = df.to_dict(orient='records')
    
    return json_like_data

# Specify the path to your CSV file
csv_file_path = 'path_to_your_csv_file.csv'

# Convert CSV to JSON-like format
transactions_json_like = csv_to_json_like(csv_file_path)

# Display the first few entries to verify
print(transactions_json_like[:5])  # Adjust as needed to see more or fewer entries
