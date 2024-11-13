import time

from selenium import webdriver
from config.proj_vars import ini_file_path
from util.ini_parser import get_option_value
from util.page_element import get_element
from util.capture_pic import cature_pic
from page_object.index_page import  IndexPage
from page_object.home_page import Home

class Contact:

    def __init__(self,driver):
        self.driver = driver

    #获取新建联系人按钮
    def get_create_contact_button(self):
        xpath = get_option_value(ini_file_path, "contact_page", "create_contact_button")
        try:
            create_contact_button = get_element(self.driver, xpath)
            return create_contact_button
        except Exception as e:
            print("定位通讯录页面的新建联系人按钮元素失败，xpath表达式内容：%s" % xpath)
            raise Exception("定位通讯录页面的新建联系人按钮元素失败，xpath表达式内容：%s" % xpath)

    #点击新建联系人按钮失败
    def click_create_contact_button(self):
        try:
            create_contact_button = self.get_create_contact_button()
        except Exception as e:
            raise e
        try:
            create_contact_button.click()
            time.sleep(2)
        except Exception as e:
            print("点击新建联系人按钮元素失败！")
            raise Exception("点击新建联系人按钮元素失败！")

    #获得名字输入框
    def get_name(self):
        xpath = get_option_value(ini_file_path, "contact_page", "name")
        try:
            name = get_element(self.driver, xpath)
            return name
        except Exception as e:
            print("定位通讯录页面的姓名输入框元素失败，xpath表达式内容：%s" % xpath)
            raise Exception("定位通讯录页面的姓名输入框元素失败，xpath表达式内容：%s" % xpath)

    #输入名字
    def input_name(self,name):
        try:
            name_input = self.get_name()
        except Exception as e:
            raise e
        try:
            name_input.send_keys(name)
        except Exception as e:
            print("在姓名输入框中输入内容失败！")
            raise Exception("在姓名输入框中输入内容失败！")

    #获得电子邮件输入框
    def get_email(self):
        xpath = get_option_value(ini_file_path, "contact_page", "email")
        try:
            email = get_element(self.driver, xpath)
            return email
        except Exception as e:
            print("定位通讯录页面的电子邮件输入框元素失败，xpath表达式内容：%s" % xpath)
            raise Exception("定位通讯录页面的电子邮件输入框元素失败，xpath表达式内容：%s" % xpath)

    #输入电子邮件输入框内容
    def input_email(self,email):
        try:
            email_input = self.get_email()
        except Exception as e:
            raise e
        try:
            email_input.send_keys(email)
        except Exception as e:
            print("在电子邮件输入框中输入内容失败！")
            raise Exception("在电子邮件输入框中输入内容失败！")

    #获取手机号输入框
    def get_mobile(self):
        xpath = get_option_value(ini_file_path, "contact_page", "mobile")
        try:
            mobile = get_element(self.driver, xpath)
            return mobile
        except Exception as e:
            print("定位通讯录页面的手机号输入框元素失败，xpath表达式内容：%s" % xpath)
            raise Exception("定位通讯录页面的手机号输入框元素失败，xpath表达式内容：%s" % xpath)

    #输入手机号
    def input_mobile(self,mobile):
        try:
            mobile_input = self.get_mobile()
        except Exception as e:
            raise e
        try:
            mobile_input.send_keys(mobile)
        except Exception as e:
            print("在手机号输入框中输入内容失败！")
            raise Exception("在手机号输入框中输入内容失败！")

    #获得标星复选框
    def get_star(self):
        xpath = get_option_value(ini_file_path, "contact_page", "star")
        try:
            star = get_element(self.driver, xpath)
            return star
        except Exception as e:
            print("定位通讯录页面的标星复选框元素失败，xpath表达式内容：%s" % xpath)
            raise Exception("定位通讯录页面的标星复选框元素失败，xpath表达式内容：%s" % xpath)

    #点击标星复选框
    def click_star(self,click_flag):
        try:
            star = self.get_star()
        except Exception as e:
            raise e
        try:
            if click_flag:
                star.click()
        except Exception as e:
            print("点击标星复选框失败！")
            raise Exception("点击标星复选框失败！")

    #获取备注输入框
    def get_comment(self):
        xpath = get_option_value(ini_file_path, "contact_page", "comment")
        try:
            comment = get_element(self.driver, xpath)
            return comment
        except Exception as e:
            print("定位通讯录页面的备注元素失败，xpath表达式内容：%s" % xpath)
            raise Exception("定位通讯录页面的备注元素失败，xpath表达式内容：%s" % xpath)

    #在备注输入框中输入
    def input_comment(self,comment):
        try:
            comment_input = self.get_comment()
        except Exception as e:
            raise e
        try:
            comment_input.send_keys(comment)
        except Exception as e:
            print("在备注输入框中输入内容失败！")
            raise Exception("在备注输入框中输入内容失败！")

    #获取确定按钮
    def get_confirm_button(self):
        xpath = get_option_value(ini_file_path, "contact_page", "confirm_button")
        try:
            confirm_button  = get_element(self.driver, xpath)
            return confirm_button
        except Exception as e:
            print("定位通讯录页面的确定按钮元素失败，xpath表达式内容：%s" % xpath)
            raise Exception("定位通讯录页面的确定按钮元素失败，xpath表达式内容：%s" % xpath)

    #点击确定按钮
    def click_confirm_button(self):
        try:
            confirm_button = self.get_confirm_button()
        except Exception as e:
            raise e
        try:
            confirm_button.click()
        except Exception as e:
            print("点击确定按钮失败！")
            raise Exception("点击确定按钮失败！")

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
    contact = Contact(driver)
    contact.click_create_contact_button()
    contact.input_name("老王")
    contact.input_email("33dsdf@qq.com")
    contact.input_mobile("13500099898")
    contact.click_star(True)
    contact.input_comment("今天天气不错")
    contact.click_confirm_button()