from pages.base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_product_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_product_button.click()

    def show_product_name_and_basket_price(self):
        item = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADDED)
        print(f"{item.text} in the basket")
        price = self.browser.find_element(*ProductPageLocators.PRICE_BUSKET)
        print(f"{price.text} total cost")