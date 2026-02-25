from bs4 import BeautifulSoup
import requests
import freecurrencyapi
def currency_list():
    table = []
    url = "https://freecurrencyapi.com/docs/currency-list"
    response = requests.get(url)
    if response.ok == True:
        soup = BeautifulSoup(response.text, "html.parser")
        rows = soup.find_all("tr")
        for row in rows:
            row_txt = row.get_text(separator=",", strip=True)
            row_txt = row_txt.split(",")
            table.append({row_txt[0]:row_txt[1]})
        return(table)
    return "Response Error"

def fetcher(api= "fca_live_WVjhIif1YmoZHhWMWYKsWpObFgFSld8gH4bF9xr9",base_currency="USD", currencies=["EUR","CAD","RUB","TRY"]):
    client = freecurrencyapi.Client(api)
    result = client.latest(base_currency=base_currency, currencies=currencies)
    return result