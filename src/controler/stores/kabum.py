from utils import get_response
from bs4 import BeautifulSoup as bs

class Kabum:
    def __init__(self, url: str) -> None:
        self.response = get_response(url)

        self.site = bs(self.response.text, 'html.parser')

    def get_product_url(self) -> list:
        product_url_partition = self.site.find_all('a', attrs={'class': 'sc-9d1f1537-10 kueyFw productLink'}, href=True)

        url_list = []
        for a in product_url_partition:
            url_list.append(f"https://www.kabum.com.br{a.get('href')}")

        return url_list

    def get_price(self) -> float:
        price_partition = self.site.find('h4', attrs={'class': 'sc-5492faee-2 ipHrwP finalPrice'}).text

        symbol, price = price_partition.split()

        price = float(price.replace('.', '').replace(',', '.'))

        return price
    
    def get_name(self) -> str:
        name_partition = self.site.find('h1', attrs={'class': 'sc-58b2114e-6 brTtKt'})

        name = name_partition.text

        return name