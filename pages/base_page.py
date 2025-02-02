from selenium.common.exceptions import NoSuchElementException #импорт эксшепшена
from selenium.common.exceptions import NoAlertPresentException
import math
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
    
    def solve_quiz_and_get_code(self): #метод для задания 4.3_2
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")