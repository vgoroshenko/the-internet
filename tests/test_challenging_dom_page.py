from pages.challening_dom_page import ChallengingDom

def test_present_challenging_dom_page(browser):
    page = ChallengingDom(browser)
    page.go_to_page()
    page.should_be_challenging_dom_page()

def test_unique_elements_after_click_button(browser):
    page = ChallengingDom(browser)
    page.go_to_page()
    page.should_check_buttons()