from SaucedemoPages import FormFiller

def test_form_positive(browser):
    login_page = FormFiller(browser)
    login_page.go_to_site()
    login_page.enter_login("standard_user")
    login_page.enter_password("secret_sauc")
    login_page.click_on_the_login_button()
    popup_text = login_page.check_submit_text()
    assert popup_text == "Epic sadface: Username and password do not match any user in this service", "Incorrect text"

def test_form_negative(browser):
    login_page = FormFiller(browser)
    login_page.go_to_site()
    login_page.enter_login("standard_user")
    login_page.enter_password("invalid_pass")
    login_page.click_on_the_login_button()
    popup_text = login_page.check_submit_text()
    assert popup_text == "Epic sadface: Username and password do not match any user in this service", "Incorrect text"

def test_form_empty(browser):
    login_page = FormFiller(browser)
    login_page.go_to_site()
    login_page.enter_login("")
    login_page.enter_password("")
    login_page.click_on_the_login_button()
    popup_text = login_page.check_submit_text()
    assert popup_text == "Epic sadface: Username is required!", "Incorrect text"