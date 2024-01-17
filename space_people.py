import requests

response = requests.get('some_api_url')

json = response.json()

# for _ in range(5):
for person in json['people']:
    print(person['name'])