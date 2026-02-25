import time
from rich.live import Live
from rich.table import Table
from api_fetcher import fetcher

def api_fetcher_display():
    """
    Live display of exchange rates using Rich.
    Fetches data from API every 5 seconds and updates table.
    Prices are rounded to 2 decimals for readability.
    """
    with Live(refresh_per_second=2) as live:
        while True:
            table = Table(title="💱 Exchange Rate Tracker (API)")
            table.add_column("Currency", justify="center")
            table.add_column("Price (USD)", justify="center")

            currencies = fetcher()
            data = currencies["data"]

            for currency, value in data.items():
                table.add_row(currency, f"{value:,.2f}")

            live.update(table)

            time.sleep(5)

api_fetcher_display()
