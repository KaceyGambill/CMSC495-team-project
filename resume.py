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
    print("\n Useful Resume tip resources: \n")
    url2 = "https://www.freecodecamp.org/news/tag/resume/"
    r = requests.get(url2)
    linksoup = BeautifulSoup(r.content, 'html.parser')
    print(linksoup.a.prettify())
    for link in linksoup.find_all('a'):
        print(link.get('href'))



def main():
    text()
    links()


if __name__ == "__main__":
    main()
    re
