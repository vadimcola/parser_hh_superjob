import requests
import json

import os

#
# response_url = requests.get('https://api.hh.ru/vacancies')
# response_data = json.loads(response_url.text)
# job_title = response_data['items'][0]['name']
# salary_min = response_data['items'][0]['salary']['from']
# salary_max = response_data['items'][0]['salary']['to']
# employee_requirement = response_data['items'][0]['snippet']['requirement']
# id_vacancy = response_data['items'][0]['id']
# url_vacancy = f'https://hh.ru/vacancy/{id_vacancy}'
#
# print(response_data)


# API_KEY = os.environ.get('API-KEY')
# KEY = {'X-Api-App-Id': API_KEY}
# response_url = 'https://api.superjob.ru/2.0/vacancies'
# response = requests.get(response_url, headers=KEY)
# response_data = json.loads(response.text)
# url_vacancy = response_data['objects'][0]['link']
# job_title = response_data['objects'][0]['profession']
# salary_min = response_data['objects'][0]['payment_from']
# salary_max = response_data['objects'][0]['payment_to']
# employee_requirement = response_data['objects'][0]['candidat']
#
# print(response)
