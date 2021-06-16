import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

BASE_URL = 'https://www.businessdailyafrica.com/bd'
markets_articles = []

url = 'https://www.businessdailyafrica.com/bd/markets'
r = requests.get(url)
html_soup = BeautifulSoup(r.text, 'html.parser')

for article_section in html_soup.find_all('div', class_='page-box'):
    article_section_header = article_section.find('header')
    if article_section_header.text == 'Capital Markets':
        articles = article_section.find_all('article', class_='article article-list-regular')
        for article in articles:
            article_tag = article.find('a')
            article_title = article_tag.get('title')
            article_link = article_tag.get('href')
            markets_articles.append({
                "title": article_title,
                "link": urljoin(BASE_URL, article_link)
            })

for markets_article in markets_articles:
    print(markets_article)
