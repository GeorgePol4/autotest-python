from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRODUCT_NAME_ADDED = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    PRICE_BUSKET = (By.CSS_SELECTOR, ".alertinner p strong")