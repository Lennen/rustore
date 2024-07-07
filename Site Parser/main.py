import requests
from bs4 import BeautifulSoup

# Замените URL на адрес сайта, который вы хотите парсить
url = 'https://www.rustore.ru/help/sdk/payments/'

# Получаем данные с сайта
response = requests.get(url)

# Проверяем, что запрос был успешным
if response.status_code == 200:
    # Анализируем HTML страницу
    soup = BeautifulSoup(response.content, 'html.parser')
    # Находим первый тег title и выводим его содержимое
    print(soup.title.string)
    # Находим все теги h1, h2, h3, h4, h5, h6 и выводим их содержимое
    for header in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        print(header.text)
    #print(soup)

else:
    print('Запрос не удался. Код статуса:', response.status_code)