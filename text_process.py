# 获取用户输入
text = input("请输入文本：")

# 替换 \r 为换行符
text = text.replace('\r', '\n')

# 输出结果
print(text)