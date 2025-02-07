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
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
    
    def test_guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented, but should be"
    
    def test_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success didn't, but should"