import requests
from bs4 import BeautifulSoup

# URL сторінки для парсингу
url = 'https://www.bbc.com/news'

# Завантажуємо HTML-сторінку
response = requests.get(url)

# Перевіряємо, чи вдалося отримати сторінку
if response.status_code == 200:
    # Парсимо HTML-код сторінки
    soup = BeautifulSoup(response.text, 'html.parser')

    # Збираємо всі заголовки новин (пошук елементів h2 або h3)
    headlines = soup.find_all(['h2', 'h3'])

    # Виводимо заголовки
    for idx, headline in enumerate(headlines, start=1):
        text = headline.get_text(strip=True)
        if text:  # Перевіряємо, чи є текст у заголовку
            print(f'{idx}. {text}')
else:
    print(f'Не вдалося завантажити сторінку. Статус код: {response.status_code}')
