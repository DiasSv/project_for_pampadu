import time
import pytest

from .base_page import BasePage
from .locators import FirstStepLocators
from .locators import DataForPages
from .locators import SecondStepLocators
from .locators import ManualSelectionCarLocators


class FirstStepPage(BasePage):

    def input_valid_all_state_number(self):
        self.input_valid_state_number()
        self.input_valid_region_code()

    def input_no_valid_all_state_number(self):
        self.input_no_valid_state_number()
        self.input_no_valid_region_code()

    def input_valid_state_number(self):
        self.wait_to_be_clickable(*FirstStepLocators.INPUT_STATE_NUMBER)
        state_num = self.browser.find_element(*FirstStepLocators.INPUT_STATE_NUMBER)
        state_num.click()
        state_num.clear()
        state_num.send_keys(*DataForPages.STATE_NUMBER_VALID)

    def input_no_valid_state_number(self):
        self.wait_to_be_clickable(*FirstStepLocators.INPUT_STATE_NUMBER)
        state_num = self.browser.find_element(*FirstStepLocators.INPUT_STATE_NUMBER)
        state_num.click()
        state_num.clear()
        state_num.send_keys(*DataForPages.STATE_NUMBER_NO_VALID)

    def input_valid_region_code(self):
        self.wait_to_be_clickable(*FirstStepLocators.INPUT_REGION_CODE)
        code_reg = self.browser.find_element(*FirstStepLocators.INPUT_REGION_CODE)
        code_reg.click()
        code_reg.clear()
        code_reg.send_keys(*DataForPages.REGION_CODE_VALID)

    def input_no_valid_region_code(self):
        self.wait_to_be_clickable(*FirstStepLocators.INPUT_REGION_CODE)
        code_reg = self.browser.find_element(*FirstStepLocators.INPUT_REGION_CODE)
        code_reg.click()
        code_reg.clear()
        code_reg.send_keys(*DataForPages.REGION_CODE_NO_VALID)



    def click_on_button_continue(self):
        self.wait_to_be_clickable(*FirstStepLocators.BUTTON_CONTINUE)
        self.browser.find_element(*FirstStepLocators.BUTTON_CONTINUE).click()

    def should_be_empty_state_number(self):
        self.wait_to_be_clickable(*FirstStepLocators.INPUT_STATE_NUMBER)
        state_num = self.browser.find_element(*FirstStepLocators.INPUT_STATE_NUMBER)
        self.wait_to_be_clickable(*FirstStepLocators.INPUT_REGION_CODE)
        region_code = self.browser.find_element(*FirstStepLocators.INPUT_REGION_CODE)
        state_num.click()
        state_num.clear()
        region_code.click()
        region_code.clear()

    def should_be_red_state_number(self):
        element = self.browser.find_element(*FirstStepLocators.INPUT_COLOR_STATE_NUM)
        cur_attr = element.get_attribute('style')
        assert "background-color: rgb(254, 212, 203" in cur_attr, "ATTR STYLE NOT BC RGB(254,212,203)"

    def should_be_second_step(self):
        self.should_be_car_brand()
        self.should_be_car_model()
        self.should_be_id_touareg()
        self.should_be_id_volkswagen()


    def should_be_car_brand(self):
        car_brand = self.browser.find_element(*SecondStepLocators.CAR_BRAND)
        assert "Марка автомобиля" in car_brand.text, "CAR_BRAND NOT 'МАРКА АВТОМОБИЛЯ'"

    def should_be_car_model(self):
        car_model = self.browser.find_element(*SecondStepLocators.CAR_MODEL)
        assert "Модель автомобиля" in car_model.text, "CAR MODEL NOT 'Модель автомобиля'"

    def should_be_id_volkswagen(self):
        id_volkswagen = self.browser.find_element(*SecondStepLocators.ID_VOLKSWAGEN)
        assert "69" == id_volkswagen.get_attribute('value'), "it is not volkswagen!!!"


    def should_be_id_touareg(self):
        id_touareg = self.browser.find_element(*SecondStepLocators.ID_TOUAREG)
        assert "1277" == id_touareg.get_attribute('value'), "it is not touareg!!!"

    def click_on_link_i_dont_remember(self):
        self.wait_to_be_clickable(*FirstStepLocators.GOS_SIGN_LINK)
        self.click_actions(*FirstStepLocators.GOS_SIGN_LINK)

    def should_be_step_after_click_on_i_dont_remember(self):
        self.should_be_car_brand()
        self.should_be_car_model()

    def should_be_step_after_input_no_valid_code_region(self):
        self.should_be_alert_limit()
        self.should_be_car_brand()
        self.should_be_car_model()

    def should_be_alert_limit(self):
        alert = self.browser.find_element(*ManualSelectionCarLocators.ALERT_LIMIT)
        assert "Превышено максимальное кол-во запросов" in alert.text, "the text does not match"





