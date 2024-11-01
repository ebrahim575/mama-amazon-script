from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time

# Configuration
URLS = [
    "https://www.amazon.com/dp/B0DDKWZS9P",
    # Add more URLs here as needed
]
VIEW_TIME_SECONDS = 5  # N seconds to view each page
WAIT_TIME_SECONDS = 10  # M seconds to wait between cycles

def setup_headless_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=chrome_options)

def main():
    driver = setup_headless_browser()
    
    try:
        while True:  # Run indefinitely
            for url in URLS:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{current_time}] Accessing {url}")
                
                # Load the page
                driver.get(url)
                
                # Wait for N seconds while viewing the page
                print(f"[{current_time}] Viewing page for {VIEW_TIME_SECONDS} seconds")
                time.sleep(VIEW_TIME_SECONDS)
                
                # Wait for M seconds before next poll
                print(f"[{current_time}] Waiting {WAIT_TIME_SECONDS} seconds before next poll")
                time.sleep(WAIT_TIME_SECONDS)
                
    except KeyboardInterrupt:
        print("\nStopping the browser...")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()