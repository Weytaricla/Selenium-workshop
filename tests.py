from DigexPages import FormFiller

# Пользовательский сценарий

def test_form(browser):
    contacts_page = FormFiller(browser)
    contacts_page.go_to_site()
    contacts_page.enter_name("Maxim")
    contacts_page.enter_email("example@ex.com")
    contacts_page.enter_phone("9998887766")
    contacts_page.enter_comment("Тестовое сообщение!")
    contacts_page.click_on_the_checkbox()
    contacts_page.click_on_the_submit_button()
    popup_text = contacts_page.check_submit_text()
    assert popup_text == "Спасибо данные успешно отправлены!", "Incorrect text"