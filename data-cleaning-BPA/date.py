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

# 打印处理后的数据
print(data)
