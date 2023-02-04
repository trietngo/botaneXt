import pandas as pd
import json

# Read the Excel file
df = pd.read_excel("plantdb.xlsx")

# Set the first column as the index
df.set_index(df.columns[0], inplace=True)

# Convert the DataFrame to a JSON string, using the index as the key
json_str = df.to_json(orient="index")

# Load the JSON string into a Python object
data = json.loads(json_str)

# Pretty-print the JSON data to a file
with open("example.json", "w") as f:
    json.dump(data, f, indent=4)
