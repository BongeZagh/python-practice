# 第一个可以运行的版本，但是是对比差异
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from nltk.corpus import wordnet
from webdriver_manager.chrome import ChromeDriverManager
import nltk
from nltk.corpus import wordnet as wn



# 下载WordNet数据集
nltk.download('wordnet')


# 设置Selenium WebDriver
driver = webdriver.Chrome(ChromeDriverManager().install())
options = Options()
options.add_argument('--headless')  # 无头模式，不显示浏览器窗口
driver = webdriver.Chrome(ChromeDriverManager().install())


# 示例网页A和网页B的URL
url_a = 'http://www.ascapacitor.com/'
url_b = ' http://www.asg-jergens.com/'

# 加载网页A
driver.get(url_a)
html_a = driver.page_source
soup_a = BeautifulSoup(html_a, 'html.parser')
text_a = soup_a.get_text()

# 加载网页B
driver.get(url_b)
html_b = driver.page_source
soup_b = BeautifulSoup(html_b, 'html.parser')
text_b = soup_b.get_text()

# 关闭Selenium WebDriver
driver.quit()

# 将文本数据传递给NLTK进行比对
# 这里只是一个示例，您可以根据需求进行更详细的文本比对处理
# 以下是一个简单的示例，计算网页A和网页B的词汇差异
#words_a = set(wordnet.words(text_a))
#words_b = set(wordnet.words(text_b))

# ...

words_a = set(wn.words(lang='eng'))
words_b = set(wn.words(lang='eng'))

word_diff = words_a.symmetric_difference(words_b)

print("网页A和网页B的词汇差异:")
print(word_diff)

