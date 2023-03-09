from base_page import BasePage
from locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_not_be_success_product_name(self):
        pass

    def should_not_be_success_message(self):
        pass

    def add_to_shopping_cart(self):
        pass

    def should_disappear_success_message(self):
        pass

  
