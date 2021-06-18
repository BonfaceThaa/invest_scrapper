import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# Business daily news home page URL
BASE_URL = 'https://www.businessdailyafrica.com/bd'

# List to hold articles (titles and links) scrapped in a day
markets_articles = []

# Fetch the capital markets page
url = urljoin(BASE_URL, '/markets')
r = requests.get(url)
html_soup = BeautifulSoup(r.text, 'html.parser')

# Loop through all page-box sections
for article_section in html_soup.find_all('div', class_='page-box'):
    article_section_header = article_section.find('header')

    # Filter capital markets page-box div
    if article_section_header.text == 'Capital Markets':
        articles = article_section.find_all('article', class_='article article-list-regular')

        # Get the article title and link from the article tag
        for article in articles:
            article_tag = article.find('a')
            article_title = article_tag.get('title')
            article_link = article_tag.get('href')

            # Add the retrieved article details to market list as a dict
            markets_articles.append({
                "title": article_title,
                "link": urljoin(BASE_URL, article_link)
            })

for markets_article in markets_articles:
    print(markets_article)
