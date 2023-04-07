import requests
import json

url = requests.get('https://api.hh.ru/vacancies')
response_data = json.loads(url.text)
job_title = response_data['items'][0]['name']
salary_min = response_data['items'][0]['salary']['from']
salary_max = response_data['items'][0]['salary']['to']
employee_requirement = response_data['items'][0]['snippet']['requirement']
id_vacancy = response_data['items'][0]['id']
url_vacancy = f'https://hh.ru/vacancy/{id_vacancy}'

print(url_vacancy)





