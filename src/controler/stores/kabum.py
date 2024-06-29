from utils import get_response
import re

link = 'https://www.kabum.com.br'

class Kabum:
    response = get_response(f'https://www.kabum.com.br/produto/102653/headset-gamer-sem-fio-astro-a50-base-station-gen-4-com-audio-dolby-atmos-para-xbox-series-xbox-one-pc-mac-preto-939-001681?gad_source=1&gclid=EAIaIQobChMI_8qvvtWBhwMV-VhIAB2yzAivEAQYASABEgLa3PD_BwE')

    site = response.content

    @classmethod
    def price(cls):
        price_compile = re.compile(r'<h4 class="sc-5492faee-2 ipHrwP finalPrice">(.*?)</h4>', re.DOTALL)

        price_partition = re.findall(price_compile, str(cls.site))[0]
        price_partition = str(price_partition).replace('\\xc2\\xa', ' ')

        symbol, price = price_partition.split()

        price = float(price.replace(',', '.'))
        
        return price