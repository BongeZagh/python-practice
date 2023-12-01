import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

csv_file = 'input.csv'
output_file = 'output.csv'
timeout = 10  # Timeout in seconds

# Set up Selenium WebDriver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Get total number of rows in the CSV file
with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    total_rows = sum(1 for _ in reader) - 1  # Subtract 1 for the header row

# Create the output CSV file and write the header row
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['URL', 'Status', 'Keyword Found', 'Keyword Found About Us', 'Error Reason'])

# Initialize counters
processed_rows = 0

with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    for row in reader:
        url = row[0]

        try:
            driver.set_page_load_timeout(timeout)
            driver.get(url)
            status = 'Success'
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            keywords = ['manufacturing', 'PCB', 'components', 'component', 'assembly']
            keyword_found = any(keyword in soup.get_text() for keyword in keywords)
            error_reason = ''  # Initialize error reason as empty

            # Check if "About Us" link exists
            about_us_link = None
            links = driver.find_elements(By.TAG_NAME, 'a')
            for link in links:
                link_text = link.text.lower()
                if 'about' in link_text or 'about us' in link_text:
                    about_us_link = link
                    break

            if about_us_link:
                try:
                    about_us_link.click()  # Click on "About Us" link
                    soup_about_us = BeautifulSoup(driver.page_source, 'html.parser')
                    keyword_found_about_us = any(keyword in soup_about_us.get_text() for keyword in keywords)
                except TimeoutException:
                    status = 'Error'
                    keyword_found_about_us = False
                    error_reason = 'Timeout while loading "About Us" page'
                except Exception as e:
                    status = 'Error'
                    keyword_found_about_us = False
                    error_reason = str(e)
            else:
                keyword_found_about_us = False

        except TimeoutException:
            status = 'Error'
            keyword_found = False
            error_reason = 'Timeout'
            keyword_found_about_us = False
        except Exception as e:
            status = 'Error'
            keyword_found = False
            error_reason = str(e)
            keyword_found_about_us = False

        with open(output_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([url, status, keyword_found, keyword_found_about_us, error_reason])

        # Update counter and display progress
        processed_rows += 1
        progress = processed_rows / total_rows * 100
        print(f"Progress: {processed_rows}/{total_rows} ({progress:.2f}%)")

# Close the Selenium WebDriver
driver.quit()

print("Detection completed. The results have been saved to output.csv file.")

