from pages.locators import FramesLocators, BasePageLocators
from pages.base.base_page import BasePage


class Frames(BasePage):

    def go_to_page(self):
        link = self.browser.find_element(*FramesLocators.LOADED_PAGE)
        link.click()

    def should_be_correct_page(self):
        text = self.get_text(*BasePageLocators.PAGE_NAME)
        correct_text = 'Frames'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def click_nested_frames(self):
        button = self.browser.find_element(*FramesLocators.NESTED_FRAMES_BUTTON)
        button.click()

    def click_i_frames(self):
        button = self.browser.find_element(*FramesLocators.IFRAMES_BUTTON)
        button.click()

    def should_be_left_frame(self):
        self.switch_to_frame_with_locator(*FramesLocators.FRAME_LEFT, FramesLocators.FRAMES)
        text = self.get_text(*FramesLocators.FRAME_BODY)
        assert 'LEFT' == text, f'should be text in frame LEFT, but {text}'

    def write_text_in_iframe(self):
        self.switch_to_frame(*FramesLocators.IFRAME_ID)
        field = self.browser.find_element(*FramesLocators.FIELD_IFRAME)
        field.send_keys('test')

    def should_be_test_text_in_iframe(self):
        text = self.get_text(*FramesLocators.FIELD_IFRAME)
        assert 'test' in text, f'should be "test" in iframe text, but {text}'
