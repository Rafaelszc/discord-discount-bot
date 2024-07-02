from utils import get_response
import re
from bs4 import BeautifulSoup as bs

class Kabum:
    response = get_response(f'https://www.kabum.com.br/produto/112948/mouse-gamer-logitech-g203-lightsync-rgb-efeito-de-ondas-de-cores-6-botoes-programaveis-e-ate-8-000-dpi-preto-910-005793')

    site = bs(response.text, 'html.parser')

    @classmethod
    def get_price(cls):
        price_partition = cls.site.find('h4', attrs={'class': 'sc-5492faee-2 ipHrwP finalPrice'}).text

        symbol, price = price_partition.split()

        price = float(price.replace('.', '').replace(',', '.'))

        return price
    
    @classmethod
    def get_name(cls):
        name_partition = cls.site.find('h1', attrs={'class': 'sc-58b2114e-6 brTtKt'})

        name = name_partition.text

        return name
    
    @classmethod
    def is_promotion(cls):
        promotion_partition = cls.site.find('span', attrs={'class': 'sc-5492faee-1 ibyzkU oldPrice'})

        if promotion_partition != []:
            return True
        
        return False