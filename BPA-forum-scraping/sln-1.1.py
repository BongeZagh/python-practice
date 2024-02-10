from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
import csv
import os

# 使用WebDriverManager来自动下载并管理chromedriver
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # 打开网站登录页面
    driver.get("https://www.brookspriceaction.com/login.php")

    # 输入用户名和密码并提交登录
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")

    username.send_keys("Zagh")
    password.send_keys("y6pU6YqGSA!aVYw")
    password.send_keys(Keys.RETURN)

    # 等待登录完成
    time.sleep(3)

    # 读取CSV文件
    csv_filename = '2016picid.csv'
    with open(csv_filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        total_rows = sum(1 for row in reader)
        start_row = int(input(f"Enter the starting row number (1-{total_rows}): ")) - 1

        if start_row < 0 or start_row >= total_rows:
            print("Invalid row number.")
            exit()

        csvfile.seek(0)  # Reset the CSV file pointer
        next(reader)  # Skip header row

        for idx, row in enumerate(reader):
            if idx < start_row:
                continue
            pic_id = row['pic_id']
            title = row['Title']

            # 构建图片页面URL
            image_url = f"https://www.brookspriceaction.com/album_pic.php?pic_id={pic_id}&full=true"
            driver.get(image_url)

            # 提取图片URL
            img_element = driver.find_element(By.TAG_NAME, "img")
            img_src = img_element.get_attribute("src")

            # 创建保存图片的文件夹
            folder_name = "2022"
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)

            # 使用requests库下载图片
            response = requests.get(img_src)
            with open(os.path.join(folder_name, f"{title}.jpg"), "wb") as f:
                f.write(response.content)

except Exception as e:
    print("An error occurred:", e)

finally:
    # 关闭浏览器
    driver.quit()

