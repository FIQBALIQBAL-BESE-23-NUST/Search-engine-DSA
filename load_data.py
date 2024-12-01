import pandas as pd

# Load CSV file
csv_file_path = "your_dataset.csv"  # Replace with your CSV file name
csv_data = pd.read_csv(csv_file_path)

# Load JSON file
json_file_path = "your_dataset.json"  # Replace with your JSON file name
json_data = pd.read_json(json_file_path)

print("CSV Data:\n", csv_data.head())  # Display the first few rows of the CSV
print("JSON Data:\n", json_data.head())  # Display the first few rows of the JSON
