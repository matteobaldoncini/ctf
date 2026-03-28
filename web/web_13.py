import requests
from bs4 import BeautifulSoup

URL =  "http://web-13.challs.olicyber.it/" 

if __name__ == "__main__":
    page = requests.get(URL)
    page = page.text
    soup = BeautifulSoup(page, 'html.parser')
    flag = soup.find_all('span')
    flag = [s.contents[0] for s in flag]
    flag = "flag{" + "".join(flag) + "}"
    print(flag)
