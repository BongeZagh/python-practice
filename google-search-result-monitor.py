
import requests
from bs4 import BeautifulSoup

# 使用代理
proxies = {
    'http': '127.0.0.1:1082'
}

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

# 构建请求url
url = 'https://www.google.com/search?q=covid'

# 发送请求
res = requests.get(url, headers=headers, proxies=proxies)

# 解析数据
soup = BeautifulSoup(res.text, 'html.parser')

# 获取搜索结果数量
num_results = soup.find('div',{'id':'result-stats'}).text

# 输出搜索结果数量
print("搜索结果数量: {}".format(num_results))

# 添加循环
while True:
    # 发送请求
    res = requests.get(url, headers=headers, proxies=proxies)

    # 解析数据
    soup = BeautifulSoup(res.text, 'html.parser')

    # 获取搜索结果数量
    num_results = soup.find('div', {'id': 'result-stats'}).text

    # 输出搜索结果数量
    print("搜索结果数量: {}".format(num_results))

    # 等待60秒
time.sleep(60)