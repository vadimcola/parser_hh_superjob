import requests
import json

url = requests.get('https://api.hh.ru/vacancies')
response_data = json.loads(url.text)


print(response_data)

