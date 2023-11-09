import os

from pages.locators import JQueryUIMenusLocators, BasePageLocators
from pages.base.base_page import BasePage


class JQuery(BasePage):

    def go_to_page(self):
        link = self.browser.find_element(*JQueryUIMenusLocators.LOADED_PAGE)
        link.click()

    def should_be_menu_page(self):
        text = self.get_text(*BasePageLocators.PAGE_NAME)
        correct_text = 'JQuery UI'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_correct_page(self):
        text = self.get_text(*BasePageLocators.PAGE_NAME)
        correct_text = 'JQueryUI - Menu'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_downloaded_file_extend(self, name):
        def is_docker():
            return False if os.name == 'nt' else True
        if is_docker():
            user = os.getlogin()
            download_dir = f"/home/{user}/Downloads"
        else:
            download_dir = f"E:\\Downloads"
        file_name = "menu." + name
        file_path = os.path.join(download_dir, file_name)
        assert os.path.exists(file_path), f'should be downloaded file, but not'

    def click_downloads(self):
        button_enabled = self.browser.find_element(*JQueryUIMenusLocators.BUTTON_ENABLED)
        button_enabled.click()
        button_downloads = self.browser.find_element(*JQueryUIMenusLocators.BUTTON_DOWNLOADS)
        button_downloads.click()

    def download_pdf(self):
        button_pdf = self.browser.find_element(*JQueryUIMenusLocators.BUTTON_PDF)
        button_pdf.click()

    def download_csv(self):
        button = self.browser.find_element(*JQueryUIMenusLocators.BUTTON_CSV)
        button.click()

    def download_excel(self):
        button = self.browser.find_element(*JQueryUIMenusLocators.BUTTON_EXCEL)
        button.click()

    def click_back_to_menu(self):
        button_enabled = self.browser.find_element(*JQueryUIMenusLocators.BUTTON_ENABLED)
        button_enabled.click()
        button_back = self.browser.find_element(*JQueryUIMenusLocators.BUTTON_BACK)
        button_back.click()

    def click_menu(self):
        button_menu = self.browser.find_element(*JQueryUIMenusLocators.LOADED_PAGE)
        button_menu.click()