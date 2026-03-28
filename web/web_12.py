import requests
from bs4 import BeautifulSoup

URL = "http://web-12.challs.olicyber.it/"

def get_page():
    response = requests.get(URL)
    return response.text

def get_p(html):
    soup = BeautifulSoup(html, 'html.parser')
    soup = soup.find_all('p')
    return soup

if __name__ == "__main__":
    html = get_page()
    soup = get_p(html)
    print(soup)
