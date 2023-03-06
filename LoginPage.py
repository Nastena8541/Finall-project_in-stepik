from selenium.webdriver.common.by import By

from main_page import MainPage
from base_page import BasePage



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(By.CSS_SELECTOR, "LOGIN_FORM"), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(By.CSS_SELECTOR, "REGISTER_FORM"), "Register form is not presented"
        assert True

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()