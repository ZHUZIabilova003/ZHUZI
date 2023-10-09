import requests

# URL, на который будет отправлен запрос
url = 'https://example.com/api/endpoint'

# Данные, которые вы хотите отправить
data = {'key1': 'value1', 'key2': 'value2'}

# Отправка POST-запроса
response = requests.post(url, data=data)

# Проверка статуса ответа
if response.status_code == 200:
    print('Запрос успешно выполнен')
else:
    print('Произошла ошибка:', response.status_code)
