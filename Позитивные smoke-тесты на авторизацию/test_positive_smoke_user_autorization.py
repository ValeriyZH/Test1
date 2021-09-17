from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import time
import sys
import os
sys.path.append(os.path.abspath('../Test1'))
from base_page import BasePage as Base
from selectors import Selectorss as S
from data import Data as D

  
def __init__(self, browser):
    self.browser = browser
      
def test_positive_user_autorization(browser):
    print('# установили нужный размер окна браузера')
    browser.set_window_size (D.windows_width, D.windows_high)

    print('# заходим на страницу регистрации в VISITORCONTROL')
    browser.get(D.url_autorization)

    print('# логинимся')
    Base.element_exists_and_send(browser, S.xpath_input_login, D.login_user)
    Base.element_exists_and_send(browser, S.xpath_input_password, D.password_user)
    Base.element_exists_and_click(browser, S.xpath_button_autorization)

    print('# смотрим результат')
    time.sleep(3)

   