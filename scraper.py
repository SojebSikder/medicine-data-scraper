import requests
from bs4 import BeautifulSoup as soup

url = 'https://medex.com.bd/companies/106/incepta-pharmaceuticals-ltd/brands'

html = requests.get(url=url)


if html.status_code == 200:
    bsobj = soup(html.content, 'lxml')

    product_name = []
    product_description = []
    product_price = []

    print("wait...")

    for name in bsobj.findAll('div', {'class': 'col-xs-12 data-row-top'}):
        product_name.append(name.text.strip())
    print(product_name)
    print(product_name.__len__())
else:
    print(html.status_code)
    print('Website is not available')
