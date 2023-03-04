from selenium.webdriver.common.by import By
#from .locators import MainPageLocators

from base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link")
        #login_link.click()



    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link")

