import requests
from bs4 import BeautifulSoup

url =('https://www.bhinneka.com/jual?cari=iphone&order=')
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

#find all elemen with 'a' tag that have class 'text primary text dec none'
links = soup.find_all('a', class_= 'text-primary text-decoration-none')

for link in links:
    href = link.get('href')
    print(href)