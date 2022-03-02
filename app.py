from functions.scraper import Scraper

url = 'https://medex.com.bd/companies/106/incepta-pharmaceuticals-ltd/brands'
details_url = 'https://medex.com.bd/brands/32000/abdolax-5mg'

names = Scraper.scrap_data(url=url)
imgs = Scraper.scrap_data(url=details_url)
contents = Scraper.scrap_data(url=details_url,value='ac-body')

print(contents)
