from bs4 import BeautifulSoup
import requests
import time
from random import randint
from scrapingbee import ScrapingBeeClient

url = 'https://www.freecodecamp.org/news/tag/resume/'
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
reqs = requests.get(url, headers=headers)
soup = BeautifulSoup(reqs.content, 'html.parser')
links = soup.findAll('h2', {'class': 'post-card-title'})

links_list = []
text_list = []

for p in links:
    try:
        a = p.find('a')['href']
    except:
        continue
    else:
        links_list.append(a)


client = ScrapingBeeClient(api_key='591KSTL38O4WVUN3S2BQMAPQRIGA1P9J62MMIZA2RQ4ES63JUX02MG4FS9WMTUMUCZCJ3GR82F8W6139')
for thing in links_list:
    new_url = url + thing
    print(new_url)
    reqs = client.get(new_url)
    soup = BeautifulSoup(reqs.content, "html.parser")
    text_body = soup.findAll('p')
    text_list.append(text_body)
    time.sleep(randint(1, 5))

for thing in text_list:
    print(thing)