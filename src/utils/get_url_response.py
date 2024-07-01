import requests

def get_response(url: str) -> requests.get:
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}

    response = requests.get(url=url, headers=header)

    return response