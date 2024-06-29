import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_response(url: str) -> requests.get:
    google_options = Options()
    google_options.add_argument("--headless")
    driver = webdriver.Chrome(options=google_options)

    url = url
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}

    driver.get(url)
    driver.execute_script("return navigator.userAgent")

    page_source = driver.page_source

    response = requests.get(url=url, headers=header)

    return response