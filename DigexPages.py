from BaseApp import BasePage
from selenium.webdriver.common.by import By

# На этой странице описаны методы для работы со страницами
# Локаторы - по ним мы будем искать элементы
class SeacrhLocators:
    LOCATOR_NAME = (By.NAME, "Name")
    LOCATOR_EMAIL = (By.NAME, "Email")
    LOCATOR_PHONE = (By.CLASS_NAME, "t-input-phonemask")
    LOCATOR_COMMENT = (By.NAME, "Ваш комментарий по желанию")    
    LOCATOR_CHECKBOX = (By.CLASS_NAME, "t-checkbox__indicator")
    LOCATOR_SUBMIT_BUTTON = (By.CLASS_NAME, "t-submit")
    LOCATOR_POPUP = (By.ID, "tildaformsuccesspopuptext")

# Здесь описаны методы для работы с формой
class FormFiller(BasePage):

    def enter_name(self, word):
        search_field = self.find_element(SeacrhLocators.LOCATOR_NAME)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def enter_email(self, word):
        search_field = self.find_element(SeacrhLocators.LOCATOR_EMAIL)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def enter_phone(self, word):
        search_field = self.find_element(SeacrhLocators.LOCATOR_PHONE)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def enter_comment(self, word):
        search_field = self.find_element(SeacrhLocators.LOCATOR_COMMENT)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_checkbox(self):
        return self.find_element(SeacrhLocators.LOCATOR_CHECKBOX,time=2).click()

    def click_on_the_submit_button(self):
        return self.find_element(SeacrhLocators.LOCATOR_SUBMIT_BUTTON,time=2).click()

    def check_submit_text(self):
        popup = self.find_element(SeacrhLocators.LOCATOR_POPUP,time=2)
        popup_text = popup.text
        return popup_text