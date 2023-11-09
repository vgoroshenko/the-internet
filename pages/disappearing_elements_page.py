from .base.base_page import BasePage
from .locators import DisappearingElementsLocators, BasePageLocators


class DisappearingElements(BasePage):

    def go_to_page(self):
        link = self.browser.find_element(*DisappearingElementsLocators.DISAPPERATING_PAGE)
        link.click()

    def should_be_correct_page(self):
        text = self.browser.find_element(*BasePageLocators.PAGE_NAME).text
        correct_text = 'Disappearing Elements'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_changed_buttons_count(self):
        start_len_button_list = len(self.browser.find_elements(*DisappearingElementsLocators.BUTTON_LIST))
        after_reload_len = start_len_button_list
        flag = 0
        while start_len_button_list == after_reload_len:
            self.browser.refresh()
            after_reload_len = len(self.browser.find_elements(*DisappearingElementsLocators.BUTTON_LIST))
            flag += 1
            if flag == 10:
                assert False, 'buttons count not changed'
