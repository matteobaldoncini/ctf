import requests
import re
from bs4 import BeautifulSoup, Comment

BASE_URL =  "http://web-15.challs.olicyber.it/" 

if __name__ == "__main__":
    page = requests.get(BASE_URL)
    page = page.text
    soup = BeautifulSoup(page, 'html.parser')
    resources = soup.find_all(
            lambda t: t.name == 'link' or t.name == 'script'
            )
    files = []
    for r in resources:
        if r.name == 'script':
            path = r['src']
        elif r.name == 'link':
            path = r['href']
        files = requests.get(BASE_URL + path)
    
    for file in files:
        file = file.decode()
        match = re.compile('flag{.*}').search(file)
        if match:
            print(match.group())
        
