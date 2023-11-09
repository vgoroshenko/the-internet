from .base.base_page import BasePage
from .locators import DynamicContentLocators, BasePageLocators


class DynamicContent(BasePage):

    def change_content(self):
        button = self.browser.find_element(*DynamicContentLocators.CHANGE_CONTENT_BUTTON)
        button.click()

    def go_to_page(self):
        link = self.browser.find_element(*DynamicContentLocators.DYNAMIC_CONTENT_PAGE)
        link.click()

    def should_be_correct_page(self):
        text = self.get_text(*BasePageLocators.PAGE_NAME)
        correct_text = 'Dynamic Content'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_changed_content_after_change(self):
        text_elements = [i.text for i in self.browser.find_elements(*DynamicContentLocators.ALL_TEXT_CONTENT_ELEMENTS)]
        self.change_content()
        elements2 = [i.text for i in self.browser.find_elements(*DynamicContentLocators.ALL_TEXT_CONTENT_ELEMENTS)]
        flag = True
        for i in elements2:
            if i in text_elements:
                flag = False
        assert flag, 'should be changed text, but not'

    def should_be_not_changed_second_row_content(self):
        elements = self.browser.find_elements(*DynamicContentLocators.ALL_TEXT_CONTENT_ELEMENTS)
        text = elements[0].text
        self.change_content()
        elements = self.browser.find_elements(*DynamicContentLocators.ALL_TEXT_CONTENT_ELEMENTS)
        text_after = elements[0].text
        assert text == text_after, f'should be not changed text, but yes {text[0:10]} and {text_after[0:10]}'


