from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage as Base
from .selectors import Selectorss as S
from .data import Data as D
import datetime
import time
import sys
  
def __init__(self, browser):
    self.browser = browser
      
def test_positive_smouk_temporary_pass(browser):
    # установили нужный размер окна браузера
    browser.set_window_size (D.windows_width, D.windows_high)

    # заходим на страницу регистрации в VISITORCONTROL
    browser.get(D.url_autorization)

    # логинимся
    Base.element_exists_and_send(browser, S.xpath_input_login, D.login_user)
    Base.element_exists_and_send(browser, S.xpath_input_password, D.password_user)
    Base.element_exists_and_click(browser, S.xpath_button_autorization)

    # смотрим результат
    time.sleep(2)

    # заходим на страницу создания временного пропуска
    Base.element_exists_and_click(browser, S.xpath_vrem_propusk)

    ##############################################################################################
    # ЗАПОЛНЯЕМ ВКЛАДКУ "ДОКУМЕНТ ПОСЕТИТЕЛЯ"
    # заполняем ФИО
    Base.element_exists_and_send(browser, S.xpath_last_name, D.last_name)
    Base.element_exists_and_send(browser, S.xpath_first_name, D.first_name)
    Base.element_exists_and_send(browser, S.xpath_middle_name, D.middle_name)

    # вписываем срок действия пропуска с и по, предвартельно очистив значения полей
    browser.find_element_by_xpath(S.xpath_beginning_validity_period).clear()
    Base.element_exists_and_send(browser, S.xpath_beginning_validity_period, D.beginning_validity_period)
    browser.find_element_by_xpath(S.xpath_expiration_validity_period).clear()
    Base.element_exists_and_send(browser, S.xpath_expiration_validity_period, D.expiration_validity_period)


    ################## !!!!!!!!!!!!!!

    # выбираем из списка ФИО принимающей стороны
    browser.find_element_by_xpath(S.xpath_FIO_host_party).clear()
    Base.drop_down_element_click(browser, S.xpath_FIO_host_party, D.FIO_host_party)
    Base.uploading_file(browser, S.xpath_FIO_host_party, D.FIO_host_party)
    Base.element_exists_and_click(browser, S.xpath_FIO_number_in_list_host_party)
   
    time.sleep(3) 

    # coхраняем заявку
    Base.element_exists_and_click(browser, S.xpath_button_save) 
    # обязательно здесь time.sleep(), иначе заявка не сохраняется  
    time.sleep(9) 
