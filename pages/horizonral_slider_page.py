from pages.locators import HorizontalSliderLocators, BasePageLocators
from pages.base.base_page import BasePage


class HorizontalSlider(BasePage):

    def go_to_page(self):
        link = self.browser.find_element(*HorizontalSliderLocators.LOADED_PAGE)
        link.click()

    def should_be_correct_page(self):
        text = self.get_text(*BasePageLocators.PAGE_NAME)
        correct_text = 'Horizontal Slider'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def move_slider_max(self):
        self.should_be_min_slider_value()
        self.drag_to_element(HorizontalSliderLocators.SLIDER, HorizontalSliderLocators.SLIDER_VALUE)

    def move_slider_min(self):
        button = self.browser.find_element(*HorizontalSliderLocators.SLIDER)
        button.click()
        #self.drag_to_element(HorizontalSliderLocators.SLIDER_VALUE, HorizontalSliderLocators.SLIDER)

    def should_be_value_5(self):
        value = self.get_text(*HorizontalSliderLocators.SLIDER_VALUE)
        assert value == '5', f'should be 5 in slider value, but {value}'

    def should_be_min_slider_value(self):
        value = self.get_text(*HorizontalSliderLocators.SLIDER_VALUE)
        assert value == '0' or '2.5', f'should be 0 in slider value, but {value}'
