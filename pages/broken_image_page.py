from pages.locators import BrokenImagesLocators
from pages.base.base_page import BasePage

class ImageNotFoundError(Exception):
    pass

class BrokenImages(BasePage):

    def go_to_module(self):
        link = self.browser.find_element(*BrokenImagesLocators.BROKEN_IMAGE_PAGE)
        link.click()

    def should_present_broken_image_page(self):
        text = self.browser.find_element(*BrokenImagesLocators.PAGE_NAME).text
        assert 'Broken Images' in text, f'should be present Broken Images page, but present "{text}"'

    def should_not_present_errors(self):
        logs = self.browser.get_log("browser")
        errors = [log for log in logs if log['level'] == 'SEVERE' and 'favicon.ico' not in log['message'] and 'chrome-error' not in log['message']]
        if errors:
            raise ImageNotFoundError(f'Есть ошибки {len(errors)} / {errors}')