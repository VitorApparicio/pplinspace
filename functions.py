import json
import requests

def GetJson(jsonfile):
	r = requests.get(jsonfile)
	return r.json()
