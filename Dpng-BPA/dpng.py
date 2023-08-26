import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 目标网页的URL
base_url = "https://www.brookstradingcourse.com/wp-content/uploads/2016/01/"

# 发送HTTP请求获取网页内容
response = requests.get(base_url)
html_content = response.content

# 使用BeautifulSoup解析网页内容
soup = BeautifulSoup(html_content, "html.parser")

# 查找所有的<a>标签
links = soup.find_all("a")

# 遍历每个链接
for link in links:
    href = link.get("href")
    # 如果链接以".png"结尾（或其他您想要的文件类型），则获取文件信息
    if href and href.endswith(".png"):
        full_url = urljoin(base_url, href)
        filename = os.path.basename(full_url)
        
        # 发送HEAD请求获取文件大小
        head_response = requests.head(full_url)
        content_length = head_response.headers.get("content-length")
        
        # 如果文件大小大于 100KB，下载文件
        if content_length and int(content_length) > 100 * 1024:  # 100KB = 100 * 1024 bytes
            file_response = requests.get(full_url)
            with open(filename, "wb") as f:
                f.write(file_response.content)
            print(f"Downloaded: {filename}")

