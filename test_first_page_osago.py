import pytest
from pages.first_step import FirstStepPage
import time

link = "https://b2c.pampadu.ru/index.html#49a973bd-2d7c-4b9b-9c28-d986d7757983"

'''Ввод валиданого гос.номера, в конце убедиться, что переход на следующий шаг произведен'''
def test_input_valid_state_number_positive(browser):
    global link #Интереса ради, чтобы в каждом
    # тесте не дублировать переменную link, можно сделать из link фикстуру и реализовать передачу параметров в фикстуру
    page = FirstStepPage(browser,link)
    page.open()
    page.input_valid_all_state_number()
    page.click_on_button_continue()
    page.should_be_second_step()

'''Валидация пустого поля гос.номера'''
def test_click_button_continue_with_empty_state_number(browser):
    global link
    page = FirstStepPage(browser,link)
    page.open()
    page.should_be_empty_state_number()
    page.click_on_button_continue()
    page.should_be_red_state_number()
    time.sleep(3)

'''Переход на ручной ввод марки и модели автомобиля при нажатии на ссылку "Не помню, не получал"'''
def test_click_on_link_i_dont_remember(browser):
    global link
    page = FirstStepPage(browser, link)
    page.open()
    page.click_on_link_i_dont_remember()
    page.should_be_step_after_click_on_i_dont_remember()

'''Ввод несущестующего региона, в конце убедиться, что пользователь переведен на ручной ввод марки и модели 
автомобиля '''
def test_input_nonexistent_code_region(browser):
    global link
    page = FirstStepPage(browser, link)
    page.open()
    page.input_valid_state_number()
    page.input_no_valid_region_code()
    page.click_on_button_continue()
    page.should_be_step_after_input_no_valid_code_region()
