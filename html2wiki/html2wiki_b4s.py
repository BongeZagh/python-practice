from bs4 import BeautifulSoup
import mwparserfromhell

# 读取HTML文件
with open("example.html", "r") as f:
    html = f.read()

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(html, "html.parser")

# 创建一个新的维基文本对象
wikicode = mwparserfromhell.wikicode.Wikicode()

# 遍历HTML标记，并将其转换为维基格式
for tag in soup.find_all():
    # 处理标题
    if tag.name in ["h1", "h2", "h3", "h4", "h5", "h6"]:
        level = int(tag.name[1])
        wikicode.append(" " * (level - 1) + tag.text + "\n\n")
    # 处理段落
    elif tag.name == "p":
        wikicode.append(tag.text + "\n\n")
    # 处理列表
    elif tag.name in ["ul", "ol"]:
        for li in tag.find_all("li"):
            wikicode.append("* " + li.text + "\n")
    # 处理链接
    elif tag.name == "a":
        wikicode.append("[[" + tag["href"] + "|" + tag.text + "]]")
    # 处理其他标记
    else:
        wikicode.append(tag.text)

# 输出维基文本
print(wikicode)

