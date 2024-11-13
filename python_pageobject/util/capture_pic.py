from selenium import webdriver
from config.proj_vars import caputre_pic_dir_path
from util.dir_util import create_hour_dir
from util.time_util import get_chinese_time
import os

#封装截图
def cature_pic(driver):
    hour_dir_path = create_hour_dir(caputre_pic_dir_path)
    time_pic_name = get_chinese_time()+".png"
    pic_path = os.path.join(hour_dir_path,time_pic_name)
    if hour_dir_path:
        driver.save_screenshot(pic_path)
        return pic_path
    else:
        print("截图生成不成功！")
        return None

if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path="e:\\chromedriver.exe")
    driver.get("https://www.sogou.com")
    pic_path = cature_pic(driver)
    print(pic_path)
    driver.quit()