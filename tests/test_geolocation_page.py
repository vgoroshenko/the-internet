from pages.geolocation_page import Geolocation


def test_go_to_page(browser):
    page = Geolocation(browser)
    page.go_to_page()
    page.should_be_correct_page()


def test_present_geolocation(browser):
    page = Geolocation(browser)
    page.go_to_page()
    page.set_coordinates()
    page.click_where_i_am()
    page.should_be_present_coordinates()


def test_google_link(browser):
    page = Geolocation(browser)
    page.go_to_page()
    page.set_coordinates()
    page.click_where_i_am()
    page.should_be_present_google_link()
    page.click_google_link()
    page.should_be_google_page()
