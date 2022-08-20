from BaseAppSaucedemo import BasePage
from selenium.webdriver.common.by import By

# На этой странице описаны методы для работы со страницами
# Локаторы - по ним мы будем искать элементы
class SeacrhLocators:
    LOCATOR_USERNAME = (By.ID, "user-name")
    LOCATOR_PASSWORD = (By.ID, "password")
    LOCATOR_LOGIN_BUTTON = (By.ID, "login-button")
    LOCATOR_POPUP = (By.CSS_SELECTOR, ".error > h3")

# Здесь описаны методы для работы с формой

class FormFiller(BasePage):

    def enter_login(self, word):
        search_field = self.find_element(SeacrhLocators.LOCATOR_USERNAME)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def enter_password(self, word):
        search_field = self.find_element(SeacrhLocators.LOCATOR_PASSWORD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_login_button(self):
        return self.find_element(SeacrhLocators.LOCATOR_LOGIN_BUTTON,time=2).click()

    def check_submit_text(self):
        popup = self.find_element(SeacrhLocators.LOCATOR_POPUP,time=2)
        popup_text = popup.text
        return popup_text