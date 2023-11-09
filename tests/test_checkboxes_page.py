from pages.checkboxes_page import Checkboxes


def test_present_checkboxes_page(browser):
    page = Checkboxes(browser)
    page.go_to_page()
    page.should_be_checkboxes_page()
    page.should_be_checked_second_checkbox()


def test_press_checkbox(browser):
    page = Checkboxes(browser)
    page.go_to_page()
    page.press_first_checkbox()
    page.should_be_checked_first_checkbox()
    page.press_first_checkbox()
    page.should_be_not_checked_first_checkbox()
