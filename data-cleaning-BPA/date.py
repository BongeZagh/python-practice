import pandas as pd
from datetime import datetime
import io

data = """
Title,Formatted Date,URL
08-06-2009,[[invalid date]],https://www.brookspriceaction.com/viewtopic.php?t=18
08-05-2009,[[Invalid Date]],https://www.brookspriceaction.com/viewtopic.php?t=17
08-04-2009,[[Invalid Date]],https://www.brookspriceaction.com/viewtopic.php?t=16
08-03-2009,[[Invalid Date]],https://www.brookspriceaction.com/viewtopic.php?t=15
07-31-2009,[[Invalid Date]],https://www.brookspriceaction.com/viewtopic.php?t=14
07-30-2009,[[Invalid Date]],https://www.brookspriceaction.com/viewtopic.php?t=13
"""

# 将数据加载为pandas的DataFrame对象
df = pd.read_csv(io.StringIO(data))

# 将标题中的日期转换并替换到Formatted Date列
df['Formatted Date'] = df.apply(lambda row: row['Formatted Date'].replace('[[invalid date]]', '[[' + datetime.strptime(row['Title'], '%m-%d-%Y').strftime('%Y%m%d') + ']]'), axis=1)

# 打印处理后的DataFrame
print(df.to_csv(index=False))

