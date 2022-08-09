from bs4 import BeautifulSoup
import requests
from urllib3.util import url

def main():
    url = "https://www.linkedin.com/jobs/search/?geoId=107024810&keywords=software%20engineer&location=Everett%2C%20Washington%2C%20United%20States"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    for link in soup.find_all('a'):
        print(link.get('href'))

def scrape_url(url: str) -> dict:
    """scrape url, return urls with 'http'
    Args:
      url: string of url to scrape"""

    dict_of_results = {
			"scrape_site": url,
            "links": []
            }
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    for link in soup.find_all('a'):
        link_href = link.get('href')
        if str(link_href).startswith('http'):
            dict_of_results['links'].append(link_href)
    return dict_of_results

def get_links(url: str) -> dict:
    text_dict = {
            "site": [
                ]
            }
    if url is None:
        url = 'https://www.freecodecamp.org/news/tag/resume/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
    reqs = requests.get(url, headers=headers)
    soup = BeautifulSoup(reqs.content, 'html.parser')
    links = soup.findAll('h2', {'class': 'post-card-title'})


    for p in links:
        try:
            a = p.find('a')['href']
        except:
            continue
        else:
            fqdn = "https://freecodecamp.org" + a
            text_dict_info = text(fqdn)
            text_dict['site'].append(text_dict_info)
    return text_dict['site']

# This block scrapes the text
def text(url: str) -> dict:
    r = requests.get(url)
    textsoup = BeautifulSoup(r.content, 'html.parser')
    title_text = textsoup.find_all("title")
    text_body = textsoup.find_all('p')

    try:
        text_dict_info = {
                "url": url,
                "title": title_text,
                "p": text_body
                }
        new_string = ""
        for i in text_body:
            for j in i:
                for k in j:
                    new_string += str(k)

        text_dict_info["p"] = new_string

    except:
        print('no info found')
    return text_dict_info


if __name__ == "__main__":
    print(get_links("https://www.freecodecamp.org/news/tag/resume"))


