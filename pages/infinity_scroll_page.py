import time

from pages.locators import InfinityScrollLocators, BasePageLocators
from pages.base.base_page import BasePage


class InfinityScroll(BasePage):

    def go_to_page(self):
        link = self.browser.find_element(*InfinityScrollLocators.LOADED_PAGE)
        link.click()

    def should_be_correct_page(self):
        text = self.get_text(*BasePageLocators.PAGE_NAME)
        correct_text = 'Infinite Scroll'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_scrolled(self):
        before_scroll = len((self.browser.find_elements(*InfinityScrollLocators.SCROLLED_ROW)))
        self.scroll_down()
        after_scroll = len((self.browser.find_elements(*InfinityScrollLocators.SCROLLED_ROW)))
        assert after_scroll > before_scroll, f'after scroll should be more before, but {before_scroll} > {after_scroll} '

    def scroll_down(self):
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height > last_height:
                break
