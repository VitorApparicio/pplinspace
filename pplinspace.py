import json
import requests

url = 'http://api.open-notify.org/astros.json'

try:
	r = requests.get(url)
	print(f"Número de pessoas no espaço:", r.json()['number'])
except:
	print(f'ERROR: Cannot get data from source - {url}')