from selenium.webdriver.common.by import By



class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    def register_new_user(self):
        self.browser.find_element(By.CSS_SELECTOR, "registration-email").send_keys("1234@mail.ru")
        self.browser.find_element(By.CSS_SELECTOR, "registration-password1").send_keys("name123")
        self.browser.find_element(By.CSS_SELECTOR, "registration-password2").send_keys("name123")
        self.browser.find_element(By.CSS_SELECTOR, "registration-submit").click()

    def go_to_login_page(self):
        self.browser.find_element(By.CSS_SELECTOR, "login-username").send_keys("1234@mail.ru")
        self.browser.find_element(By.CSS_SELECTOR, "login-password").send_keys("name123")
        self.browser.find_element(By.CSS_SELECTOR, "login_submit").click()

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')






