from bs4 import BeautifulSoup
import requests


def main():
    url = "https://www.dice.com/jobs?q=software%20engineering&countryCode=US&radius=30&radiusUnit=mi&page=1&pageSize=20&language=en&eid=S2Q_"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    for link in soup.find_all('a'):
        print(link.get('href'))


if __name__ == "__main__":
    main()
