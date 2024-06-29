from utils import get_response
import re

link = 'https://www.kabum.com.br'

def main():
    response = get_response(f'https://www.kabum.com.br/produto/94555/mouse-gamer-redragon-cobra-chroma-rgb-10000dpi-7-botoes-preto-m711-v2')

    site = response.content
    price_compile = re.compile(r'<h4 class="sc-5492faee-2 ipHrwP finalPrice">(.*?)</h4>', re.DOTALL)

    price = re.findall(price_compile, str(site))[0]