from selenium.common.exceptions import NoSuchElementException #импорт эксшепшена
class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    
    def open(self):
        self.browser.get(self.url)
    
    def is_element_present(self, how, selector): #задаем переменные, которые будут переданы в тесте, в методе приписываем возврат True или False в зависимости от exeption
        try:
            self.browser.find_element(how, selector)
        except (NoSuchElementException):
            return False
        return True