from .locators import DynamicallyLoadedLocators, BasePageLocators
from .base.base_page import BasePage

class DynamicallyLoaded(BasePage):

    def click_example_1(self):
        button = self.browser.find_element(*DynamicallyLoadedLocators.EXAMPLE_ONE_BUTTON)
        button.click()

    def click_example_2(self):
        button = self.browser.find_element(*DynamicallyLoadedLocators.EXAMPLE_TWO_BUTTON)
        button.click()

    def click_start(self):
        button = self.browser.find_element(*DynamicallyLoadedLocators.START_BUTTON)
        button.click()

    def go_to_page(self):
        link = self.browser.find_element(*DynamicallyLoadedLocators.DYNAMICALLY_LOADED_PAGE)
        link.click()

    def should_be_correct_page(self):
        text = self.get_text(*BasePageLocators.PAGE_NAME)
        correct_text = 'Dynamically Loaded'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_load_bar_present(self):
        load_bar = self.browser.find_element(*DynamicallyLoadedLocators.LOADING_BAR)
        assert load_bar.is_displayed(), 'should be load bar present, but not'

    def should_be_load_bar_disappeared(self):
        assert self.is_disappeared(*DynamicallyLoadedLocators.LOADING_BAR, 8), 'should be load bar dont present, but yes'

    def should_be_hello_word_present(self):
        final_text = self.browser.find_element(*DynamicallyLoadedLocators.FINISH_TEXT).text
        text = 'Hello World!'
        assert text == final_text, f'should be {text}, but present {final_text}'






