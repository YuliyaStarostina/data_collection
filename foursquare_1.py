
# Домашнее задание 1
# Напишите сценарий на языке Python, который предложит пользователю ввести интересующую его категорию (например, кофейни, музеи, парки и т.д.).
# Используйте API Foursquare для поиска заведений в указанной категории.
# Получите название заведения, его адрес и рейтинг для каждого из них.
# # Скрипт должен вывести название и адрес и рейтинг каждого заведения в консоль.




import os

import sys

import certifi
os.environ['REQUESTS_CA_BUNDLE'] = os.path.join(os.path.dirname(sys.argv[0]), certifi.where())

import requests
import json

# Ваши учетные данные API
client_id = "P54V3O3BOIFXR4FUTLUD05TJFL0ZIU32USFQQCVRKLUWMCCA"
client_secret = "ZMX3A3I4EJWMZVZNQEEMOL0TW3KRFVJ3WGKT4YKWBWCTACEL"

# Конечная точка API
endpoint = "https://api.foursquare.com/v3/places/search"

# Определение параметров для запроса API
categoryes = input("Введите категорию поиска: ")
params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "near": 'Istambul',
    "query": categoryes
  
}

headers = {
    "Accept": "application/json",
    "Authorization": "fsq3aR6nnmyZrvKv6W2S8mQ1aM23P32smdHXMNVya3Lq6cs="
}

# Отправка запроса API и получение ответа
response = requests.get(endpoint, params=params,headers=headers)

# Проверка успешности запроса API
if response.status_code == 200:
    print("Успешный запрос API!")
    data = json.loads(response.text)
    venues = data["results"]
    for venue in venues:
        name = venue['name']
        formatted_address = venue['location']['formatted_address'] if 'formatted_address' in venue['location'] else 'Адрес не указан'
        rate = venue["unreadCount"] if "unreadCount" in venue else 'Рейтинг не указан'
        print(f'Название: {name}, Адрес: {formatted_address}, Рейтинг: {rate}', "\n")
      
else:
    print("Запрос API завершился неудачей с кодом состояния:", response.status_code)
    print(response.text)
