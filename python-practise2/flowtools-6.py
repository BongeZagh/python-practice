# match 有点像精细的搜索功能
# 精细到有点不好理解=i
#代码运行了没反应，留给以后处理吧，教程中也没有，告诉我运行结果，问GPT则是帮我改了代码，这不是我想要的


from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
