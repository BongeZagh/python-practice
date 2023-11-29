import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
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
    writer.writerow(['URL', 'Status', 'Keyword Found', 'Error Reason'])

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
        except TimeoutException:
            status = 'Error'
            keyword_found = False
            error_reason = 'Timeout'
        except Exception as e:
            status = 'Error'
            keyword_found = False
            error_reason = str(e)

        with open(output_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([url, status, keyword_found, error_reason])

        # Update counter and display progress
        processed_rows += 1
        progress = processed_rows / total_rows * 100
        print(f"Progress: {processed_rows}/{total_rows} ({progress:.2f}%)")

# Close the Selenium WebDriver
driver.quit()

print("Detection completed. The results have been saved to output.csv file.")

