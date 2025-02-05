from selenium.webdriver.common.by import By

def extract_cognism_urls(driver):
    """Extracts all unique profile URLs from the page."""
    seen_urls = set()
    
    try:
        # Find all profile links in the table
        url_elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/search/prospects/persons/') and contains(@class, 't-text-primary-600')]")

        for elem in url_elements:
            href = elem.get_attribute("href")
            if href and "/search/prospects/persons/" in href:
                full_url = f"https://app.cognism.com{href}" if href.startswith("/") else href
                seen_urls.add(full_url)

        return list(seen_urls)

    except Exception as e:
        print(f"⚠️ Error extracting URLs: {e}")
        return []
