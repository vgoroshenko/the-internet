from .base.base_page import BasePage
from .locators import ABPageLocators


class ABPage(BasePage):

    def go_to_ab_page(self):
        link = self.browser.find_element(*ABPageLocators.AB_PAGE)
        link.click()
    def should_be_ab_page(self):
        text = self.browser.find_element(*ABPageLocators.NO_AB_TEXT).text
        assert 'No A/B Test' in text, f'should be "No A/B Test", but "{text}"'