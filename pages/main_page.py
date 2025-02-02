from pages.base_page import BasePage #импортируем методы класса 
from .locators import MainPageLocators

class MainPage(BasePage): #наследуем методы класса BasePage для нового класса

    def go_to_login_page(self): #ищем и кликаем на ссылки логина 
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self): 
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
