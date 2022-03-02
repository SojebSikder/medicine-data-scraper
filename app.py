from functions.scraper import Scraper

url = 'https://medex.com.bd/companies/106/incepta-pharmaceuticals-ltd/brands'
product_name = Scraper.scrap_data(url=url)
print(product_name)
