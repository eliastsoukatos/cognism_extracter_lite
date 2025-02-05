import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from contact_extractors.cognism_urls import extract_cognism_urls  # Import the function

def scrape_urls(driver, segment):
    """Extracts all profile URLs from the page using scrolling for virtualized lists."""
    try:
        # Wait for the page to fully load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # Wait for the table to appear
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, '/search/prospects/persons/') and contains(@class, 't-text-primary-600')]"))
        )
        
        # Find the scrollable container
        scroll_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cdk-virtual-scroll-viewport"))
        )

        seen_urls = set()
        previous_count = 0

        while True:
            # Extract new URLs
            new_urls = extract_cognism_urls(driver)
            seen_urls.update(new_urls)

            # Scroll down
            driver.execute_script("arguments[0].scrollBy(0, 300);", scroll_container)
            time.sleep(1.5)  # Allow new elements to load

            # Stop if no new URLs are added
            if len(seen_urls) == previous_count:
                break

            previous_count = len(seen_urls)

        # Create structured output
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        urls_data = [{"url": url, "segment": segment, "timestamp": timestamp} for url in seen_urls]
        
        print(f"✅ Total URLs Extracted: {len(seen_urls)}")
        return {"URLs": urls_data}

    except Exception as e:
        print(f"⚠️ Error during scrolling & scraping: {e}")
        return None
