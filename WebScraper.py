from bs4 import BeautifulSoup
import requests


def main():
    url = "https://www.linkedin.com/jobs/search/?geoId=107024810&keywords=software%20engineer&location=Everett%2C%20Washington%2C%20United%20States"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    for link in soup.find_all('a'):
        print(link.get('href'))


if __name__ == "__main__":
    main()
