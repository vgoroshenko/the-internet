import pytest

from pages.exit_intent_page import ExitIntent


def test_go_to_page(browser):
    page = ExitIntent(browser)
    page.go_to_page()
    page.should_be_correct_page()


@pytest.mark.xfail  # Dont work in docker
class TestPopup():
    def test_show_popup(self, browser):
        page = ExitIntent(browser)
        page.go_to_page()
        page.move_mouse_out()
        page.should_be_popup_present()

    def test_close_popup(self, browser):
        page = ExitIntent(browser)
        page.go_to_page()
        page.move_mouse_out()
        page.click_close_popup()
        page.should_be_popup_disappeared()
