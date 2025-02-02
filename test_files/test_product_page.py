from pages.product_page import ProductPage
import pytest

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_product_to_basket()

def test_add_product_to_basket_and_see_name_and_price(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.show_product_name_and_basket_price()

@pytest.mark.parametrize('promo_num', [n for n in range(10)])
def test_guest_can_add_product_to_basket_params(browser, promo_num):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_num}"
    print(link)
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    #требуется проверка совпадения названия продукта, стоимости и того, что в алерте после добавления, добавить в product_page стадии проверки в метод добавления в корзину 