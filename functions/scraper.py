import requests
from bs4 import BeautifulSoup as soup


class Scraper:

    # Scrap data from the website
    def scrap_data(url, el="div", attr="class", value="col-xs-12 data-row-top"):
        # url = 'https://medex.com.bd/companies/106/incepta-pharmaceuticals-ltd/brands'
        html = requests.get(url=url)

        if html.status_code == 200:
            bsobj = soup(html.content, 'lxml')

            product_name = []

            for name in bsobj.findAll(el, {attr: value}):
                product_name.append(name.text.strip())
            return product_name
        else:
            print(html.status_code)
            print('Website is not available')
