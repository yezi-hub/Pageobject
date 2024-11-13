import time

from selenium import webdriver
from config.proj_vars import ini_file_path
from util.ini_parser import get_option_value
from util.page_element import get_element
from util.capture_pic import cature_pic

#登录页面
class IndexPage:

    def __init__(self,driver):
        self.driver = driver

    #获取iframe对象
    def get_iframe(self):
        xpath = get_option_value(ini_file_path,"index_page","iframe")
        try:
            iframe = get_element(self.driver,xpath)
            return iframe
        except Exception as e:
            print("定位登录首页的iframe元素失败，xpath表达式内容：%s" %xpath)
            raise  Exception("定位登录首页的iframe元素失败，xpath表达式内容：%s" %xpath)

    #切换到iframe中
    def switch_to_iframe(self):
        try:
            iframe = self.get_iframe()
        except Exception as e:
            raise  e
        try:
            self.driver.switch_to.frame(iframe)
        except Exception as e:
            print("切换到iframe失败")
            raise Exception("切换到iframe失败")

    #获取到user_name的输入框对象
    def get_user_name(self):
        xpath = get_option_value(ini_file_path,"index_page","user_name")
        try:
            user_name = get_element(self.driver,xpath)
            return user_name
        except Exception as e:
            print("定位登录首页的用户名输入框元素失败，xpath表达式内容：%s" %xpath)
            raise  Exception("定位登录首页的用户名输入框元素失败，xpath表达式内容：%s" %xpath)

    #在用户名输入框中输入用户名
    def input_user_name(self,user_name):
        try:
            user_name_input = self.get_user_name()
        except Exception as e:
            raise  e
        try:
            user_name_input.send_keys(user_name)
        except Exception as e:
            print("输入用户名输入框失败！")
            raise Exception("输入用户名输入框失败！")

    #获取密码输入框
    def get_pass_word(self):
        xpath = get_option_value(ini_file_path,"index_page","pass_word")
        try:
            pass_word = get_element(self.driver,xpath)
            return pass_word
        except Exception as e:
            print("定位登录首页的密码输入框元素失败，xpath表达式内容：%s" %xpath)
            raise  Exception("定位登录首页的密码输入框元素失败，xpath表达式内容：%s" %xpath)

    #在密码输入框输入密码
    def input_pass_word(self,pass_word):
        try:
            pass_word_input = self.get_pass_word()
        except Exception as e:
            raise  e
        try:
            pass_word_input.send_keys(pass_word)
        except Exception as e:
            print("输入用户名输入框失败！")
            raise Exception("输入用户名输入框失败！")

    #获取登录按钮
    def get_submit_button(self):
        xpath = get_option_value(ini_file_path, "index_page", "submit_button")
        try:
            submit_button = get_element(self.driver, xpath)
            return submit_button
        except Exception as e:
            print("定位登录首页的登录元素失败，xpath表达式内容：%s" % xpath)
            raise Exception("定位登录首页的登录按钮元素失败，xpath表达式内容：%s" % xpath)

    # 点击登录按钮
    def click_submit_button(self):
        try:
            submit_button = self.get_submit_button()
        except Exception as e:
            raise e
        try:
            submit_button.click()
            self.switch_out_iframe()
            time.sleep(5)
        except Exception as e:
            print("点击登录按钮失败！")
            raise Exception("点击登录按钮失败！失败！")

    #切换出iframe
    def switch_out_iframe(self):
        self.driver.switch_to.default_content()

if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path="e:\\chromedriver.exe")
    driver.get("https://mail.126.com")
    index_page = IndexPage(driver)
    index_page.switch_to_iframe()
    index_page.input_user_name("testman1980")
    index_page.input_pass_word("wulaoshi1978")
    index_page.click_submit_button()
