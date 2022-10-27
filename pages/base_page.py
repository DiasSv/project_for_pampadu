from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import pytest


class BasePage():
    """Мы создаем конструктор, в котором передаются тело
    браузера и ссылка для дальнейшего использования"""

    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    '''Функция отвечает за универсальную проверку наличия элемента на странице Возращает булево значение'''

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    '''Функция отвечает за проверку отсутствия элемента на странице, функция ждет, пока элемент не пропадет'''

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    '''Ожидание подходящего URL / проверка url'''

    def is_url_present(self, timeout=4):
        changed_url = "https://app.clockify.me/en/login"
        try:
            WebDriverWait(self.browser, timeout).until(EC.url_changes(changed_url))
        except TimeoutException:
            return False

        return True

    '''Получение заголовка страницы'''

    def is_title_correct(self, title, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.title_contains(title))
        except TimeoutException:
            return False

        return True

    '''Функция имитирует клик мыши по указанному элементу '''

    def click_actions(self, how, what, hold_seconds=0):
        element = self.browser.find_element(how, what)
        action = ActionChains(self.browser)
        action.move_to_element(element). \
            pause(hold_seconds).click().perform()

        '''Ожидание элемента  + проверка на кликабельность'''

    def wait_to_be_clickable(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout). \
                until(EC.element_to_be_clickable((how, what)))
        except:
            print('Element not clickable!')  # можно импортировать пакет colored и расскрашивать ошибки,
            # чтобы в отчете становились еще заметнее
            return False
        return True

    '''Возвращает на предыдущую стр. Работает как Backspace'''

    def go_back(self):
        self._web_driver.back()

    '''Обновляет страницу'''

    def refresh(self):
        self._web_driver.refresh()

    """Выполняет комплексные действия перед тем, ввести данные в поле"""




