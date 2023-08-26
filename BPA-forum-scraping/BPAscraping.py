import requests
from bs4 import BeautifulSoup
import re

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
#if "logout.php" in response.text:
#    print("Login successful")
#else:
#    print("Login failed")
##    print(response.text)
#    exit()

# 需要访问的链接列表
url_list = [
    "https://www.brookspriceaction.com/viewtopic.php?t=1153",
    "https://www.brookspriceaction.com/viewtopic.php?t=807",
    # 添加更多链接
]

# 下载图片
for url in url_list:
    response = session.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        pic_id_element = soup.find("span", id="pic_id")  # 根据具体情况修改选择器
        if pic_id_element:
            pic_id = pic_id_element.text.strip()

            # 构建图片下载链接
            image_url = f"https://www.brookspriceaction.com/album_showpage.php?full=true&pic_id={pic_id}"
            image_response = session.get(image_url)
            if image_response.status_code == 200:
                filename = f"pic_{pic_id}.png"
                with open(filename, "wb") as f:
                    f.write(image_response.content)
                print(f"Downloaded: {filename}")
            else:
                print(f"Failed to download image: {pic_id}")
        else:
            print("pic_id element not found")
            print(response.text)

    else:
        print(f"Failed to access link: {url}")

