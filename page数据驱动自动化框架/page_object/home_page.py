import time

from selenium import webdriver
from config.proj_vars import ini_file_path
from util.ini_parser import get_option_value
from util.page_element import get_element
from util.capture_pic import cature_pic
from page_object.index_page import  IndexPage

class Home:
    def __init__(self,driver):
        self.driver = driver

    #获取通讯录的链接
    def get_contact_link(self):
        xpath = get_option_value(ini_file_path, "home_page", "contact_link")
        try:
            contact_link = get_element(self.driver, xpath)
            return contact_link
        except Exception as e:
            print("定位登录后首页的通讯录链接元素失败，xpath表达式内容：%s" % xpath)
            raise Exception("定位登录后首页的通讯录链接元素失败，xpath表达式内容：%s" % xpath)

    def click_contact_link(self):
        try:
            contact_link = self.get_contact_link()
        except Exception as e:
            raise e
        try:
            contact_link.click()
            time.sleep(2)
        except Exception as e:
            print("点击通讯录链接失败！")
            raise Exception("点击通讯录链接失败！")

if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path="e:\\chromedriver.exe")
    driver.get("https://mail.126.com")
    index_page = IndexPage(driver)
    index_page.switch_to_iframe()
    index_page.input_user_name("testman1980")
    index_page.input_pass_word("wulaoshi1978")
    index_page.click_submit_button()
    home = Home(driver)
    home.click_contact_link()