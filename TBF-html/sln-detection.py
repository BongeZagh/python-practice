import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

csv_file = 'input.csv'
output_file = 'output.csv'

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode

# Set up Chrome driver service
service = Service('/path/to/chromedriver')  # Replace with the path to your chromedriver executable

# Create a new Chrome driver instance
driver = webdriver.Chrome(service=service, options=chrome_options)

# Get total number of rows
with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    total_rows = sum(1 for _ in reader) - 1  # Subtract header row

# Create output CSV file and write header row
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['URL', 'Status', 'Keyword Found', 'Error Reason'])

# Initialize counter
processed_rows = 0

with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        url = row[0]

        try:
            # Try 3 times
            for _ in range(3):
                driver.get(url)
                status = 'Success'
                keyword = 'manufacture'
                keyword_found = keyword in driver.page_source
                error_reason = ''  # Initialize error reason as empty
                break  # If successful response obtained, break out of the loop
            else:
                # If 3 attempts failed, record error information
                status = 'Error'
                keyword_found = False
                error_reason = 'Maximum retries exceeded'

        except Exception as e:
            status = 'Error'
            keyword_found = False
            error_reason = str(e)  # Save error message to error reason

        with open(output_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([url, status, keyword_found, error_reason])

        # Update counter and display progress
        processed_rows += 1
        progress = processed_rows / total_rows * 100
        print(f"Progress: {processed_rows}/{total_rows} ({progress:.2f}%)")

# Close the Chrome driver
driver.quit()

print("Detection completed. Results have been saved to output.csv file.")
