from bs4 import BeautifulSoup
import csv
from datetime import datetime

# 读取 txt 文件
with open('A.txt', 'r', encoding='utf-8') as txt_file:
    data = txt_file.read()

# 创建 Beautiful Soup 对象
soup = BeautifulSoup(data, 'html.parser')

# 查找所有包含标题和网址的 <a> 元素
links = soup.find_all('a', class_='topictitle')

# 提取标题、日期和网址，并存储在列表中
data_list = []
for link in links:
    title = link.get_text()
    url = "https://www.brookspriceaction.com/" + link['href']  # 添加前缀

    # 提取日期部分
    date_string = title.split()[:3]
    date_string = " ".join(date_string)
    
    # 解析日期并进行格式转换
    original_date = datetime.strptime(date_string, '%m-%d-%Y %A')
    formatted_date = "[[" + original_date.strftime('%Y%m%d') + "]]"

    data_list.append([title, formatted_date, url])

# 将提取的数据输出到 CSV 文件
csv_filename = 'extracted_data.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Title', 'Formatted Date', 'URL'])  # 写入标题行
    csv_writer.writerows(data_list)                           # 写入数据行

print("Data extracted and saved to", csv_filename)

