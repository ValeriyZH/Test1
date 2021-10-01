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
    
    logger.info('# ЗАПУСТИЛИ ПОЗИТИВНЫЙ СМОУК-ТЕСТ НА СОЗДАНИЕ ЗАЯВКИ НА МАТЕРИАЛЬНЫЙ ПРОПУСК')


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

    logger.info('# заходим на страницу создания заявки на материальный пропуск')
    Base.element_exists_and_click(browser, S.xpath_material_propusk)

    logger.info('# заполняем ФИО')
    Base.element_exists_and_send(browser, S.xpath_last_name, D.last_name)
    Base.element_exists_and_send(browser, S.xpath_first_name, D.first_name)
    Base.element_exists_and_send(browser, S.xpath_middle_name, D.middle_name)

    logger.info('# смотрим результат')
    time.sleep(5)
    
    logger.info('# ставим отметку "Внос"')
    Base.element_exists_and_click(browser, S.xpath_material_propusk_check_box_vnos)

    logger.info('# ставим отметку "Вынос"')
    Base.element_exists_and_click(browser, S.xpath_material_propusk_chek_box_vynos)

    logger.info('# заполняем наименование материальной ценности')
    Base.element_exists_and_send(browser, S.xpath_document_of_wealth, D.wealth_model)

    logger.info('# указываем количество материальных ценностей')
    browser.find_element_by_xpath(S.xpath_wealth_count).clear()
    Base.element_exists_and_send(browser, S.xpath_wealth_count, D.wealth_count)

    logger.info('# выбираем единицы измерения количества материальных ценностей')
    browser.find_element_by_xpath(S.xpath_wealth_unit).clear()
    Base.drop_down_element_click(browser, S.xpath_wealth_unit, D.wealth_unit)
    Base.uploading_file(browser, S.xpath_wealth_unit, D.wealth_unit)
    Base.element_exists_and_click(browser, S.xpath_wealth_unit_number_in_list)

    logger.info('# кликаем на кнопку "ДОБАВИТЬ"')
    Base.element_exists_and_click(browser, S.xpath_wealth_add)

    logger.info('# вписываем дату действия пропуска') 
    browser.find_element_by_xpath(S.xpath_date_material_propusk).clear()
    Base.element_exists_and_send(browser, S.xpath_date_material_propusk, D.beginning_validity_period)

    logger.info('# coхраняем заявку')
    Base.element_exists_and_click(browser, S.xpath_button_save) 
    logger.info('# обязательно здесь time.sleep(), иначе заявка не сохраняется')  
    time.sleep(7) 

    logger.info('# ЗАВЕРШИЛИ ПОЗИТИВНЫЙ СМОУК-ТЕСТ НА СОЗДАНИЕ ЗАЯВКИ НА МАТЕРИАЛЬНЫЙ ПРОПУСК')
    logger.info('****************************************************************************')

    