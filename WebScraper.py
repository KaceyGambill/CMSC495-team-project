from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen
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

# This block scrapes links for resumes
def links(url: str):
    text_dict = {
            "site": [
                ]
            }
    r = requests.get(url)
    linksoup = BeautifulSoup(r.content, 'html.parser')
##    print(linksoup.a.prettify())
    for link_index, link in enumerate(linksoup.find_all('a')):
        # set limit at 100 so it doesn't take forever
        if link_index == 100:
            break
        link_href = link.get('href')
        if str(link_href).startswith('http'):
#            print(link_href)
            try:
                text_dict_info = text(link_href)
                text_dict['site'].append(text_dict_info)
            except:
                print('did not scrape')
    return text_dict['site']

# This block scrapes the text from a resume article
def text(url: str) -> dict:
    r = requests.get(url)
    textsoup = BeautifulSoup(r.content, 'html.parser')
    title_text = textsoup.find_all("title")
    text_body = textsoup.find_all('p')


#    print(textsoup.title.prettify())
    try:
        text_dict_info = {
                "url": url,
                "title": title_text,
                "p": text_body
                }
#        print(f'url: {url}')
#        print(f'title: {title_text}')
#        print(text.get_text())
    except:
        print('no info found')
    return text_dict_info


if __name__ == "__main__":
##    main()
##    text("https://arc.dev/resume")
    links("https://www.freecodecamp.org/news/tag/resume")
##    text("https://www.freecodecamp.org/news/rtc-connecting-discord-how-to-fix-the-server-error/")
