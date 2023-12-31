
import re
from datetime import datetime
data = """
Title,Formatted Date,URL
08-06-2009,[[invalid date]],https://www.brookspriceaction.com/viewtopic.php?t=18
08-05-2009,[[Invalid Date]],https://www.brookspriceaction.com/viewtopic.php?t=17
08-04-2009,[[Invalid Date]],https://www.brookspriceaction.com/viewtopic.php?t=16
08-03-2009,[[Invalid Date]],https://www.brookspriceaction.com/viewtopic.php?t=15
07-31-2009,[[Invalid Date]],https://www.brookspriceaction.com/viewtopic.php?t=14
07-30-2009,[[Invalid Date]],https://www.brookspriceaction.com/viewtopic.php?t=13
"""

# 使用正则表达式匹配标题中的日期并进行替换
pattern = r"(\d{2}-\d{2}-\d{4})"
data = re.sub(pattern, lambda x: datetime.strptime(x.group(), '%m-%d-%Y').strftime('%Y%m%d'), data)
data = re.sub(pattern, lambda x: '[[' + datetime.strptime(x.group(), '%m-%d-%Y').strftime('%Y%m%d') + ']]', data)

# 将转换后的日期替换到 Formatted Date 列
data_lines = data.strip().split('\n')
data_lines = [line.split(',') for line in data_lines]
for line in data_lines[1:]:
    line[1] = line[0]  # 将标题中的日期替换到 Formatted Date 列
# 重新组合数据行并打印结果
data = '\n'.join([','.join(line) for line in data_lines])
print(data)

~/logseq-public/

