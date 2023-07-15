# 导入 markdown 模块
import markdown

# 打开文件 A.txt，并读取其中的内容
with open("A.txt", "r") as f:
    text = f.read()

# 转换 markdown 文本为 HTML 文本
# 使用 output_format="html5" 来指定输出的 HTML 版本为 HTML5
# 使用 extensions=["extra", "markdown.extensions.smart_strong"] 来指定使用 extra 和 smart_strong 扩展
html = markdown.markdown(text, output_format="html5", extensions=["extra", "markdown.extensions.smart_strong"])

# 打开文件 B.html，并写入转换后的 HTML 文本
with open("B.html", "w") as f:
    f.write(html)

# 打印转换后的 HTML 文本
print(html)