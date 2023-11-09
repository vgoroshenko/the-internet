from pages.locators import InputsLocators, BasePageLocators
from pages.base.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class Inputs(BasePage):

    def go_to_page(self):
        link = self.browser.find_element(*InputsLocators.LOADED_PAGE)
        link.click()

    def should_be_correct_page(self):
        text = self.get_text(*BasePageLocators.PAGE_NAME)
        correct_text = 'Inputs'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def click_input(self):
        number_input = self.browser.find_element(*InputsLocators.INPUT)
        number_input.click()

    def press_up(self, time=1):
        number_input = self.browser.find_element(*InputsLocators.INPUT)
        for i in range(time):
            number_input.send_keys(Keys.UP)

    def press_down(self, time=1):
        number_input = self.browser.find_element(*InputsLocators.INPUT)
        for i in range(time):
            number_input.send_keys(Keys.DOWN)

    def should_be_present_number(self, num):
        number_input = self.browser.find_element(*InputsLocators.INPUT)
        number_input = number_input.get_property("value")
        assert str(num) == number_input, f'should present {num} but present {number_input}'
