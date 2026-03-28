import requests
import re
from bs4 import BeautifulSoup, Comment

BASE_URL =  "http://web-16.challs.olicyber.it/" 

if __name__ == "__main__":  
    urls = [BASE_URL]
    visited = []
    for url in urls:
        if url not in visited:
            visited.append(url)
            page = requests.get(url).text
            soup = BeautifulSoup(page, 'html.parser')
            match = re.compile('flag{.*}').search(page)
            if match:
                print(f"{url} -> SI -> {match.group()}")
                exit(1)
            
            print(f"{url} -> NO")
            resources = soup.find_all('a')
            for res in resources:
                path = res['href']
                urls.append(BASE_URL + path)
