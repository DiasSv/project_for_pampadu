from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options  # Возможность передать браузеру язык

from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

import time
import math
import pytest


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help='choose browser: chrome of firefox')  # Мы добавили опцию , которая отвечает за выбор браузера
    parser.addoption('--language', action='store', default='en',
                     help='choose language en, ru ... etc')  # А эта опция отвечает за выбор языка


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\n start chrome browser test suite")
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl accept_languages", user_language)
        print("\n Start firefox browser test suite")
        browser = webdriver.Firefox(firefox_profile=fp, executable_path=GeckoDriverManager().install())
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\n browser quit")
    browser.quit()
