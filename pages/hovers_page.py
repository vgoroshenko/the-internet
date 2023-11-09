from pages.locators import HoverLocators, BasePageLocators
from pages.base.base_page import BasePage


class Hover(BasePage):

    def should_be_check_all_profile(self):
        profiles = self.browser.find_elements(*HoverLocators.PERSONS)
        for i in range(len(profiles)):
            num = i + 1
            self.click_profile(num)
            self.should_be_profile(num)
            self.open()
            self.go_to_page()

    def new_index(self, lst):
        lst.insert(0,' ')
        return lst

    def click_profile(self, num):
        self.mouse_move_to_profile(num)
        profile_link = self.browser.find_elements(*HoverLocators.PERSONS_LINK)
        profile_link = self.new_index(profile_link)
        profile_link[num].click()

    def go_to_page(self):
        link = self.browser.find_element(*HoverLocators.LOADED_PAGE)
        link.click()

    def mouse_move_to_profile(self, num):
        profile = self.browser.find_elements(*HoverLocators.PERSONS)
        profile = self.new_index(profile)
        self.move_mouse_to_element(profile[num])

    def should_be_hover_profile_present(self, num):
        profile_name = self.browser.find_elements(*HoverLocators.PERSONS_NAME)
        profile_name = self.new_index(profile_name)
        assert True == self.is_element_displayed(profile_name[num]), 'should be present hover profile but not'

    def should_be_profile(self, num):
        current_url = self.browser.current_url
        assert f'/users/{num}' in current_url, f'should be users/{num}, but {current_url}'

    def should_be_correct_page(self):
        text = self.get_text(*BasePageLocators.PAGE_NAME)
        correct_text = 'Hovers'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'
