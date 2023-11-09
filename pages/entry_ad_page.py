from pages.locators import EntryAdLocators, BasePageLocators
from pages.base.base_page import BasePage


class EntryAd(BasePage):

    def go_to_page(self):
        link = self.browser.find_element(*EntryAdLocators.LOADED_PAGE)
        link.click()

    def click_re_enable_button(self):
        button = self.browser.find_element(*EntryAdLocators.RE_ENABLE_BUTTON)
        button.click()

    def click_close_popup(self):
        self.should_be_popup_present()
        button = self.browser.find_element(*EntryAdLocators.CLOSE_BUTTON)
        button.click()

    def should_be_correct_page(self):
        text = self.get_text(*BasePageLocators.PAGE_NAME)
        correct_text = 'Entry Ad'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_popup_present(self):
        assert self.is_element_present_timeout(*EntryAdLocators.POPUP), 'should popup present, but not'

    def should_be_popup_disappeared(self):
        assert self.is_disappeared(*EntryAdLocators.POPUP), 'should popup dont present, but yes'
