from utils import get_response
from bs4 import BeautifulSoup as bs

class Kabum:
    def __init__(self, url: str) -> None:
        self.site = get_response(url)
        self.store_name = "kabum"

    async def get_product_url(self) -> list:
        product_url_partition = self.site.find_all('a', attrs={'class': 'sc-9d1f1537-10 kueyFw productLink'}, href=True)

        url_list = []
        for a_href in product_url_partition:
            url_list.append(f"https://www.kabum.com.br{a_href.get('href')}")

        return url_list

    async def get_price(self) -> float:
        price_partition = self.site.find('h4', attrs={'class': 'sc-5492faee-2 ipHrwP finalPrice'}).text

        symbol, price = price_partition.split()

        price = float(price.replace('.', '').replace(',', '.'))

        return price
    
    async def get_name(self) -> str:
        name_partition = self.site.find('h1', attrs={'class': 'sc-58b2114e-6 brTtKt'})

        name = name_partition.text

        return name
    
    async def get_image_url(self) -> str:
        img_figure = self.site.find('figure', attrs={'class': 'iiz'})
        img = img_figure.find('img', src=True)

        return img['src']