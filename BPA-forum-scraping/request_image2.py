import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# 登录信息
login_url = "https://www.brookspriceaction.com/login.php"
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

# 读取CSV文件并获取URL列表
df = pd.read_csv('urls2.csv')
url_list = df['URL'].tolist()

# 遍历链接列表
for url in url_list:
    if pd.notna(url):  # Check if the URL is not NaN (not missing)
        response = session.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
    
    # 查找pic_id并打印结果
    a_tags = soup.find_all('a', href=re.compile(r'album_showpage\.php\?pic_id=(\d+)'))
    pic_ids = []
    for a_tag in a_tags:
        match = re.search(r'pic_id=(\d+)', a_tag['href'])
        if match:
            pic_id = match.group(1)
            pic_ids.append(pic_id)
    
    # 将pic_ids写入CSV文件
    df.loc[df['URL'] == url, 'pic_id'] = ', '.join(pic_ids)
    df.to_csv('urls2.csv', index=False)

# 检查登录是否成功
if "logout.php" in response.text:
    print("Login successful")
else:
    print("Login failed")
    exit()

url = "https://www.brookspriceaction.com/album_pic.php?pic_id=582&full=true"

# 获取网页内容
html_doc = requests.get(url).text

# 使用正则表达式提取图片URL
img_url = re.search(r'<img src="(.*?)"', html_doc).group(1)

print(img_url)

