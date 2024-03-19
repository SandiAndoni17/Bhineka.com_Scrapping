import requests
from bs4 import BeautifulSoup

for halaman in range(1,3):
    #ubah nomor halaman dalam url
    print(f'Halaman{halaman}')
    url =f'https://www.bhinneka.com/jual?page={halaman}&cari=iphone&order='
    #https: // www.bhinneka.com / jual?page = 5 & cari = iphone & order =
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

#find all elemen with 'a' tag that have class 'text primary text dec none'
    links = soup.find_all('a', class_= 'text-primary text-decoration-none')

    for link in links:
        href = link.get('href')
        print(href)