# Example using requests library in Python
import requests

response = requests.get('https://biggamesapi.io/api/collections')
data = response.json()
print(data)

