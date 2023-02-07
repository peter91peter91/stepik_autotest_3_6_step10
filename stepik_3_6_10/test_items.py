#ЗАПУСК    pytest --language=es test_items.py
#Пожалуйста,проверьте, что у вас нет своего conftest.py в директории выше.

import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
def test_find_add_to_card_btn(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(7)  #ждем 7 секунд ,чтобы Вы убедились, что язык на странице соответствует требуемому Вами

    #проверяем в течение 30 секунд, что на странице для нажатия стала доступна кнопка добавления товара в корзину. Если недоступна, то сработает ASSERT
    assert WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-add-to-basket"))) is not None,\
        'Кнопка добавления товара в корзину отсутствует!'
