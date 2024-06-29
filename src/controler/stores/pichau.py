from utils import get_response

def main():
    response = get_response('https://www.pichau.com.br/search?q=mouse')

    print(response)