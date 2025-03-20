import requests
from bs4 import BeautifulSoup

def quote_taker(headers, choice):
    print("\nConnecting...\n")
    url = f"http://quotes.toscrape.com/tag/{choice}/"

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Connection failed! Error: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("span", class_="text")

    if quotes:
        for quote in quotes:
            print(quote.text, "\n")
    else:
        print(f"No quotes found for the tag: {choice}")

tags = ["love", "inspirational", "life", "humor", "books", "reading",
        "friendship", "friends", "truth", "simile"]

while True:
    print("\nTop ten tags:")
    print(", ".join(tags))  

    choice = input("\nEnter a tag (or type 'exit' to quit): ").strip().lower()

    if choice == "exit":
        print("Goodbye!")
        break

    if choice in tags:
        quote_taker({"User-Agent": "Mozilla/5.0"}, choice)
        q = input("\nDo you want to check another tag? (yes/no): ").strip().lower()
        if q != "yes":
            print("Goodbye!")
            break
    else:
        print("Invalid tag! Please enter a valid tag from the list.")