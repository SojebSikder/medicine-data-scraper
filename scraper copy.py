import requests
from bs4 import BeautifulSoup as soup

header = {'Origin': 'https://www.1mg.com',
          'Referer': 'https://www.1mg.com/categories/exclusive/immunity-boosters/vitamin-c-734',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
          }

url = 'https://www.1mg.com/categories/exclusive/immunity-boosters/vitamin-c-734'
url = 'https://www.1mg.com/categories/exclusive/immunity-boosters/vitamin-c-734'
html = requests.get(url=url, headers=header)

print(html.status_code)

# bsobj = soup(html.content, 'html.parser')
bsobj = soup(html.content, 'lxml')

product_name = []
product_description = []
product_price = []

for name in bsobj.findAll('div', {'itemprop': 'name'}):
    product_name.append(name.text.strip())
print(product_name)
