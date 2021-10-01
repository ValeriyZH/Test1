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
    

    logger.info('# ЗАПУСТИЛИ ПОЗИТИВНЫЙ СМОУК-ТЕСТ НА СОЗДАНИЕ ЗАЯВКИ НА РАЗОВЫЙ ПРОПУСК')

    logger.info('# установили нужный размер окна браузера')
    browser.set_window_size (D.windows_width, D.windows_high)

    logger.info('# заходим на страницу регистрации в VISITORCONTROL')
    browser.get(D.url_autorization_RP)

    logger.info('# логинимся')
    Base.element_exists_and_send(browser, S.xpath_input_login, D.login_user_RP)
    Base.element_exists_and_send(browser, S.xpath_input_password, D.password_user_RP)
    Base.element_exists_and_click(browser, S.xpath_button_autorization)

    logger.info('# смотрим результат')
    time.sleep(3)

    n = 1

    for i in range(n):

        logger.info('# заходим на страницу создания разового пропуска')
        Base.element_exists_and_click(browser, S.xpath_raz_propusk_RP)

        ##############################################################################################
        logger.info('# Заполняем вкладку "Документ постетителя"')

        logger.info('# заполняем ФИО')
        Base.element_exists_and_send(browser, S.xpath_last_name_RP, D.last_name_RP)
        Base.element_exists_and_send(browser, S.xpath_first_name_RP, D.first_name_RP)
        Base.element_exists_and_send(browser, S.xpath_middle_name_RP, str(i+1))

        logger.info('# вписываем срок действия пропуска с и по, предвартельно очистив значения полей')
        browser.find_element_by_xpath(S.xpath_beginning_validity_period_RP).clear()
        Base.element_exists_and_send(browser, S.xpath_beginning_validity_period_RP, D.beginning_validity_period_RP)
        browser.find_element_by_xpath(S.xpath_expiration_validity_period_RP).clear()
        Base.element_exists_and_send(browser, S.xpath_expiration_validity_period_RP, D.expiration_validity_period_RP)

        logger.info('# устанавливаем количество пропусков')
        browser.find_element_by_xpath(S.xpath_count_RP).clear()
        Base.element_exists_and_send(browser, S.xpath_count_RP, D.count_RP)


        ################## !!!!!!!!!!!!!!
        logger.info('# выбираем из списка ФИО принимающей стороны')
        browser.find_element_by_xpath(S.xpath_FIO_host_party_RP).clear()
        Base.drop_down_element_click(browser, S.xpath_FIO_host_party_RP, D.FIO_host_party_RP)
        Base.uploading_file(browser, S.xpath_FIO_host_party_RP, D.FIO_host_party_RP)
        Base.element_exists_and_click(browser, S.xpath_FIO_number_in_list_host_party_RP)
   
        time.sleep(3) 

        logger.info('# coхраняем заявку')
        Base.element_exists_and_click(browser, S.xpath_button_save)

        
        # Base.element_exists_and_click(browser, S.xpath_again_create_RP)  # если добавлена дата в отчество, то кнопка не появляется
     
        logger.info('# обязательно здесь time.sleep(), иначе заявка не сохраняется')
        time.sleep(9) 

        logger.info('# ЗАВЕРШИЛИ ПОЗИТИВНЫЙ СМОУК-ТЕСТ НА СОЗДАНИЕ ЗАЯВКИ НА РАЗОВЫЙ ПРОПУСК')
        logger.info('****************************************************************************')

