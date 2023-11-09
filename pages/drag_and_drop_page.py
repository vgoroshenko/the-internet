from .base.base_page import BasePage
from .locators import DragAndDropLocators, BasePageLocators


class DragAndDrop(BasePage):

    def drag_to_element_b(self):
        self.drag_to_element(DragAndDropLocators.BOX_A, DragAndDropLocators.BOX_B)

    def go_to_page(self):
        link = self.browser.find_element(*DragAndDropLocators.DRAG_AND_DROP_PAGE)
        link.click()

    def should_be_correct_page(self):
        text = self.get_text(*BasePageLocators.PAGE_NAME)
        correct_text = 'Drag and Drop'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_change_text(self):
        text = self.get_text(*DragAndDropLocators.BOX_A)
        assert 'B' == text, f'Should be "B", but {text}'
