import requests

URL = "https://transport.integration.sl.se/v1/sites?expand=true"
HEADERS = {"Content-Type": "application/json"}

# Send the GET request
response = requests.get(URL, headers=HEADERS)

# Parse the JSON response
data = response.json()

# Open a text file to write the output
with open('output.txt', 'w') as file:
    for item in data:  # Loop through each item in the data list
        # Use dictionary's get method for 'name' and 'id' with defaults
        name = item.get('name', 'No Name') if isinstance(item, dict) else 'No Name'
        id = item.get('id', 'No ID') if isinstance(item, dict) else 'No ID'
        # Write formatted string to the file
        file.write(f"{name}: {id}\n")

print("Output has been written to output.txt")