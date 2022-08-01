import pytest
from selenium import webdriver

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