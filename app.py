from functions.scraper import Scraper


# url = 'https://medex.com.bd/companies/106/incepta-pharmaceuticals-ltd/brands'
# details_url = 'https://medex.com.bd/brands/32000/abdolax-5mg'

# names = Scraper.scrap_data(url=url)
# imgs = Scraper.scrap_data(url=details_url)
# contents = Scraper.scrap_data(url=details_url,value='ac-body')
# prices = Scraper.scrap_data(url=details_url,value='ac-body')

# print(contents)

url = 'https://osudpotro.com/manufacturer/incepta-pharmaceuticals-ltd'
details_url = 'https://medex.com.bd/brands/32000/abdolax-5mg'

names = Scraper.scrap_data(el="span", url=url, value='productTitle')
imgs = Scraper.scrap_data(url=details_url, el="img", attr='src')
contents = Scraper.scrap_data(url=details_url, value='ac-body')
prices = Scraper.scrap_data(url=details_url, value='ac-body')

print(imgs)
