import requests
from bs4 import BeautifulSoup
 # Making a GET request
result = requests.get('https://www.bhinneka.com/jual?cari=iphone&order=')
# print(result.status_code)
# print(result.headers)
src = result.content
# print(src)
soup = BeautifulSoup(src, 'html.parser')
# print(type(soup))
#finding by id
s = soup.find('div',id='products_grid')

#getting the leftbar
#leftbar = s.find('div', class_='o_wsale_product_grid_wrapper position-relative h-100')
#all the a under the above ul
# content = leftbar.find_all('a')
# print(content)

products = soup.find_all("div", "o_wsale_product_grid_wrapper position-relative h-100")
# print(products)

product_name = []

for product in products:
    nama = product.find('a', 'text-primary text-decoration-none').get_text()
    product_name.append(nama)
print(product_name)