import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from contact_extractors.cognism_urls import extract_cognism_urls
from contact_extractors.name_lastname import extract_name  # Import the function

def scrape_urls(driver, segment):
    """Extracts all profile URLs and names from the page using scrolling for virtualized lists."""
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

        seen_contacts = {}  # Store names and URLs
        previous_count = 0

        while True:
            # Extract new URLs
            new_urls = extract_cognism_urls(driver)

            for url in new_urls:
                if url not in seen_contacts:
                    # Extract name for the corresponding URL
                    name_data = extract_name(driver)  # Extract name before clicking away
                    
                    # Store extracted data
                    seen_contacts[url] = {
                        "url": url,
                        "segment": segment,
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "Name": name_data["Name"],
                        "Last_Name": name_data["Last_Name"]
                    }

                    # ✅ Debugging print: See extracted contact in real-time
                    print(f"🔍 Extracted Contact: {seen_contacts[url]}")

            # Scroll down
            driver.execute_script("arguments[0].scrollBy(0, 300);", scroll_container)
            time.sleep(1.5)  # Allow new elements to load

            # Stop if no new contacts are added
            if len(seen_contacts) == previous_count:
                break

            previous_count = len(seen_contacts)

        print(f"✅ Total Contacts Extracted: {len(seen_contacts)}")
        return {"Contacts": list(seen_contacts.values())}

    except Exception as e:
        print(f"⚠️ Error during scrolling & scraping: {e}")
        return None
