import re
from urllib.request import urlopen

from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen
from urllib3.util import url


# This block scrapes the text from a resume article
def text():
    print('This should print the paragraph \n')
    url1 = "https://arc.dev/resume"
    r = requests.get(url1)
    textsoup = BeautifulSoup(r.content, 'html.parser')
    title_text = textsoup.find_all("title")
    print(textsoup.title.prettify())
    for text in textsoup.find_all('p'):
        print(text.get_text())


# This block scrapes links for resumes
def links():
    print("\n here on out should be links\n")
    url2 = "https://www.freecodecamp.org/news/tag/resume/"
    r = requests.get(url2)
    linksoup = BeautifulSoup(r.content, 'html.parser')
    print(linksoup.a.prettify())
    # print(linksoup.find_all('a'))
    print("Here are other links and resources for building a resume: \n")
    for link in linksoup.find_all('a'):
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

def main():
    text()
    links()


if __name__ == "__main__":
    main()
    #scrape_url( "https://www.dice.com/jobs?q=software%20engineering&countryCode=US&radius=30&radiusUnit=mi&page=1&pageSize=20&language=en&eid=S2Q_")
