import requests
from bs4 import BeautifulSoup as bs

def get_response(url: str) -> bs:
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

    try:
        response = requests.get(url=url, headers=header)
    
    except requests.exceptions.URLRequired:
        print(f"Error to connect url= '{url}'\nInsert the correct url")

    except requests.exceptions.ConnectTimeout:
        return get_response(url)

    else:
        site = bs(response.content, 'html.parser')

        return site