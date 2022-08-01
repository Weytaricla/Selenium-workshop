#Подключаем всё необходимое для работы
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Выносим используемую ссылку в отдельную переменную для удобства
link = "https://digexco.ru/home"


# фикстура для открытия и закрытия браузера. Такой способ позволяет сильно сократить количества кода в тестах.
@pytest.fixture
def browser():
    # этот код выполнится перед началом кода теста
    print("\nstart browser for test..")
    # инициализация драйвера
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()

def test_form_correct(browser):
    browser.get(link)
    # пжидание каждого элемента до 5 секунд
    browser.implicitly_wait(5)

    button = browser.find_element(By.LINK_TEXT, "Контакты")
    button.click()

    textarea_name = browser.find_element(By.NAME, "Name")
    textarea_name.send_keys("Maxim")

    textarea_email = browser.find_element(By.NAME, "Email")
    textarea_email.send_keys("example@ex.com")

    textarea_phone = browser.find_element(By.CLASS_NAME, "t-input-phonemask")
    textarea_phone.send_keys("9998887766")

    textarea_comment = browser.find_element(By.NAME, "Ваш комментарий по желанию")
    textarea_comment.send_keys("Тестовое сообщение!")

    checkbox = browser.find_element(By.CLASS_NAME, "t-checkbox__indicator")
    checkbox.click()

    button = browser.find_element(By.CLASS_NAME, "t-submit")
    button.click()

    # time.sleep(2)

    popup = browser.find_element(By.ID, "tildaformsuccesspopuptext")
    popup_text = popup.text

    # time.sleep(10)

    # команда для сравнения переменной 
    assert popup_text == "Спасибо данные успешно отправлены!", "Incorrect text"

    # time.sleep(2)

    # browser.quit()