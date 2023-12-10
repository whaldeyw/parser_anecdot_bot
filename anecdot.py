import requests
from  bs4 import BeautifulSoup
from  time import sleep

headers ={
    "Accept": "*/*",
    "User-Agent":  "UserAgent().chrome"
}
url = 'https://anekdotbar.ru/top-100-2.html'
r = requests.get(url, headers=headers)
src = r.text

sleep(2)
soup = BeautifulSoup(src, 'lxml')

text = soup.find_all(class_="tecst")
for i in text:
    print(i.text)