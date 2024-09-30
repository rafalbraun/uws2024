import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Content-Type': 'application/json',
    'api-key': 'feba79e524aad71178fe8bf611458dfb'
}

##url = 'https://rekrutacja.teamwsuws.pl/events'
##url = 'https://rekrutacja.teamwsuws.pl/events/3'
url = 'https://rekrutacja.teamwsuws.pl/events/filter/?tag=piknik'

response = requests.get(url, headers=headers)

if response.status_code == 200:
    body = response.json()
    print(body)
else:
    print(f"Failed to retrieve data: {response.status_code}")
