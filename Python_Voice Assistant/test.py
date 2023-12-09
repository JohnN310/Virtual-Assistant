import requests
import json

url = 'https://newsapi.org/v2/everything?q=tesla&from=2023-11-09&sortBy=publishedAt&apiKey=3e08910778ea403aa5649faab8fbb916'

response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the content of the response
    print(response.text)
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code}")
