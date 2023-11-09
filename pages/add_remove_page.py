from pages.base.base_page import BasePage
from pages.locators import AddRemoveLocators


class AddRemove(BasePage):
    def go_to_module(self):
        link = self.browser.find_element(*AddRemoveLocators.ADD_REMOVE_PAGE)
        link.click()

    def should_be_add_remove_page_present(self):
        self.should_be_add_button_present()

    def should_be_add_button_present(self):
        assert self.is_element_present(*AddRemoveLocators.ADD_BUTTON), 'should be Add button'

    def should_be_remove_button_present(self):
        assert self.is_element_present(*AddRemoveLocators.ADD_BUTTON), 'should be Delete button'

    def should_removed_element(self):
        assert self.is_disappeared(*AddRemoveLocators.DELETE_BUTTON), 'should not present Delete button'

    def should_be_present_remove_buttons_count(self, num):
        buttons_count = len(self.browser.find_elements(*AddRemoveLocators.DELETE_BUTTON))
        assert buttons_count == num, f'should be {num} buttons, but present {buttons_count}'

    def press_add_buttont_count(self, num):
        for _ in range(num):
            self.press_add_button()

    def press_add_button(self):
        button = self.browser.find_element(*AddRemoveLocators.ADD_BUTTON)
        button.click()

    def press_delete_button(self):
        button = self.browser.find_element(*AddRemoveLocators.DELETE_BUTTON)
        button.click()
