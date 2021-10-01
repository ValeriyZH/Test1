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

    logger.info('# Записываем дату и время начала теста: ' + str(datetime.datetime.today().strftime('%d.%m.%Y')))
    logger.info('# устанавливаем имя файла для логирования')
    Base.logging_file(D.log_file_name)
    

    logger.info('# ЗАПУСТИЛИ ПОЗИТИВНЫЙ СМОУК-ТЕСТ НА СОЗДАНИЕ ПРОПУСКА ПО ЗАЯВКЕ НА РАЗОВЫЙ ПРОПУСК')

    logger.info('# установили нужный размер окна браузера')
    browser.set_window_size (D.windows_width, D.windows_high)

    logger.info('# заходим на страницу регистрации в VISITORCONTROL')
    browser.get(D.url_autorization_RP)

    logger.info('# логинимся')
    Base.element_exists_and_send(browser, S.xpath_input_login, D.login_user_RP)
    Base.element_exists_and_send(browser, S.xpath_input_password, D.password_user_RP)
    Base.element_exists_and_click(browser, S.xpath_button_autorization)

    #Base.element_exists_and_click(browser, S.xpath_in_system_go)

    logger.info('# смотрим результат')
    time.sleep(3)

    n = 250

    logger.info('# заходим в раздел "Пропуска"')
    Base.element_exists_and_click(browser, S.xpath_passes)

    for i in range(n):

        logger.info('# заходим на страницу создания пропуска по заявке')
        Base.element_exists_and_click(browser, S.xpath_raz_propusk_by_request)

        ##############################################################################################
        logger.info('# Заполняем вкладку "Посетитель"')

        logger.info('# Выбираем фамилию из выпадающего списка фамилий в заявках')
        browser.find_element_by_xpath(S.xpath_last_name_in_reguest).clear()
        logger.info('# 1')
        Base.element_exists_and_send(browser, S.xpath_last_name_in_reguest, D.last_name_in_request)
        logger.info('# 2')
        Base.element_exists_and_click(browser, S.xpath_fio_in_list_request)
        logger.info('# 3')
        
        
        #Base.element_exists_and_send(browser, S.xpath_first_name_in_reguest, D.first_name_in_request)
        #Base.element_exists_and_send(browser, S.xpath_middle_name_in_reguest, D.middle_name_in_request)

        
        logger.info('# Открываем список свободных карт доступа')
        Base.element_exists_and_click(browser, S.xpath_free_card_list)

        logger.info('# Кликаем первую свободную карту')
        Base.element_exists_and_click(browser, S.xpath_first_free_card)

        logger.info('# Выбираем эту карту')
        Base.element_exists_and_click(browser, S.xpath_select_first_free_card)
   
        time.sleep(3) 

        logger.info('# coхраняем пропуск')
        Base.element_exists_and_click(browser, S.xpath_save_RP)
     
        logger.info('# обязательно здесь time.sleep(), иначе пропуск не сохраняется')
        time.sleep(9) 

        logger.info('# закрываем окно с пропуском')
        Base.element_exists_and_click(browser, S.xpath_close_window_RP)

        logger.info('# открываем все пропуска')
        Base.element_exists_and_click(browser, S.xpath_all_pass)

        logger.info('# выбираем только что созданный пропуск')
        Base.element_exists_and_click(browser, S.xpath_this_pass)

        logger.info('# кликаем кнопку "Внести отметку" ("Время сдачи пропуска")')
        Base.element_exists_and_click(browser, S.xpath_pass_delivery_button)

        logger.info('# кликаем кнопку "Ок" ("Отметка о выходе из здания внесена!")')
        Base.element_exists_and_click(browser, S.xpath_ok_button_mark_made)


        logger.info('# ЗАВЕРШИЛИ ПОЗИТИВНЫЙ СМОУК-ТЕСТ НА СОЗДАНИЕ РАЗОВОГО ПРОПУСКА ПО ЗАЯВКЕ')
        logger.info('****************************************************************************')

