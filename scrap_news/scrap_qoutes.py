import requests
import dataset
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

db = dataset.connect('sqlite:///quotes.db')

authors_seen = set()

BASE_URL = 'http://quotes.toscrape.com/'


def clean_url(url):
    url = urljoin(BASE_URL, url)
    path = urlparse(url).path
    return path.split('/')[2]


def scrape_quotes(html_soup):
    for quote in html_soup.select('div.quote'):
        quote_text = quote.find(class_='text').get_text(strip=True)
        quote_author_url = clean_url(quote.find(class_='author').find_next_sibling('a').get('href'))
        quote_tag_urls = [clean_url(a.get('href')) for a in quote.find_all('a', class_='tag')]
        authors_seen.add(quote_author_url)
        quote_id = db['quotes'].insert({'text': quote_text, 'author': quote_author_url})
        db['quote_tags'].insert_many(
            [{'quote_id': quote_id, 'tag_id': tag} for tag in quote_tag_urls]
        )


def scrape_author(html_soup, author_id):
    author_name = html_soup.find(class_='author-title').get_text(strip=True)
    author_born_date = html_soup.find(class_='author-born-date').get_text(strip=True)
    author_born_loc = html_soup.find(class_='author-born-location').get_text(strip=True)
    author_desc = html_soup.find(class_='author-description').get_text(strip=True)
    db['authors'].insert({
        'author_id': author_id,
        'name': author_name,
        'born_date': author_born_date,
        'born_location': author_born_loc,
        'description': author_desc
    })

url = BASE_URL

while True:
    print('Now scrapping page:', url)
    r = requests.get(url)
    html_soup = BeautifulSoup(r.text, 'html.parser')
    scrape_quotes(html_soup)
    next_a = html_soup.select('li.next > a')

    if not next_a or not next_a[0].get('href'):
        break

    url = urljoin(url, next_a[0].get('href'))

for author_id in authors_seen:
    url = urljoin(BASE_URL, '/author/' + author_id)
    print('Now scrapping author:', url)
    r = requests.get(url)
    html_soup = BeautifulSoup(r.text, 'html.parser')
    scrape_author(html_soup, author_id)
