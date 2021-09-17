import pathlib
from pathlib import Path
import datetime

class Data:
   
    path_webdriver = Path('C:', 'Users', 'zhuravlev', 'source', 'repos')
    url_autorization = 'http://vsrv-ins-kf:8559/'

    login_user = 'admin'
    password_user = '111111'

    windows_width = 1920
    windows_high = 1080

    ############################################################################################
    # Для страницы "Временный пропуск"

    last_name = 'Автотестеров  ' + str(datetime.datetime.today())
    first_name = 'Автотестер  ' + str(datetime.datetime.today())
    middle_name = 'Автотесторович' + str(datetime.datetime.today())
    element_text =  'Organization'
    firm_value = 'ООО "Автотестирование"'

    visitor_birthday = '16.11.1973'
    visitor_email = 'autotester@autotest.ru'

    code_country_prefix_text = 'Иностранный'
    number_mobile_phone = '79099073250'

    beginning_validity_period = datetime.datetime.today().strftime('%d.%m.%Y')
    expiration_validity_period = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%d.%m.%Y')

    purpose_visit = 'Автотестирование системы VISITORCONTROL'

    file_path = r'C:\Users\zhuravlev\Pictures\123.jpg'

    FIO_host_party = 'Иванов Иван'
    host_party_address = 'Домодедово, к. 2'

    host_room = 'Палата №6'
    host_phone = '+79099073250'

    document_type = 'Иностранный паспорт'
    document_series = 'XXX'
    document_number = '77777777'
    document_authority = 'Выдано Императором Вселенной с большого бодуна и по ошибке'
    document_code = 'Код Да Винчи'
    document_date = '25.07.1980'
    place_of_registration = "Шалаш под пальмой в Занзибаре"

    document_of_wealth = "Филькина грамота, выданная Филькой Фильковичем"
    wealth_model = 'Мешок золота'
    wealth_serial_number = 'XGGHGG7897867656786'
    wealth_count = '100'
    wealth_unit = 'шт.'
   
    car_number = str(datetime.datetime.today())
    car_brand = 'Alfa Romeo'
    car_color = 'серо-буро-малиновый'
    parking_place = 'Парковка 2'

    ############################################################################################
    # Для страницы " "



    '''
    url_home_avito = 'https://avito.ru'
    url_autorization = 'https://www.avito.ru/#login'
    url_users_profile = 'https://www.avito.ru/profile'
    url_google_autorization = 'https://www.google.com/intl/ru/gmail/about/'
    
    element_text = 'Телефоны'
    message_input = 'OnePlus 8'
    
    password_user_google = 'Tester20212021'
    '''
   