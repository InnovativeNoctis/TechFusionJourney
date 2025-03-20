from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def IMDB_Check(box):
    print("\nConnecting to IMDb...\n")

    options = Options()
    options.add_argument("--headless=new")  
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.139 Safari/537.36")

    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://www.imdb.com/chart/top/")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "ul.ipc-metadata-list li"))
        )

        movie_elements = driver.find_elements(By.CSS_SELECTOR, "ul.ipc-metadata-list li")

        if not movie_elements:
            print("Error: Could not find movie list. IMDb structure may have changed.")
            return

        print("\nTop Movies:\n")
        for i in range(min(box, len(movie_elements))):
            try:
                movie = movie_elements[i]
                title_element = movie.find_element(By.CSS_SELECTOR, "h3")
                rating_element = movie.find_element(By.CSS_SELECTOR, "span.ipc-rating-star")
                
                title = title_element.text.strip() if title_element else "Unknown Title"
                rating = rating_element.text.strip() if rating_element else "N/A"

                print(f"{title} | Rating: {rating}")
            except Exception:
                continue
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        if driver:
            try:
                driver.quit()
            except Exception as e:
                print("Exception during driver.quit():", e)

if __name__ == "__main__":
    while True:
        try:
            box = int(input("\nEnter how many movies you are looking for (1-250) (exit(0)): ").strip())
            if 1 <= box <= 250:
                IMDB_Check(box)
            elif box == 0:
                break
            else:
                print("Invalid number. Choose between: 1-250")
        except ValueError:
            print("Please enter a valid number.")