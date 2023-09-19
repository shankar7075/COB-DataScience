import requests
import pandas as pd

# API endpoint
url = "https://api.binance.com/api/v3/ticker/24hr"

# Make a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Convert the JSON response into a Pandas DataFrame
    data = response.json()
    df = pd.DataFrame(data)

    # Specify the file path for the CSV file
    csv_file = "binance_ticker_data.csv"

    # Save the DataFrame to a CSV file
    df.to_csv(csv_file, index=False)

    print(f"Data has been successfully saved to {csv_file}")
else:
    print("Failed to retrieve data from the API")

