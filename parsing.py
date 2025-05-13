from bs4 import BeautifulSoup
import requests

url = 'https://24.kg'
response = requests.get(url=url)
# print(response)

soup = BeautifulSoup(response.text, 'lxml')
all_news = soup.find_all('div', class_='title')
# print(all_news)

count_news = 0
for news in all_news:
    count_news += 1
    print(count_news,news.text)