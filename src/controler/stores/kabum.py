import requests
from bs4 import BeautifulSoup as bs

link = 'https://www.kabum.com.br/busca/mouse'
header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}

request = requests.get(link, headers=header)

site = bs(request.text, 'html.parser')

product_article = site.find('article', attrs={'class': 'sc-9d1f1537-7 hxuzLm productCard'})

product_info = product_article.find('div', attrs={'class': 'sc-9d1f1537-11 hsSiHU'})