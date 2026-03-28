import requests
import re
from bs4 import BeautifulSoup, Comment

URL =  "http://web-14.challs.olicyber.it/" 

if __name__ == "__main__":
    page = requests.get(URL)
    page = page.text
    soup = BeautifulSoup(page, 'html.parser')
    flag = soup.find_all(string= lambda t: isinstance(t, Comment))
    for s in flag:
        if (re.compile('flag{.*}')).search(s):
            print(s)
