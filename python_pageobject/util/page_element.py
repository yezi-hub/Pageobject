from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util.ini_parser import get_option_value
from config.proj_vars import ini_file_path

#通过xpath获取对应元素
def get_element(driver,xpath):
    try:
        # 设置显式等待时间（例如 10 秒）
        wait = WebDriverWait(driver, 10)
        # 等待直到元素出现（例如，XPATH 为 'xpath' 的元素）
        element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        return element
    except Exception as e:
        print("xpath的表达式 %s 无法定位到元素！" %xpath)
        return None

def get_elements(driver,xpath):
    try:
        # 设置显式等待时间（例如 10 秒）
        wait = WebDriverWait(driver, 10)
        # 等待直到元素出现（例如，XPATH 为 'xpath' 的元素）
        # 等待直到所有具有特定类名的元素都出现在页面上
        elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
        return elements
    except Exception as e:
        print("xpath的表达式 %s 无法定位到元素！" %xpath)
        return []

if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path="e:\\chromedriver.exe")
    driver.get("https://mail.126.com")
    xpath = get_option_value(ini_file_path,"index_page","iframe")
    iframe = get_elements(driver,xpath)
    print(iframe)
    #element = get_element(driver,"//input[@id='query1']")
    #if element:
    #    element.send_keys("找到了")
    #else:
    #    print("元素没找到！")

    #elements = get_elements(driver, "//a")
    #print(len(elements))