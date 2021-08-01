import requests
import json
github_url = 'https://api.github.com'
user = 'Valerievna'
response = requests.get(f'{github_url}/users/{user}/repos')

print(f"Проверка статуса запроса \nСтатус:", response.status_code)

# Запись файла в формате json
with open('data.json', 'w') as f:
    json.dump(response.json(), f, sort_keys=True, indent=2)

print("Список репозиториев:")
for i in response.json():
    print(i['name'])


