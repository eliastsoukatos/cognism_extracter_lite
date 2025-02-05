import os
import random
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve credentials
COGNISM_EMAIL = os.getenv("COGNISM_EMAIL")
COGNISM_PASSWORD = os.getenv("COGNISM_PASSWORD")

# Retrieve configuration settings
OVERWRITE_SEGMENT = os.getenv("OVERWRITE_SEGMENT", "False").lower() == "true"

# Function to introduce variability in waiting times
def randomize_wait_time(base_time):
    return round(base_time * random.uniform(0.5, 1.5), 2)  # Adds variability

# Time settings with randomization
SCROLL_ITERATIONS = int(os.getenv("SCROLL_ITERATIONS", 3))  # Fixed integer

PAGE_LOAD_TIMEOUT = randomize_wait_time(float(os.getenv("PAGE_LOAD_TIMEOUT", 10)))  
EXTRA_RENDER_TIME = randomize_wait_time(float(os.getenv("EXTRA_RENDER_TIME", 3)))  
SCROLL_WAIT_TIME = randomize_wait_time(float(os.getenv("SCROLL_WAIT_TIME", 1)))  
TAB_LOAD_TIME = randomize_wait_time(float(os.getenv("TAB_LOAD_TIME", 3)))  

# Randomized wait time between scraping pages
SCRAPING_DELAY = randomize_wait_time(float(os.getenv("SCRAPING_DELAY", 2)))  
