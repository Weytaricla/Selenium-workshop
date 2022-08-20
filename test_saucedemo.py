#Подключаем всё необходимое для работы
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Выносим используемую ссылку в отдельную переменную для удобства
link = "https://www.saucedemo.com/"

# фикстура для открытия и закрытия браузера. Такой способ позволяет сильно сократить количества кода в тестах.
@pytest.fixture
def browser():
    # этот код выполнится перед началом кода теста
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()

def test_form_correct(browser):
    browser.get(link)
    browser.implicitly_wait(5)

    # поиск элементов с помощью библиотеки BY
    textarea_name = browser.find_element(By.ID, "user-name")
    textarea_name.send_keys("standard_user")

    textarea_password = browser.find_element(By.ID, "password")
    textarea_password.send_keys("secret_sauc")

    button = browser.find_element(By.ID, "login-button")
    button.click()

    popup = browser.find_element(By.CSS_SELECTOR, ".error > h3")
    popup_text = popup.text

    # команда для сравнения переменной 
    assert popup_text == "Epic sadface: Username and password do not match any user in this service", "Incorrect text"

    browser.quit()