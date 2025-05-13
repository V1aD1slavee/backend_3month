from bs4 import BeautifulSoup
import requests

for page in range(1, 11):
    url = f'https://24.kg/page_{page}'
    response = requests.get(url=url)
    # print(response)

    soup = BeautifulSoup(response.text, 'lxml')
    all_news = soup.find_all('div', class_='title')
    # print(all_news)

    count_news = 0
    for news in all_news:
        count_news += 1
        print(count_news,news.text)