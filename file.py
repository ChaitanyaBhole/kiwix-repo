import requests
from bs4 import BeautifulSoup
import urllib.request

url = "https://wiki.kiwix.org/wiki/Content_in_all_languages"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

torrent_links = []
for link in soup.find_all('a'):
    href = link.get('href')
    if isinstance(href, str) and href.endswith('.torrent'):
        torrent_links.append(href)

for link in torrent_links:
    filename = link.split('/')[-1]
    urllib.request.urlretrieve(link, filename)
