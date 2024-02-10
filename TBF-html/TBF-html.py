import csv
from bs4 import BeautifulSoup
import re

# 从文件中读取源代码
with open("A.txt", "r") as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a')

with open("B.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    for link in links:
        href = link['href']
        match = re.search(r"'(.*?)'", href)
        if match:
            clean_href = match.group(1)
            writer.writerow([clean_href])

