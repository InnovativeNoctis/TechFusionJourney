import re
import requests
from bs4 import BeautifulSoup

def Countries(amount):
    url = "https://www.scrapethissite.com/pages/simple/"
    print("Connecting...\n")
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve data. Please check the website URL.")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")

    countries_name = soup.find_all("h3", class_="country-name")
    countries_capital = soup.find_all("span", class_="country-capital")
    countries_population = soup.find_all("span", class_="country-population")
    countries_area = soup.find_all("span", class_="country-area")

    total_countries = len(countries_name)
    
    if amount > total_countries:
        print(f"Only {total_countries} countries are available. Showing all of them.")
        amount = total_countries

    for index in range(amount):
        country = re.sub(r"\s+", " ", countries_name[index].text).strip()
        capital = re.sub(r"\s+", " ", countries_capital[index].text).strip()
        population = re.sub(r"\s+", " ", countries_population[index].text).strip()
        area = re.sub(r"\s+", " ", countries_area[index].text).strip()

        print(f"""
{index+1}.
Country: {country}
Capital: {capital}
Population: {population}
Area(km²): {area}
        """)

if __name__ == "__main__":
    while True:
        try:
            amount = int(input("Enter how many countries you want to see: "))
            if amount >= 1:
                Countries(amount)
                break
            else:
                print("You have to enter a number greater than or equal to 1.")
        except ValueError:
            print("Please enter a valid number.")
