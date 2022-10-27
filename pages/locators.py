from selenium.webdriver.common.by import By


class FirstStepLocators():
    INPUT_STATE_NUMBER = (By.CSS_SELECTOR, 'input.gos-input-main')
    INPUT_REGION_CODE = (By.CSS_SELECTOR, 'input.gos-input-region')
    BUTTON_CONTINUE = (By.CSS_SELECTOR, 'button[data-test="left-side-gos-sign-continue"]')
    GOS_SIGN_LINK =  (By.CSS_SELECTOR, 'span.gos-sign-link')
    INPUT_COLOR_STATE_NUM = (By.CSS_SELECTOR, 'div.gos-input[style="background-color: rgb(254, 212, 203);"]')

class SecondStepLocators():
    CAR_BRAND = (By.XPATH,'//div[@class="ppdw-stepper-body"]//label[contains(text(), "Марка автомобиля")]')
    ID_VOLKSWAGEN = (By.XPATH, '//div[@class="flex ppdw-element xs100 sm50"]// input[@value="69"] | label[contains(text(), "Марка автомобиля")]')
    CAR_MODEL = (By.XPATH, '//div//label[contains(text(), "Модель автомобиля")]')
    ID_TOUAREG = (By.XPATH, '//div[@class="flex ppdw-element xs100 sm50"]// input[@value="1277"] | label[contains(text(), "Модель автомобиля")]')
class DataForPages():
    STATE_NUMBER_VALID = 'А123АА'
    REGION_CODE_VALID = '123'
    STATE_NUMBER_NO_VALID = 'Д123ЙГ'
    REGION_CODE_NO_VALID = '000'

class ManualSelectionCarLocators():
    ALERT_LIMIT = (By.XPATH, '//div[@class = "rate-limit mb-2"]/div[contains(text(),"Превышено максимальное кол-во запросов")]')