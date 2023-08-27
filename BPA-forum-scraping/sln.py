from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import requests

# 使用WebDriverManager来自动下载并管理chromedriver
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # 打开网站登录页面
    driver.get("https://www.brookspriceaction.com/login.php")

    # 输入用户名和密码并提交登录
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")

    username.send_keys("Zagh")
    password.send_keys("y6pU6YqGSA!aVYw")
    password.send_keys(Keys.RETURN)

    # 等待登录完成
    time.sleep(3)

    # 访问图片页面
    image_url = "https://www.brookspriceaction.com/album_pic.php?pic_id=582&full=true"
    driver.get(image_url)

    # 提取图片URL
    img_element = driver.find_element_by_tag_name("img")
    img_src = img_element.get_attribute("src")

    # 使用requests库下载图片
    response = requests.get(img_src)
    with open("image.jpg", "wb") as f:
        f.write(response.content)

except Exception as e:
    print("An error occurred:", e)

finally:
    # 关闭浏览器
    driver.quit()

