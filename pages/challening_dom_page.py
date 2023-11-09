from pages.locators import ChallengingDomLocators
from pages.base.base_page import BasePage


class ChallengingDom(BasePage):

    def go_to_page(self):
        link = self.browser.find_element(*ChallengingDomLocators.CHALLENGING_DOM_PAGE)
        link.click()

    def should_be_challenging_dom_page(self):
        text = self.browser.find_element(*ChallengingDomLocators.PAGE_NAME).text
        assert 'Challenging DOM' in text, f'Should be Challenging DOM, but {text}'

    def should_check_buttons(self):
        for i in range(3):
            button = self.browser.find_element(*ChallengingDomLocators.FIRST_BUTTON)
            button.click()
            button = self.browser.find_element(*ChallengingDomLocators.SECOND_BUTTON)
            button.click()
            button = self.browser.find_element(*ChallengingDomLocators.THIRD_BUTTON)
            button.click()