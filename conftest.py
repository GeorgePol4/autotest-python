import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Choose language") #парсим язык из строки терминала, задаем английский в качестве деыолтного 

@pytest.fixture(scope="function")
def browser(request): #открываем браузер с выбранными опциями
    print("\nstart browser for test..")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = options)
    yield browser
    print("\nquit browser..")
    browser.quit()
