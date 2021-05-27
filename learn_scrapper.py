import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/w/index.php' + \
      '?title=List_of_Game_of_Thrones_episodes&oldid=802553687'

r = requests.get(url)
html_contents = r.text

html_soup = BeautifulSoup(html_contents, 'html.parser')
cites = html_soup.find_all('cite', class_='citation', limit=5)
for citation in cites:
    print(citation.get_text())
    link = citation.find('a')
    print(link.get('href'))



