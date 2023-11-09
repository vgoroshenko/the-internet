import pytest

from pages.entry_ad_page import EntryAd

def test_go_to_page(browser):
    page = EntryAd(browser)
    page.go_to_page()
    page.should_be_correct_page()

def test_show_popup(browser):
    page = EntryAd(browser)
    page.go_to_page()
    page.should_be_popup_present()

def test_close_popup(browser):
    page = EntryAd(browser)
    page.go_to_page()
    page.click_close_popup()
    page.should_be_popup_disappeared()

@pytest.mark.xfail #Need refactor
def test_re_enable_popup(browser):
    page = EntryAd(browser)
    page.go_to_page()
    page.click_close_popup()
    page.click_re_enable_button()
    page.should_be_popup_present()
    page.click_close_popup()
    page.should_be_popup_disappeared()
