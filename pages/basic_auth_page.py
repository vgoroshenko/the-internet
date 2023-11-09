from pages.base.base_page import BasePage
from .locators import BasicAuthLocators


class BasicAuth(BasePage):

    def go_to_module(self):
        self.browser.get('http://admin:admin@172.17.0.1:5000/basic_auth')

    def go_to_failed_module(self):
        self.browser.get('http://admin:admin1@172.17.0.1:5000/basic_auth')

    def should_be_success_basic_auth_page(self):
        text = self.browser.find_element(*BasicAuthLocators.CONGRAT_MESSAGE).text
        assert 'Congratulations!' in text, f'should be Congratulations, but present {text}'

    def should_be_present_failed_message(self):
        text = self.browser.find_element(*BasicAuthLocators.FAILED_MESSAGE).text
        assert '' in text, f'should be Not authorized, but present {text}'
