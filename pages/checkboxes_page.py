from pages.locators import CheckboxesLocators
from pages.base.base_page import BasePage


class Checkboxes(BasePage):

    def go_to_page(self):
        link = self.browser.find_element(*CheckboxesLocators.CHECKBOXES_PAGE)
        link.click()

    def press_first_checkbox(self):
        button = self.browser.find_element(*CheckboxesLocators.FIRST_CHECKBOX)
        button.click()

    def press_second_checkbox(self):
        button = self.browser.find_element(*CheckboxesLocators.SECOND_CHECKBOX)
        button.click()

    def should_be_checkboxes_page(self):
        text = self.get_text(*CheckboxesLocators.PAGE_NAME)
        assert 'Checkboxes' in text, f'Should be Checkboxes, but {text}'

    def should_be_checked_first_checkbox(self):
        checkbox = self.is_checked(*CheckboxesLocators.FIRST_CHECKBOX)
        assert checkbox == True, 'Should be checked, but no'

    def should_be_checked_second_checkbox(self):
        checkbox = self.is_checked(*CheckboxesLocators.SECOND_CHECKBOX)
        assert checkbox == True, 'Should be checked, but no'

    def should_be_not_checked_first_checkbox(self):
        checkbox = self.is_checked(*CheckboxesLocators.FIRST_CHECKBOX)
        assert checkbox == False, 'Should be not checked, but yes'

    def should_be_not_checked_second_checkbox(self):
        checkbox = self.is_checked(*CheckboxesLocators.SECOND_CHECKBOX)
        assert checkbox == False, 'Should be not checked, but yes'
