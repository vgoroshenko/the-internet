from .base.base_page import BasePage
from .locators import ContextMenuLocators


class ContextMenu(BasePage):

    def go_to_page(self):
        link = self.browser.find_element(*ContextMenuLocators.CONTEXT_PAGE)
        link.click()

    def press_box_button(self):
        button = self.browser.find_element(*ContextMenuLocators.BOX_BUTTON)
        self.right_click(button)

    def should_be_correct_page(self):
        text = self.browser.find_element(*ContextMenuLocators.PAGE_NAME).text
        assert 'Context Menu' in text, f'should be "Context Menu", but "{text}"'

    def should_be_correct_context(self):
        text = self.get_alert_text()
        assert 'context menu' in text, f'should be context menu, but {text}'

    def should_alert_present(self):
        assert self.alert_is_present(), 'should alert present, but not'
