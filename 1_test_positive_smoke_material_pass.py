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

    # заходим на страницу создания заявки на материальный пропуск
    Base.element_exists_and_click(browser, S.xpath_material_propusk)

    # заполняем ФИО
    Base.element_exists_and_send(browser, S.xpath_last_name, D.last_name)
    Base.element_exists_and_send(browser, S.xpath_first_name, D.first_name)
    Base.element_exists_and_send(browser, S.xpath_middle_name, D.middle_name)

    # смотрим результат
    time.sleep(5)
    
    # ставим отметку "Внос"
    Base.element_exists_and_click(browser, S.xpath_material_propusk_check_box_vnos)

    # ставим отметку "Вынос"
    Base.element_exists_and_click(browser, S.xpath_material_propusk_chek_box_vynos)

    # заполняем наименование материальной ценности
    Base.element_exists_and_send(browser, S.xpath_document_of_wealth, D.wealth_model)

    # указываем количество материальных ценностей
    browser.find_element_by_xpath(S.xpath_wealth_count).clear()
    Base.element_exists_and_send(browser, S.xpath_wealth_count, D.wealth_count)

    # выбираем единицы измерения количества материальных ценностей
    browser.find_element_by_xpath(S.xpath_wealth_unit).clear()
    Base.drop_down_element_click(browser, S.xpath_wealth_unit, D.wealth_unit)
    Base.uploading_file(browser, S.xpath_wealth_unit, D.wealth_unit)
    Base.element_exists_and_click(browser, S.xpath_wealth_unit_number_in_list)

    # кликаем на кнопку "ДОБАВИТЬ"
    Base.element_exists_and_click(browser, S.xpath_wealth_add)

    # вписываем дату действия пропуска 
    browser.find_element_by_xpath(S.xpath_date_material_propusk).clear()
    Base.element_exists_and_send(browser, S.xpath_date_material_propusk, D.beginning_validity_period)

    # coхраняем заявку
    Base.element_exists_and_click(browser, S.xpath_button_save) 
    # обязательно здесь time.sleep(), иначе заявка не сохраняется  
    time.sleep(7) 

    