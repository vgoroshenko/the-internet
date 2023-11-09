import time

from pages.locators import GeolocationLocators, BasePageLocators
from pages.base.base_page import BasePage


class Geolocation(BasePage):

    def go_to_page(self):
        link = self.browser.find_element(*GeolocationLocators.LOADED_PAGE)
        link.click()

    def should_be_correct_page(self):
        text = self.get_text(*BasePageLocators.PAGE_NAME)
        correct_text = 'Geolocation'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def set_coordinates(self):
        self.browser.execute_script(
            "navigator.geolocation.getCurrentPosition = function(success) { success({coords: {latitude: 51.5074, longitude: -0.1278}}); }")

    def click_where_i_am(self):
        button = self.browser.find_element(*GeolocationLocators.BUTTON_WHERE_I_AM)
        button.click()

    def click_google_link(self):
        button = self.browser.find_element(*GeolocationLocators.BUTTON_GOOGLE_MAP)
        button.click()

    def should_be_present_coordinates(self):
        lat = self.is_element_present(*GeolocationLocators.LATITUDE_COORD)
        long = self.is_element_present(*GeolocationLocators.LONGITUDE_COORD)
        assert lat and long == True, 'should be present coordinates, but not'

    def should_be_present_google_link(self):
        link = self.is_element_present(*GeolocationLocators.BUTTON_GOOGLE_MAP)
        assert link, 'should present google link, but not'

    def should_be_google_page(self):
        url = self.browser.current_url
        assert 'google.com' in url, f'should be present google url, but {url}'
