import sys
import os

# Add src to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from src.main_urls import run_urls_scraper
from src.main_csv import export_contacts_to_csv  # ✅ Import the new function

def main():
    print("Welcome to the Cognism Scraper.")
    print("Press 1 to start scraping contacts from your Cognism list.")
    print("Press 2 to export contacts to CSV.")

    user_input = input("Enter your choice: ")

    if user_input == "1":
        run_urls_scraper()    
    elif user_input == "2":
        export_contacts_to_csv()  # ✅ Calls the new function to export CSV
    else:
        print("❌ Invalid option. Exiting...")

if __name__ == "__main__":
    main()
