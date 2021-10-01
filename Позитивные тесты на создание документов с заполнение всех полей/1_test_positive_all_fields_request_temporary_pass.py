import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
sys.path.append("../Test1/")
path.insert(0, /Users/zhuravlev/source/repos/Test1)
from base_page import BasePage as Base
from selectors import Selectorss as S
from data import Data as D


  
def __init__(self, browser):
    self.browser = browser
      
def test_all_fields_request_temporary_pass(browser):
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

    # заполняем название организации (в какую пришёл посетитель)
    Base.element_exists_and_send(browser, S.xpath_firm_value, D.firm_value)

    # заполняем дату рождения посетителя
    Base.element_exists_and_send(browser, S.xpath_birthday, D.visitor_birthday)

    # ставим отметку, что он иностранный гражданин
    Base.element_exists_and_click(browser, S.xpath_foreign_person_chekbox)

    # вводим e-mail посетителя
    Base.element_exists_and_send(browser, S.xpath_visitor_email, D.visitor_email)

    # выбираем префикс номера телефона
    Base.drop_down_element_click(browser, S.xpath_code_country_drop_down_list, D.code_country_prefix_text)
    # вписываем номер телефона посетителя
    Base.element_exists_and_send(browser, S.xpath_number_mobile_phone, D.number_mobile_phone)

    # вписываем срок действия пропуска с и по, предвартельно очистив значения полей
    browser.find_element_by_xpath(S.xpath_beginning_validity_period).clear()
    Base.element_exists_and_send(browser, S.xpath_beginning_validity_period, D.beginning_validity_period)
    browser.find_element_by_xpath(S.xpath_expiration_validity_period).clear()
    Base.element_exists_and_send(browser, S.xpath_expiration_validity_period, D.expiration_validity_period)

    # вносим цель посещения
    Base.element_exists_and_send(browser, S.xpath_purpose_visit, D.purpose_visit)

    ################## !!!!!!!!!!!!!!

    # выбираем из списка ФИО принимающей стороны
    browser.find_element_by_xpath(S.xpath_FIO_host_party).clear()
    Base.drop_down_element_click(browser, S.xpath_FIO_host_party, D.FIO_host_party)
    Base.uploading_file(browser, S.xpath_FIO_host_party, D.FIO_host_party)
    Base.element_exists_and_click(browser, S.xpath_FIO_number_in_list_host_party)

    # указываем адрес из списка "Адрес*:"
    browser.find_element_by_xpath(S.xpath_host_party_address).clear()
    Base.drop_down_element_click(browser, S.xpath_host_party_address, D.host_party_address)
    Base.uploading_file(browser, S.xpath_host_party_address, D.host_party_address)
    Base.element_exists_and_click(browser, S.xpath_number_in_list_host_party_address)
  

    time.sleep(1)

    # указываем комнату посещения (поле "Комната:")
    Base.element_exists_and_send(browser, S.xpath_host_room, D.host_room)

    # указываем номер телефона принимающей стороны (полк "Телефон:")
    Base.element_exists_and_send(browser, S.xpath_host_phone, D.host_phone)
    
    # подгружаем файл - скан документа (jpg или png, dox, xls, pdf)
    Base.uploading_file(browser, S.xpath_input_file, D.file_path)
    
    time.sleep(5) 
    ##############################################################################################
    # ПЕРЕХОДИМ НА ВКЛАДКУ "ДОКУМЕНТ ПОСЕТИТЕЛЯ"
    Base.element_exists_and_click(browser, S.xpath_users_document)

    # выбираем тип документа
    Base.drop_down_element_click(browser, S.xpath_document_type, D.document_type)

    # указываем серию документа
    Base.element_exists_and_send(browser, S.xpath_document_series, D.document_series)

    time.sleep(1)
    # указываем номер документа
    Base.element_exists_and_click(browser, S.xpath_document_number)
    Base.element_exists_and_send(browser, S.xpath_document_number, D.document_number)

    # указываем, кем выдан документ
    Base.element_exists_and_send(browser, S.xpath_document_authority, D.document_authority)

    # указываем код документа
    Base.element_exists_and_send(browser, S.xpath_document_code, D.document_code)

    # записываем дату выдачи документа
    browser.find_element_by_xpath(S.xpath_document_date).clear()
    Base.element_exists_and_send(browser, S.xpath_document_date, D.document_date)

    # указываем место регистрации
    Base.element_exists_and_send(browser, S.xpath_place_of_registration, D.place_of_registration)
    
    time.sleep(5) 
    ##############################################################################################
    # ПЕРЕХОДИМ НА ВКЛАДКУ "МАТЕРИАЛЬНЫЕ ЦЕННОСТИ"
    Base.element_exists_and_click(browser, S.xpath_wealth)
    
    # устанавливаем чек-бокс "на внос"
    Base.element_exists_and_click(browser, S.xpath_checkbox_move_in)

    # устанавливаем чек-бокс "на вынос"
    Base.element_exists_and_click(browser, S.xpath_checkbox_move_out)

    # записываем документ на материальные ценности
    Base.element_exists_and_send(browser, S.xpath_document_of_wealth, D.document_of_wealth)

    # указываем модель материальных ценностей
    Base.element_exists_and_send(browser, S.xpath_wealth_model, D.wealth_model)

    # указываем серийный номер материальных ценностей
    Base.element_exists_and_send(browser, S.xpath_wealth_serial_number, D.wealth_serial_number)

    # указываем количество материальных ценностей
    browser.find_element_by_xpath(S.xpath_wealth_count).clear()
    Base.element_exists_and_send(browser, S.xpath_wealth_count, D.wealth_count)

    # выбираем единицы измерения количества материальных ценностей
    browser.find_element_by_xpath(S.xpath_wealth_unit).clear()
    Base.drop_down_element_click(browser, S.xpath_wealth_unit, D.wealth_unit)
    Base.uploading_file(browser, S.xpath_wealth_unit, D.wealth_unit)
    Base.element_exists_and_click(browser, S.xpath_wealt_unit_number)

    # кликаем на кнопку "ДОБАВИТЬ"
    Base.element_exists_and_click(browser, S.xpath_wealth_add)

    time.sleep(5) 
    ##############################################################################################
    # ПЕРЕХОДИМ НА ВКЛАДКУ "АВТОМОБИЛЬ"
    Base.element_exists_and_click(browser, S.xpath_car)

    # указываем номер автомобиля
    Base.element_exists_and_click(browser, S.xpath_car_number)
    Base.element_exists_and_send(browser, S.xpath_car_number, D.car_number)

    # выбираем марку автомобиля
    browser.find_element_by_xpath(S.xpath_car_brand).clear()
    Base.drop_down_element_click(browser, S.xpath_car_brand, D.car_brand)
    Base.uploading_file(browser, S.xpath_car_brand, D.car_brand)
    Base.element_exists_and_click(browser, S.xpath_car_brand_in_list)

    # указываем цвет автомобиля
    Base.element_exists_and_send(browser, S.xpath_car_color, D.car_color)

    # устанавливаем чек-бокс "Оставить на ночь"
    Base.element_exists_and_click(browser, S.xpath_checkbox_night_car)

    # устанавливаем чек-бокс "Разрешение на разгрузку автомобиля"
    Base.element_exists_and_click(browser, S.xpath_checkbox_permission_unload_car)

    # выбираем парковочное место
    browser.find_element_by_xpath(S.xpath_parking_place).clear()
    Base.drop_down_element_click(browser, S.xpath_parking_place, D.parking_place)
    Base.uploading_file(browser, S.xpath_parking_place, D.parking_place)
    Base.element_exists_and_click(browser, S.xpath_parking_place_in_list)

    # coхраняем заявку
    Base.element_exists_and_click(browser, S.xpath_button_save) 
    # обязательно здесь time.sleep(), иначе заявка не сохраняется  
    time.sleep(7) 
