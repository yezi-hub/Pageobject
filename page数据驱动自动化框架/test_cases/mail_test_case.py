import time

from selenium import webdriver
from config.proj_vars import ini_file_path
from util.ini_parser import get_option_value
from util.page_element import get_element
from util.capture_pic import cature_pic
from page_object.index_page import  IndexPage
from page_object.home_page import Home
from page_object.contact_page import Contact

def login(user_name,pass_word):
    try:
        driver = webdriver.Chrome(executable_path="e:\\chromedriver.exe")
        driver.get("https://mail.126.com")
        index_page = IndexPage(driver)
        index_page.switch_to_iframe()
        index_page.input_user_name(user_name)
        index_page.input_pass_word(pass_word)
        index_page.click_submit_button()
        time.sleep(3)
        assert "通讯录" in driver.page_source, "断言词通讯录没有出现在页面源码中"
        return  driver
    except AssertionError as e:
        print(e)
        raise e
    except Exception as e:
        raise e

def visit_contact(driver):
    try:
        home = Home(driver)
        home.click_contact_link()
    except Exception as e:
        raise e

def add_contact(driver,name,email,mobile,comment,assert_word,star=False):
    try:
        contact = Contact(driver)
        contact.click_create_contact_button()
        contact.input_name(name)
        contact.input_email(email)
        contact.input_mobile(mobile)
        contact.click_star(star)
        contact.input_comment(comment)
        contact.click_confirm_button()
        time.sleep(4)
        assert_words = assert_word.split("||")
        for assert_word in assert_words:
            assert assert_word in driver.page_source,"断言词 %s 没有出现在页面源码中" %assert_word
    except AssertionError as e:
        print(e)
        raise e
    except Exception as e:
        print(e)
        raise e

if __name__ == "__main__":
    driver = login("testman1980","wulaoshi1978")
    visit_contact(driver)
    add_contact(driver,"老李","339dddd@qq.com","13511111111","好好学习！",True)
    driver.quit()