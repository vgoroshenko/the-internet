from pages.ab_page import ABPage


def test_ab_page(browser):
    page = ABPage(browser)
    page.open()
    page.go_to_ab_page()
    page.should_be_ab_page()
