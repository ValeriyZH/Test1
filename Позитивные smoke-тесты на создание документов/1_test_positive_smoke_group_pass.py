from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import time
import sys
import os
sys.path.append(os.path.abspath('../Test1'))
from base_page import BasePage as Base
from selectorss import Selectorss as S
from data import Data as D
from loguru import logger
  
def __init__(self, browser):
    self.browser = browser

@logger.catch
      
def test_positive_smouk_temporary_pass(browser):
    
    logger.info('# устанавливаем имя файла для логирования')
    Base.logging_file(D.log_file_name)

    logger.info('# ЗАПУСТИЛИ ПОЗИТИВНЫЙ СМОУК-ТЕСТ НА СОЗДАНИЕ ЗАЯВКИ НА ГРУППОВОЙ ПРОПУСК')
    
    logger.info('# установили нужный размер окна браузера')
    browser.set_window_size (D.windows_width, D.windows_high)

    logger.info('# заходим на страницу регистрации в VISITORCONTROL')
    browser.get(D.url_autorization)

    logger.info('# логинимся')
    Base.element_exists_and_send(browser, S.xpath_input_login, D.login_user)
    Base.element_exists_and_send(browser, S.xpath_input_password, D.password_user)
    Base.element_exists_and_click(browser, S.xpath_button_autorization)

    logger.info('# смотрим результат')
    time.sleep(2)

    logger.info('# заходим на страницу создания группового пропуска')
    Base.element_exists_and_click(browser, S.xpath_group_propusk)

    logger.info('# вписываем срок действия пропуска с и по, предвартельно очистив значения полей')
    browser.find_element_by_xpath(S.xpath_beginning_validity_period).clear()
    logger.info('# 1')
    Base.element_exists_and_send(browser, S.xpath_beginning_validity_period, D.beginning_validity_period)
    logger.info('# 2')
    browser.find_element_by_xpath(S.xpath_expiration_validity_period).clear()
    logger.info('# 3')
    Base.element_exists_and_send(browser, S.xpath_expiration_validity_period, D.expiration_validity_period)
    logger.info('# 4')
 
    logger.info('# выбираем из списка ФИО принимающей стороны')
    browser.find_element_by_xpath(S.xpath_FIO_group_host_party).clear()
    logger.info('# 1')
    Base.drop_down_element_click(browser, S.xpath_FIO_group_host_party, D.FIO_host_party)
    logger.info('# 2')
    Base.uploading_file(browser, S.xpath_FIO_group_host_party, D.FIO_host_party)
    logger.info('# 3')
    Base.element_exists_and_click(browser, S.xpath_FIO_group_host_party_list)
    logger.info('# 4')

    
   #################################################
    logger.info('# указываем адрес из списка "Адрес*:"')
    browser.find_element_by_xpath(S.xpath_group_address_host_party).clear()
    logger.info('# 1')
    Base.drop_down_element_click(browser, S.xpath_group_address_host_party, D.host_party_address)
    logger.info('# 2')
    Base.uploading_file(browser, S.xpath_group_address_host_party, D.host_party_address)
    logger.info('# 3')
    Base.element_exists_and_click(browser, S.xpath_group_address_host_party_list)
    logger.info('# 4')

    logger.info('# заполняем фамилию')
    Base.element_exists_and_send(browser, S.xpath_last_name, D.last_name)
    
    logger.info('# добавляем посетителя')
    Base.element_exists_and_click(browser, S.xpath_button_add_visitor)

    time.sleep(3)

    logger.info('# coхраняем заявку')
    Base.element_exists_and_click(browser, S.xpath_button_save) 
    logger.info('# обязательно здесь time.sleep(), иначе заявка не сохраняется')  
    time.sleep(7) 

    logger.info('# ЗАВЕРШИЛИ ПОЗИТИВНЫЙ СМОУК-ТЕСТ НА СОЗДАНИЕ ЗАЯВКИ НА ГРУППОВОЙ ПРОПУСК')
    logger.info('****************************************************************************')
    