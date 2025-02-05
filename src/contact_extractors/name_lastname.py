from selenium.webdriver.common.by import By

def extract_name(driver):
    """Extracts full name from the webpage and splits it into Name and Last Name."""
    try:
        # Find the full name element using its specific class
        name_element = driver.find_element(By.XPATH, "//a[contains(@class, 't-text-primary-600')]")
        full_name = name_element.text.strip()

        # Split into first and last name
        name_parts = full_name.split(" ", 1)  # Splits at the first space

        first_name = name_parts[0] if name_parts else "Not found"
        last_name = name_parts[1] if len(name_parts) > 1 else "Not found"

        return {
            "Name": first_name,
            "Last_Name": last_name
        }

    except:
        return {
            "Name": "Not found",
            "Last_Name": "Not found"
        }
