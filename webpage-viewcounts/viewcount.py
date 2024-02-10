import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Khmer_language"  # 替换为你要检测的网页 URL

# 发起 HTTP 请求
response = requests.get(url)
html_content = response.text

# 解析 HTML 内容
soup = BeautifulSoup(html_content, "html.parser")
view_count_element = soup.select_one(".view-count")  # 使用合适的 CSS 选择器选择包含浏览量的元素
view_count = view_count_element.text.strip()  # 提取元素的文本内容，并去除首尾的空白字符

# 处理和显示数据
print("月浏览量:", view_count)

