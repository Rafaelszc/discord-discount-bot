from bs4 import BeautifulSoup as bs
from utils import get_response

def main():
    response = get_response('https://www.terabyteshop.com.br/busca?str=mouse')

    print(response)