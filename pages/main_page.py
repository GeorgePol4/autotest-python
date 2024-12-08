from pages.base_page import BasePage #импортируем методы класса 
from selenium.webdriver.common.by import By

class MainPage(BasePage): #наследуем методы класса BasePage для нового класса

    def go_to_login_page(self): #ищем и кликаем на ссылки логина 
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self): #пока неправильно ищем ссылку 
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"
