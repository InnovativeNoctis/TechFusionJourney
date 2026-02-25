import requests
from bs4 import BeautifulSoup

def scrape_data():
    url = "https://www.xe.com/currencyconverter/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        html = response.text
    else:
        return "Fetching failed!"
    
    soup = BeautifulSoup(html, "html.parser")



    
    