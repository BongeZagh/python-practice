import csv
import requests
from bs4 import BeautifulSoup

csv_file = 'input.csv'
output_file = 'output.csv'

# 获取总行数
with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    total_rows = sum(1 for _ in reader) - 1  # 减去标题行

# 创建输出 CSV 文件并写入标题行
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['URL', 'Status', 'Keyword Found', 'Error Reason'])  # 添加 'Error Reason' 列

# 初始化计数器
processed_rows = 0

with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        url = row[0]

        try:
            response = requests.get(url)
            response.raise_for_status()
            status = 'Success'
            soup = BeautifulSoup(response.content, 'html.parser')
            keyword = 'manufacture'
            keyword_found = keyword in soup.get_text()
            error_reason = ''  # 初始化错误原因为空
        except requests.exceptions.RequestException as e:
            status = 'Error'
            keyword_found = False
            error_reason = str(e)  # 将错误信息保存到错误原因中

        with open(output_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([url, status, keyword_found, error_reason])

        # 更新计数器并显示进度
        processed_rows += 1
        progress = processed_rows / total_rows * 100
        print(f"进度：{processed_rows}/{total_rows} ({progress:.2f}%)")

print("检测完成，结果已保存到 output.csv 文件中。")

