import json
import requests
from functions import GetJson

x = True
while x:
	try:
		print("\n(1) Número de pessoas no espaço:")
		print("(2) Posição atual da ISS:")
		print("(3) Sair")
		num = int(input('Escolha a opção desejada: '))
	except:
		continue
	if num == 1:
		url = 'http://api.open-notify.org/astros.json'
		print(GetJson(url)['number'])
	if num == 2:
		url = 'http://api.open-notify.org/iss-now.json'
		iss = GetJson(url)
		for key, value in iss['iss_position'].items():
			print(key,": ", value)
	if num == 3:
		exit(0)
