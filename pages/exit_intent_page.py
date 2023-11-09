import time

from pages.locators import ExitIntentLocators, BasePageLocators
from pages.base.base_page import BasePage
import pyautogui


class ExitIntent(BasePage):

    def go_to_page(self):
        link = self.browser.find_element(*ExitIntentLocators.LOADED_PAGE)
        link.click()

    def click_close_popup(self):
        self.should_be_popup_present()
        button = self.browser.find_element(*ExitIntentLocators.CLOSE_BUTTON)
        button.click()

    def move_mouse_out(self):
        x, y = pyautogui.position()
        time.sleep(1)
        pyautogui.moveTo(100, -100, duration=1)


    def should_be_correct_page(self):
        text = self.get_text(*BasePageLocators.PAGE_NAME)
        correct_text = 'Exit Intent'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_popup_present(self):
        assert self.is_element_present_timeout(*ExitIntentLocators.POPUP), 'should popup present, but not'

    def should_be_popup_disappeared(self):
        assert self.is_disappeared(*ExitIntentLocators.POPUP), 'should popup dont present, but yes'
