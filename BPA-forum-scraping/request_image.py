import requests
from bs4 import BeautifulSoup
import re
import requests

# 登录信息
login_url = "https://www.brookspriceaction.com/login.php?sid=040bbcfe6e0945d2ac521e1208ca3466"
username = "Zagh"
password = "y6pU6YqGSA!aVYw"


# 创建会话
session = requests.Session()

# 发送登录POST请求
login_data = {
    "username": username,
    "password": password,
    "login": "login",
}
response = session.post(login_url, data=login_data)



# 检查登录是否成功
# if "logout.php" in response.text:
#     print("Login successful")
# else:
#     print("Login failed")
#     print(response.text)
#     exit()
# 目标图片链接
#target_image_url = "https://www.brookspriceaction.com/album_pic.php?pic_id=582&full=true"
#
## 发送GET请求获取图片页面内容
#image_response = session.get(target_image_url)
#if image_response.status_code == 200:
#    image_soup = BeautifulSoup(image_response.content, "html.parser")
#    # 在此使用Beautiful Soup解析页面内容，检查是否有图片可以下载
#    # 根据网页的具体结构进行解析，可能涉及到具体的CSS选择器、类名等
#    # 例如: image_element = image_soup.find("img", class_="image-class")
#    # 如果找到了图片元素，表示有图片可以下载
#else:
#    print("Failed to access image page")

url = "https://www.brookspriceaction.com/album_pic.php?pic_id=582&full=true"

# 获取网页内容
html_doc = requests.get(url).text

# 使用正则表达式提取图片URL
img_url = re.search(r'<img src="(.*?)"', html_doc).group(1)

print(img_url)
print(response.text)
